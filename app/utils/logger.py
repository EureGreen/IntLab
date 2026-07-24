import logging
from pathlib import Path

from app.config import settings


log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("backend")

logger.setLevel(logging.INFO)

handler = logging.FileHandler(
    settings.LOG_FILE,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.handlers.clear()
logger.addHandler(handler)