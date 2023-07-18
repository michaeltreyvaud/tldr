from typing import Any


class Environment:
    def __init__(self, env_vars: dict[str, Any]) -> None:
        self.environment = env_vars.get("ENVIRONMENT", "dev")
        self.port = int(env_vars.get("PORT", 3000))
        self.app_name = env_vars.get("APP_NAME", "")
        self.reddit_client_id = env_vars.get("REDDIT_CLIENT_ID", "")
        self.reddit_client_secret = env_vars.get("REDDIT_CLIENT_SECRET", "")
        self.open_ai_api_key = env_vars.get("OPEN_AI_API_KEY", "")

    def get_environment(self) -> str:
        return self.environment

    def get_port(self) -> int:
        return self.port

    def get_app_name(self) -> str:
        return self.app_name

    def get_reddit_client_id(self) -> str:
        return self.reddit_client_id

    def get_reddit_client_secret(self) -> str:
        return self.reddit_client_secret

    def get_open_ai_api_key(self) -> str:
        return self.open_ai_api_key
