from fastapi import FastAPI
from .schemas import WebsiteIn

app = FastAPI(title="FastAPI URL Validator", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/validate")
def validate(payload: WebsiteIn):
    # If invalid, FastAPI returns 422 automatically for schema errors.
    # We return the normalized string value here.
    return {"ok": True, "website": str(payload.website)}
