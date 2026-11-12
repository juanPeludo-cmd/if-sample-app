"""Partner integrations: a ping that checks the partner's API key with app.auth.keys."""

import inspect
import os

from fastapi import APIRouter, HTTPException, Request

from app.auth import keys

router = APIRouter(prefix="/partner")

PARTNER_KEY = os.environ.get("PARTNER_API_KEY", "partner-key-1")


@router.get("/ping")
def ping(request: Request, api_key: str = "") -> dict[str, str]:
    """200 when the partner's key matches. `check_key` is given what its first parameter
    asks for: the request headers (X-API-Key) when it takes headers, else the `api_key`
    query parameter."""
    first = next(iter(inspect.signature(keys.check_key).parameters), "")
    given: dict[str, str] | str = api_key
    if "header" in first:
        value = request.headers.get("x-api-key")
        given = {"X-API-Key": value} if value is not None else {}
    if not keys.check_key(given, PARTNER_KEY):
        raise HTTPException(401, "invalid partner key")
    return {"partner": "ok"}
