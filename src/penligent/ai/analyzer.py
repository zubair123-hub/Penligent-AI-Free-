"""Vulnerability Analyzer using AI"""

from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class Vulnerability:
    """Represents a security vulnerability"""
    id: str
    name: str
    severity: str  # Critical, High, Medium, Low
    description: str
    affected_component: str
    cvss_score: float
    remediation: str


class VulnerabilityAnalyzer:
    """Analyzes and prioritizes vulnerabilities using AI"""

    def __init__(self, llm_engine):
        self.llm_engine = llm_engine
        self.vulnerabilities: List[Vulnerability] = []

    def add_vulnerability(self, vuln: Vulnerability) -> None:
        """Add vulnerability to analysis queue"""
        self.vulnerabilities.append(vuln)

    def analyze_all(self) -> List[Dict[str, Any]]:
        """Analyze all vulnerabilities and get AI insights"""
        results = []
        for vuln in self.vulnerabilities:
            analysis = self._analyze_single(vuln)
            results.append(analysis)
        return results

    def _analyze_single(self, vuln: Vulnerability) -> Dict[str, Any]:
        """Analyze single vulnerability with AI"""
        prompt = f"""Provide detailed security analysis for this vulnerability:
        Name: {vuln.name}
        Severity: {vuln.severity}
        CVSS Score: {vuln.cvss_score}
        Description: {vuln.description}
        
Provide: risk level, exploit probability, business impact, and urgent actions needed."""
        
        analysis = self.llm_engine.analyze(prompt)
        
        return {
            "vulnerability_id": vuln.id,
            "vulnerability_name": vuln.name,
            "severity": vuln.severity,
            "cvss_score": vuln.cvss_score,
            "ai_analysis": analysis,
            "recommended_remediation": vuln.remediation
        }

    def prioritize(self) -> List[Vulnerability]:
        """Prioritize vulnerabilities by severity and risk"""
        severity_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
        return sorted(
            self.vulnerabilities,
            key=lambda x: (severity_order.get(x.severity, 999), -x.cvss_score)
        )
