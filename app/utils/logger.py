import logging
from pathlib import Path

from app.config import settings


Path("data/logs").mkdir(
    parents=True,
    exist_ok=True
)


logger = logging.getLogger("backend")

logger.setLevel(logging.INFO)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


file_handler = logging.FileHandler(
    settings.LOG_FILE,
    encoding="utf-8"
)

file_handler.setFormatter(formatter)


if not logger.handlers:
    logger.addHandler(file_handler)