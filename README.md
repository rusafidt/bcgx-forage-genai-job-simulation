<p align="center">
  <img src="https://cdn-assets.theforage.com/images/meta-image-homepage.png" alt="Forage" width="520" />
</p>

<p align="center">
  <img src="https://cdn-assets.theforage.com/firm_logos/firm-logo-ticker-logos/v2/other/bcg.svg" alt="BCG" width="160" />
</p>

# BCG x Forage Financial Chatbot Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

This repository contains my Forage project submission, split into two parts:
- Task 1: EDGAR data analysis in Jupyter Notebook
- Task 2: FastAPI-based financial chatbot using predefined query-response mapping

## Certificate

- Forage Completion Certificate (PDF): [View Certificate](./certificate/BCG_Forage_Certificate.pdf)

## What This Project Contains

- `Task 1/`:
  - Financial analysis notebook
  - Raw extracted data files (CSV/XLSX)
- `Task 2/`:
  - Chatbot API code
  - Query-response JSON file
  - Tests
  - Documentation and test results
- `requirements.txt`:
  - Python dependencies for running and testing

## Task 1 (Data Analysis)

Task 1 is the financial data analysis part of the project.
It analyzes EDGAR extracted data for selected companies and summarizes key financial metrics and trends.

- Notebook: [`Task 1/edgar_data_analysis.ipynb`](./Task%201/edgar_data_analysis.ipynb)
- Data file (CSV): [`Task 1/data/EDGAR Entity Extracted Data.csv`](./Task%201/data/EDGAR%20Entity%20Extracted%20Data.csv)

## Task 2 (Chatbot API)

Task 2 is the implementation part where the predefined financial Q&A chatbot is built.
The chatbot reads supported queries from JSON and returns mapped responses through an API.

- Main API file: [`Task 2/main.py`](./Task%202/main.py)
- Query/response mapping: [`Task 2/chatbot_responses.json`](./Task%202/chatbot_responses.json)
- Tests: [`Task 2/tests/test_main.py`](./Task%202/tests/test_main.py)
- Task documentation: [`Task 2/chatbot_documentation.md`](./Task%202/chatbot_documentation.md)
- Test output: [`Task 2/test_results.txt`](./Task%202/test_results.txt)

## How To Run `main.py` (Step by Step)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI app:

```bash
uvicorn "Task 2.main:app" --reload
```

4. Open in browser:
- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/test`

## How To Test The Chatbot

Run automated tests:

```bash
python -m pytest "Task 2/tests/test_main.py" -q
```

## Example Chat Request

`POST /chat` with JSON body:

```json
{
  "message": "what is the total revenue in 2025 (all companies combined)?"
}
```

Example response:

```json
{
  "response": "Total revenue in 2025 is $792,712,000,000."
}
```

## License

This project is licensed under the [MIT License](./LICENSE).
