import json
import time
import threading
from pathlib import Path

from app.config import settings


class RateLimitService:

    _lock = threading.Lock()

    def __init__(self):

        self.max_requests = settings.RATE_LIMIT_REQUESTS
        self.window_seconds = settings.RATE_LIMIT_WINDOW

        self.file = Path("data/ratelimit.json")

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file.exists():
            self.file.write_text(
                "{}",
                encoding="utf-8"
            )

    def is_allowed(self, ip: str) -> bool:

        now = int(time.time())

        with self._lock:

            data = self._load()

            requests = data.get(ip, [])

            requests = [
                ts
                for ts in requests
                if now - ts < self.window_seconds
            ]

            if len(requests) >= self.max_requests:

                data[ip] = requests
                self._save(data)

                return False

            requests.append(now)

            data[ip] = requests

            self._save(data)

            return True

    def _load(self):

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):

            return {}

    def _save(self, data):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )