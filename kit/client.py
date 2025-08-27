import os
import requests

class Client:
    def __init__(self, base_url=None, api_key=None, timeout=5):
        self.base_url = (base_url or os.getenv("PLAYPULSE_BASE_URL") or "http://localhost:8000").rstrip("/")
        self.api_key = api_key or os.getenv("PLAYPULSE_API_KEY")
        self.timeout = timeout

    def send(self, event_obj):
        url = f"{self.base_url}/collect"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload = event_obj.to_dict()
        r = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r