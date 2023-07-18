from typing import Any

from fastapi import APIRouter
from src.app.adapters.Runner import Runner


def create_router(adapter_runner: Runner) -> APIRouter:
    router = APIRouter()

    @router.get("/summarize")
    async def summarize() -> dict[str, Any]:
        res = adapter_runner.run()
        return res

    return router
