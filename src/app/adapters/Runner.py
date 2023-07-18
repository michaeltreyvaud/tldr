from typing import List, Any

from src.app.adapters.Adapter import Adapter


class Runner():
    def __init__(self, adapters: List[Adapter]) -> None:
        self.adapters = adapters

    def run(self) -> dict[str, Any]:
        res_dict = {}
        for adapter in self.adapters:
            adapter_name = adapter.get_name()
            adapter_summary = adapter.summarize()
            res_dict[adapter_name] = adapter_summary
        return res_dict
