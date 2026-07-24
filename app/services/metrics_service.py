import json
from pathlib import Path


class MetricsService:

    def __init__(self):

        self.file = Path(
            "data/metrics.json"
        )

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file.exists():

            self._save(
                {
                    "total_requests": 0,
                    "successful_requests": 0,
                    "failed_requests": 0
                }
            )


    def get_metrics(self):

        return self._load()


    def increment_success(self):

        data = self._load()

        data["total_requests"] += 1

        data["successful_requests"] += 1

        self._save(data)


    def increment_failed(self):

        data = self._load()

        data["total_requests"] += 1

        data["failed_requests"] += 1

        self._save(data)


    def _load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def _save(
        self,
        data
    ):

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