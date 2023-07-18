from typing import Any
from src.app.adapters.Adapter import Adapter


class Facebook(Adapter):
    name = 'facebook'

    def summarize(self) -> dict[str, Any]:
        return {"hello": "facebook"}
