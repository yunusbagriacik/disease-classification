import os
import sys
import logging

LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(name)s: %(message)s]"

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "running_logs.log")

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
