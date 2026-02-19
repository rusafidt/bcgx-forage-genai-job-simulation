import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

RESPONSES_PATH = Path(__file__).with_name("chatbot_responses.json")


def load_responses(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("chatbot_responses.json must contain a JSON object.")
    if "_default" not in data:
        raise ValueError("chatbot_responses.json must include a _default response.")
    return {str(key): str(value) for key, value in data.items()}


RESPONSES = load_responses(RESPONSES_PATH)


def get_chatbot_response(message: str) -> str:
    normalized = message.strip().lower()
    return RESPONSES.get(normalized, RESPONSES["_default"])


@app.get("/test")
def test():
    return {"message": "Test endpoint is working!"}


@app.get("/")
def root():
    return {
        "message": "Financial chatbot API is running.",
        "endpoints": ["GET /test", "POST /chat"],
    }


@app.post("/chat")
async def chat(request: Request):
    try:
        body: Any = await request.json()
    except json.JSONDecodeError:
        return JSONResponse(
            status_code=400,
            content={"response": "Invalid JSON body. Please send valid JSON."},
        )

    if not isinstance(body, dict):
        return JSONResponse(
            status_code=400,
            content={"response": "JSON body must be an object with a 'message' field."},
        )

    message = body.get("message")
    if not isinstance(message, str) or not message.strip():
        return {"response": "Please provide a message."}

    return {"response": get_chatbot_response(message)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
