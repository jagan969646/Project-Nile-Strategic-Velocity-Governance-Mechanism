import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str = "app_logger"):
    """
    Returns a configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # File name with date
    log_filename = f"{LOG_DIR}/{datetime.now().strftime('%Y-%m-%d')}.log"

    # File Handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger