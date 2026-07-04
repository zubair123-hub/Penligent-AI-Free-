"""Logging configuration for Penligent AI"""

import logging
import sys
from pathlib import Path
from typing import Optional
from loguru import logger


def setup_logger(name: str, level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """Configure and return logger instance"""
    # Remove default handlers
    logger.remove()

    # Add console handler
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level=level,
    )

    # Add file handler if specified
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        logger.add(
            log_file,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
            level=level,
            rotation="500 MB",
            retention="7 days",
        )

    return logger.bind(name=name)
