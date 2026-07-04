"""LLM Engine for AI-powered analysis"""

import os
from typing import Optional, Dict, Any
import openai
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""

    @abstractmethod
    def analyze(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Analyze input and return response"""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI GPT implementation"""

    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def analyze(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Analyze using OpenAI API"""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a cybersecurity expert and penetration testing analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2048
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"


class LocalLLMProvider(LLMProvider):
    """Local LLM implementation (e.g., Ollama, Llama2)"""

    def __init__(self, endpoint: str, model: str = "mistral"):
        self.endpoint = endpoint
        self.model = model

    def analyze(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Analyze using local LLM"""
        import requests
        try:
            response = requests.post(
                f"{self.endpoint}/api/generate",
                json={"model": self.model, "prompt": prompt, "stream": False},
                timeout=30
            )
            return response.json().get("response", "No response")
        except Exception as e:
            return f"Error connecting to local LLM: {str(e)}"


class LLMEngine:
    """Main LLM orchestration engine"""

    def __init__(self, provider_type: str = "openai", config: Optional[Dict[str, Any]] = None):
        self.provider_type = provider_type
        self.config = config or {}
        self.provider = self._initialize_provider()

    def _initialize_provider(self) -> LLMProvider:
        """Initialize the appropriate LLM provider"""
        if self.provider_type == "openai":
            api_key = self.config.get("api_key") or os.getenv("OPENAI_API_KEY")
            model = self.config.get("model", "gpt-4")
            return OpenAIProvider(api_key, model)
        elif self.provider_type == "local":
            endpoint = self.config.get("endpoint", "http://localhost:11434")
            model = self.config.get("model", "mistral")
            return LocalLLMProvider(endpoint, model)
        else:
            raise ValueError(f"Unknown provider: {self.provider_type}")

    def analyze(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Analyze input using configured provider"""
        return self.provider.analyze(prompt, context)

    def analyze_vulnerability(self, vulnerability_data: Dict[str, Any]) -> str:
        """Analyze vulnerability data and provide insights"""
        prompt = f"""Analyze this security vulnerability and provide recommendations:
        
Vulnerability: {vulnerability_data.get('name', 'Unknown')}
Severity: {vulnerability_data.get('severity', 'Unknown')}
Description: {vulnerability_data.get('description', '')}
Affected Component: {vulnerability_data.get('affected_component', '')}

Provide:
1. Risk assessment
2. Exploitation difficulty
3. Recommended remediation
4. Priority level"""
        return self.analyze(prompt)

    def generate_report(self, scan_results: Dict[str, Any]) -> str:
        """Generate AI-powered security report"""
        prompt = f"""Generate a professional security assessment report based on these findings:
        
{scan_results}

Include:
1. Executive Summary
2. Critical Findings
3. Risk Assessment
4. Remediation Plan
5. Conclusion"""
        return self.analyze(prompt)
