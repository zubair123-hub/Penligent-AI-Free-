"""Reconnaissance module for passive and active information gathering"""

from typing import Dict, List, Any
import requests
from dataclasses import dataclass


@dataclass
class ReconData:
    """Reconnaissance data structure"""
    target: str
    dns_records: Dict[str, Any]
    subdomains: List[str]
    open_ports: List[int]
    services: Dict[int, str]


class Reconnaissance:
    """Passive and active reconnaissance module"""

    def __init__(self, target: str):
        self.target = target
        self.data = ReconData(
            target=target,
            dns_records={},
            subdomains=[],
            open_ports=[],
            services={}
        )

    def gather_dns_info(self) -> Dict[str, Any]:
        """Gather DNS information"""
        import socket
        try:
            ip = socket.gethostbyname(self.target)
            self.data.dns_records['ip'] = ip
            self.data.dns_records['hostname'] = self.target
            return self.data.dns_records
        except socket.gaierror:
            return {"error": "Cannot resolve hostname"}

    def enumerate_subdomains(self) -> List[str]:
        """Enumerate subdomains (using common subdomains)"""
        common_subdomains = [
            "www", "mail", "ftp", "localhost", "webmail", "smtp",
            "pop", "ns1", "webdisk", "ns2", "cpanel", "whm", "autodiscover",
            "autoconfig", "m", "api", "admin", "test", "staging", "dev"
        ]
        found = []
        for sub in common_subdomains:
            try:
                import socket
                subdomain = f"{sub}.{self.target}"
                socket.gethostbyname(subdomain)
                found.append(subdomain)
            except:
                pass
        self.data.subdomains = found
        return found

    def get_results(self) -> ReconData:
        """Get all reconnaissance data"""
        return self.data
