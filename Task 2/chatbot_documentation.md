# Financial Chatbot Documentation

## Overview
This is a simple rule-based financial chatbot built with FastAPI.
It reads predefined query-response pairs from `chatbot_responses.json`.

## API
- Endpoint: `POST /chat`
- Request JSON: `{"message": "your query"}`
- Response JSON: `{"response": "answer"}`
- Health checks: `GET /` and `GET /test`

## How It Works
1. Receive `message` from request body.
2. Normalize input using trim + lowercase.
3. Lookup answer in `chatbot_responses.json`.
4. Return matching response or default fallback.
5. Validate malformed/invalid JSON request formats.

## Supported Query Set
The bot supports the predefined financial queries in `chatbot_responses.json`, including:
- total revenue (combined and company-specific)
- highest revenue company
- year-over-year change examples

## Limitations
- Not an AI/NLP chatbot; it is rule-based.
- Answers only predefined queries.
- No live data fetch; values are static from Task 1 analysis.
- Unexpected phrasing may return fallback.

## Testing
Automated tests are available in `tests/test_main.py`.
Sample test run output is recorded in `test_results.txt`.
