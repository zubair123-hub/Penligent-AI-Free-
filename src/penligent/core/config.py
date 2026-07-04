"""Configuration management for Penligent AI"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import json


class Config:
    """Centralized configuration management"""

    def __init__(self, env_file: Optional[str] = None):
        """Initialize configuration from environment variables and .env file"""
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()

        # API Configuration
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4")
        self.llm_provider = os.getenv("LLM_PROVIDER", "openai")
        self.local_llm_endpoint = os.getenv("LOCAL_LLM_ENDPOINT", "http://localhost:8000")

        # Database Configuration
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./penligent.db")

        # Logging Configuration
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_file = os.getenv("LOG_FILE", "./logs/penligent.log")
        self._ensure_log_dir()

        # Scanning Configuration
        self.max_threads = int(os.getenv("MAX_THREADS", "10"))
        self.timeout = int(os.getenv("TIMEOUT", "30"))
        self.retry_count = int(os.getenv("RETRY_COUNT", "3"))

        # Network Scanning
        self.enable_nmap = os.getenv("ENABLE_NMAP", "true").lower() == "true"
        self.nmap_path = os.getenv("NMAP_PATH", "/usr/bin/nmap")

        # API Server Configuration
        self.api_host = os.getenv("API_HOST", "0.0.0.0")
        self.api_port = int(os.getenv("API_PORT", "8080"))
        self.api_debug = os.getenv("API_DEBUG", "false").lower() == "true"

        # Output Configuration
        self.output_format = os.getenv("OUTPUT_FORMAT", "json")
        self.reports_dir = os.getenv("REPORTS_DIR", "./reports")
        self._ensure_reports_dir()

    def _ensure_log_dir(self) -> None:
        """Ensure log directory exists"""
        log_dir = Path(self.log_file).parent
        log_dir.mkdir(parents=True, exist_ok=True)

    def _ensure_reports_dir(self) -> None:
        """Ensure reports directory exists"""
        Path(self.reports_dir).mkdir(parents=True, exist_ok=True)

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "openai_api_key": "***" if self.openai_api_key else None,
            "openai_model": self.openai_model,
            "llm_provider": self.llm_provider,
            "database_url": self.database_url,
            "log_level": self.log_level,
            "max_threads": self.max_threads,
            "timeout": self.timeout,
            "enable_nmap": self.enable_nmap,
            "api_host": self.api_host,
            "api_port": self.api_port,
            "output_format": self.output_format,
        }
