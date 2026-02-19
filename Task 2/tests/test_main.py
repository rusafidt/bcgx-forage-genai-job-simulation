import importlib.util
from pathlib import Path

from fastapi.testclient import TestClient


def load_app():
    main_path = Path(__file__).resolve().parents[1] / "main.py"
    spec = importlib.util.spec_from_file_location("task2_main", main_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.app


client = TestClient(load_app())


def test_test_endpoint():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Test endpoint is working!"}


def test_chat_known_query():
    response = client.post(
        "/chat",
        json={"message": "what is the total revenue in 2025 (all companies combined)?"},
    )
    assert response.status_code == 200
    assert (
        response.json()["response"]
        == "Total revenue in 2025 is $792,712,000,000."
    )


def test_chat_query_normalization():
    response = client.post(
        "/chat",
        json={"message": "   What is the total revenue in 2025 for Apple?   "},
    )
    assert response.status_code == 200
    assert response.json()["response"] == "Total revenue in 2025 for Apple is $416,161,000,000."


def test_chat_missing_message():
    response = client.post("/chat", json={})
    assert response.status_code == 200
    assert response.json()["response"] == "Please provide a message."


def test_chat_unknown_query():
    response = client.post("/chat", json={"message": "What is gross margin in 2025?"})
    assert response.status_code == 200
    assert (
        response.json()["response"]
        == "Sorry, I do not have a predefined answer for that question yet."
    )


def test_chat_invalid_json_body():
    response = client.post(
        "/chat",
        content="{bad json}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 400
    assert response.json()["response"] == "Invalid JSON body. Please send valid JSON."


def test_chat_non_object_json():
    response = client.post("/chat", json=["hello"])
    assert response.status_code == 400
    assert (
        response.json()["response"]
        == "JSON body must be an object with a 'message' field."
    )
