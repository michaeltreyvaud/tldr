import praw
import os
import openai
from dotenv import load_dotenv
from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from src.dependencies.Environment import Environment

from src.app.routers.summarize import create_router as create_summarize_router
from src.app.routers.health import create_router as create_health_router
from src.app.adapters.Reddit import Reddit
from src.app.adapters.Runner import Runner

load_dotenv()
environment = Environment(dict(os.environ))
openai.api_key = environment.get_open_ai_api_key()
reddit_client = praw.Reddit(
    client_id=environment.get_reddit_client_id(),
    client_secret=environment.get_reddit_client_secret(),
    user_agent=environment.get_app_name(),
)
adapters = [Reddit(reddit_client=reddit_client, openai_client=openai)]
adapter_runner = Runner(adapters=adapters)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def init_routers(app: FastAPI) -> None:
    health_router = create_health_router()
    summarize_router = create_summarize_router(adapter_runner=adapter_runner)
    app.include_router(health_router)
    app.include_router(summarize_router)


def create_app() -> FastAPI:
    app = FastAPI(
        title=environment.get_app_name(),
        middleware=make_middleware(),
    )
    init_routers(app=app)
    return app


app = create_app()
