"""
logging.py
"""

import logging
from logging import Logger

from pydmt.static import LOGGER_NAME


def get_logger() -> Logger:
    """
    This function returns the logger for pydmt
    """
    return logging.getLogger(LOGGER_NAME)
