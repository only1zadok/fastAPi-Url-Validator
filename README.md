# FastAPI URL Validator (validation-only)

Validates user-submitted website URLs:
- Must be http/https
- Rejects localhost
- Rejects private/local IPs
- Rejects hostnames that resolve to private/local IP ranges

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Endpoints:
- GET http://127.0.0.1:8000/health
- POST http://127.0.0.1:8000/validate

Example request:
```bash
curl -X POST "http://127.0.0.1:8000/validate" \
  -H "Content-Type: application/json" \
  -d '{"website":"https://example.com"}'
```

## Tests

```bash
pytest -q
```
