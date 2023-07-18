from typing import Any

from fastapi import APIRouter


def create_router() -> APIRouter:
    router = APIRouter()

    @router.get("/health")
    async def health() -> dict[str, Any]:
        return {"in the pipe": "5x5"}

    return router
