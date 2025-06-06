import logging
import os
from datetime import datetime

LOGS_DIR = "hotel_res_logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")


logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(leveltime)s - %(messages)s",
    level=logging.INFO,
)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
