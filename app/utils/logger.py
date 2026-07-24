import logging
from pathlib import Path

from app.config import settings


log_path = Path(settings.LOG_FILE)

log_path.parent.mkdir(
    parents=True,
    exist_ok=True
)


logger = logging.getLogger("backend")

logger.setLevel(logging.INFO)


file_handler = logging.FileHandler(
    log_path,
    encoding="utf-8"
)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


file_handler.setFormatter(formatter)


logger.handlers.clear()
logger.addHandler(file_handler)