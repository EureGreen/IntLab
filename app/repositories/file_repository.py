from pathlib import Path
import json


class FileRepository:

    def __init__(self):
        self.base_path = Path("data")
        self.base_path.mkdir(exist_ok=True)

    def append_json(self, filename: str, data: dict):

        path = self.base_path / filename

        if path.exists():

            with open(path, "r", encoding="utf8") as f:
                content = json.load(f)

        else:
            content = []

        content.append(data)

        with open(path, "w", encoding="utf8") as f:
            json.dump(content, f, ensure_ascii=False, indent=4)