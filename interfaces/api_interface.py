from abc import ABC

import requests

class APIInterface(ABC):
    def _get(self, url: str, params: dict = None, headers: dict = None, timeout: int = 10) -> dict:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()

    def _build_url(self, base: str, endpoint: str, *segments: str) -> str:
        if not endpoint.strip():
            raise ValueError("Endpoint must not be empty.")

        all_parts = [base.rstrip("/"), endpoint.strip("/")] + [s.strip("/") for s in segments]
        return "/".join(all_parts)
