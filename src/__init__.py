"""Penligent AI - Advanced Pentesting Framework"""

__version__ = "0.1.0"
__author__ = "Penligent AI Team"

from .core.config import Config
from .core.logger import setup_logger

__all__ = ["Config", "setup_logger"]
