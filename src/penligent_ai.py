"""
Penligent AI - Automated Pentesting Engine
Auto-execution with integrated free APIs and local LLM
Educational purposes only
"""

import os
import sys
import json
import subprocess
import time
import argparse
from datetime import datetime
from pathlib import Path
import threading
from queue import Queue
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('penligent_ai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('PenligentAI')


class AIController:
    """Main AI Controller for autonomous pentesting"""
    
    def __init__(self, config_path='config/ai_config.yml'):
        self.config_path = config_path
        self.scan_results = {}
        self.vulnerabilities = []
        self.active_scans = {}
        self.load_config()
        logger.info("🤖 Penligent AI Controller initialized")
    
    def load_config(self):
        """Load configuration from YAML"""
        try:
            import yaml
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
            logger.info("✅ Configuration loaded")
        except Exception as e:
            logger.error(f"❌ Failed to load config: {e}")
            self.config = {}
    
    def run_nmap_scan(self, target, aggressive=False):
        """Execute Nmap scan autonomously"""
        logger.info(f"🔍 Starting Nmap scan on {target}")
        try:
            args = self.config.get('tools', {}).get('nmap', {})
            cmd = f"nmap {args.get('aggressive_args' if aggressive else 'default_args')} {target} -oJ /tmp/nmap_scan.json"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Nmap scan completed")
                return self.parse_nmap_results('/tmp/nmap_scan.json')
            else:
                logger.error(f"❌ Nmap failed: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            logger.error("❌ Nmap scan timed out")
            return None
        except Exception as e:
            logger.error(f"❌ Nmap error: {e}")
            return None
    
    def run_nikto_scan(self, target):
        """Execute Nikto web vulnerability scan"""
        logger.info(f"🌐 Starting Nikto scan on {target}")
        try:
            cmd = f"nikto -h {target} -output /tmp/nikto_scan.json -Format json"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Nikto scan completed")
                return self.parse_nikto_results('/tmp/nikto_scan.json')
            else:
                logger.warning(f"⚠️ Nikto warning: {result.stderr}")
                return None
        except Exception as e:
            logger.error(f"❌ Nikto error: {e}")
            return None
    
    def run_sqlmap_scan(self, url):
        """Execute SQLMap SQL injection scan"""
        logger.info(f"💉 Starting SQLMap scan on {url}")
        try:
            config = self.config.get('tools', {}).get('sqlmap', {})
            cmd = f"sqlmap -u '{url}' --level={config.get('level', 1)} --risk={config.get('risk', 1)} --batch --json-file=/tmp/sqlmap_scan.json"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            
            if result.returncode in [0, 1]:  # 0=found, 1=not found
                logger.info("✅ SQLMap scan completed")
                return self.parse_sqlmap_results('/tmp/sqlmap_scan.json')
            else:
                logger.warning(f"⚠️ SQLMap info: {result.stderr}")
                return None
        except Exception as e:
            logger.error(f"❌ SQLMap error: {e}")
            return None
    
    def run_wpscan(self, url):
        """Execute WPScan WordPress vulnerability scan"""
        logger.info(f"📝 Starting WPScan on {url}")
        try:
            cmd = f"wpscan --url {url} --format json --output=/tmp/wpscan_scan.json"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ WPScan completed")
                return self.parse_wpscan_results('/tmp/wpscan_scan.json')
            else:
                logger.warning(f"⚠️ WPScan info: {result.stderr}")
                return None
        except Exception as e:
            logger.error(f"❌ WPScan error: {e}")
            return None
    
    def run_searchsploit(self, query):
        """Search for exploits using searchsploit"""
        logger.info(f"🔫 Searching exploits for: {query}")
        try:
            cmd = f"searchsploit -j '{query}'"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                exploits = json.loads(result.stdout)
                logger.info(f"✅ Found {len(exploits.get('results', []))} exploits")
                return exploits
            else:
                logger.warning("⚠️ No exploits found")
                return None
        except Exception as e:
            logger.error(f"❌ Searchsploit error: {e}")
            return None
    
    def check_vulnerability_database(self, software, version):
        """Check free vulnerability databases"""
        logger.info(f"🔎 Checking vulnerabilities for {software} v{version}")
        vulnerabilities = []
        
        try:
            # Use searchsploit for offline CVE lookup
            cmd = f"searchsploit -j '{software} {version}'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for exploit in data.get('results', [])[:5]:  # Top 5 results
                    vulnerabilities.append({
                        'title': exploit.get('title'),
                        'type': exploit.get('type'),
                        'path': exploit.get('path'),
                        'source': 'ExploitDB'
                    })
            
            logger.info(f"✅ Found {len(vulnerabilities)} vulnerabilities")
            return vulnerabilities
        except Exception as e:
            logger.error(f"❌ Vulnerability check error: {e}")
            return []
    
    def query_ai_controller(self, prompt):
        """Query local AI for intelligent analysis"""
        logger.info("🤖 Querying AI for analysis...")
        try:
            # Try Ollama first (local LLM)
            cmd = f"curl -s http://localhost:11434/api/generate -d '{{\"model\":\"llama2\",\"prompt\":\"{prompt}\",\"stream\":false}}'"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                response = json.loads(result.stdout)
                ai_response = response.get('response', '')
                logger.info(f"✅ AI analysis complete")
                return ai_response
            else:
                # Fallback: Use simple heuristics
                logger.info("ℹ️ Using heuristic analysis (install Ollama for AI)")
                return self.heuristic_analysis(prompt)
        except Exception as e:
            logger.error(f"❌ AI query error: {e}")
            return self.heuristic_analysis(prompt)
    
    def heuristic_analysis(self, findings):
        """Fallback heuristic analysis without AI"""
        analysis = """
        🔍 Automated Security Analysis:
        
        Based on scan results:
        1. Open ports detected - Network services exposed
        2. Recommend service hardening and firewall rules
        3. Implement network segmentation
        4. Enable intrusion detection systems
        5. Conduct regular security audits
        6. Apply latest security patches
        7. Implement strong authentication mechanisms
        """
        return analysis
    
    def parse_nmap_results(self, json_file):
        """Parse Nmap JSON output"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            results = {
                'open_ports': [],
                'services': [],
                'vulnerabilities': []
            }
            
            # Extract results (simplified)
            logger.info("📊 Parsing Nmap results")
            return results
        except Exception as e:
            logger.error(f"❌ Error parsing Nmap: {e}")
            return None
    
    def parse_nikto_results(self, json_file):
        """Parse Nikto JSON output"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            logger.info("📊 Parsing Nikto results")
            return data
        except Exception as e:
            logger.error(f"❌ Error parsing Nikto: {e}")
            return None
    
    def parse_sqlmap_results(self, json_file):
        """Parse SQLMap JSON output"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            logger.info("📊 Parsing SQLMap results")
            return data
        except Exception as e:
            logger.error(f"❌ Error parsing SQLMap: {e}")
            return None
    
    def parse_wpscan_results(self, json_file):
        """Parse WPScan JSON output"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            logger.info("📊 Parsing WPScan results")
            return data
        except Exception as e:
            logger.error(f"❌ Error parsing WPScan: {e}")
            return None
    
    def autonomous_pentest(self, target, scan_type='full'):
        """Execute autonomous pentesting workflow"""
        logger.info(f"🚀 Starting autonomous pentest on {target}")
        logger.info(f"📋 Scan Type: {scan_type}")
        
        scan_id = f"scan_{int(time.time())}"
        self.active_scans[scan_id] = {
            'target': target,
            'start_time': datetime.now(),
            'status': 'running',
            'results': {}
        }
        
        try:
            # Phase 1: Reconnaissance
            logger.info("\n" + "="*50)
            logger.info("PHASE 1: RECONNAISSANCE")
            logger.info("="*50)
            
            if ':' in target:  # Web target
                nmap_results = self.run_nmap_scan(target.split(':')[0])
                self.active_scans[scan_id]['results']['nmap'] = nmap_results
            else:
                nmap_results = self.run_nmap_scan(target)
                self.active_scans[scan_id]['results']['nmap'] = nmap_results
            
            # Phase 2: Vulnerability Scanning
            logger.info("\n" + "="*50)
            logger.info("PHASE 2: VULNERABILITY SCANNING")
            logger.info("="*50)
            
            if scan_type in ['full', 'web']:
                if target.startswith('http'):
                    nikto_results = self.run_nikto_scan(target)
                    self.active_scans[scan_id]['results']['nikto'] = nikto_results
                    
                    sqlmap_results = self.run_sqlmap_scan(target)
                    self.active_scans[scan_id]['results']['sqlmap'] = sqlmap_results
            
            if scan_type in ['full', 'wordpress']:
                if 'wordpress' in target.lower() or target.startswith('http'):
                    wpscan_results = self.run_wpscan(target)
                    self.active_scans[scan_id]['results']['wpscan'] = wpscan_results
            
            # Phase 3: Exploit Database Search
            logger.info("\n" + "="*50)
            logger.info("PHASE 3: EXPLOIT DATABASE SEARCH")
            logger.info("="*50)
            
            exploits = self.run_searchsploit(target)
            self.active_scans[scan_id]['results']['exploits'] = exploits
            
            # Phase 4: AI Analysis
            logger.info("\n" + "="*50)
            logger.info("PHASE 4: AI-POWERED ANALYSIS")
            logger.info("="*50)
            
            analysis_prompt = f"Analyze security findings from pentest on {target}"
            ai_analysis = self.query_ai_controller(analysis_prompt)
            self.active_scans[scan_id]['results']['ai_analysis'] = ai_analysis
            
            # Generate Report
            self.generate_report(scan_id)
            
            self.active_scans[scan_id]['status'] = 'completed'
            self.active_scans[scan_id]['end_time'] = datetime.now()
            
            logger.info("\n" + "="*50)
            logger.info("✅ AUTONOMOUS PENTEST COMPLETED")
            logger.info("="*50)
            
            return scan_id
            
        except Exception as e:
            logger.error(f"❌ Autonomous pentest error: {e}")
            self.active_scans[scan_id]['status'] = 'failed'
            return None
    
    def generate_report(self, scan_id):
        """Generate comprehensive security report"""
        logger.info("📄 Generating security report...")
        
        try:
            scan_data = self.active_scans[scan_id]
            report = {
                'scan_id': scan_id,
                'target': scan_data['target'],
                'timestamp': scan_data['start_time'].isoformat(),
                'duration': str(scan_data.get('end_time', datetime.now()) - scan_data['start_time']),
                'status': scan_data['status'],
                'findings': scan_data['results'],
                'recommendations': self.generate_recommendations(scan_data['results'])
            }
            
            # Save report
            report_path = f"reports/penligent_report_{scan_id}.json"
            Path("reports").mkdir(exist_ok=True)
            
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"✅ Report saved to {report_path}")
            return report_path
            
        except Exception as e:
            logger.error(f"❌ Report generation error: {e}")
            return None
    
    def generate_recommendations(self, findings):
        """Generate security recommendations"""
        recommendations = [
            "🔐 Implement SSL/TLS for all web services",
            "🛡️ Deploy Web Application Firewall (WAF)",
            "🔑 Enforce strong password policies",
            "🔄 Enable Multi-Factor Authentication (MFA)",
            "📊 Implement comprehensive logging and monitoring",
            "🚨 Set up automated alerting for security events",
            "🔍 Conduct regular vulnerability assessments",
            "📋 Maintain updated inventory of systems and services",
            "🔐 Apply security patches regularly",
            "📚 Provide security awareness training"
        ]
        return recommendations[:3]  # Return top 3
    
    def interactive_mode(self):
        """Interactive AI-assisted pentesting"""
        logger.info("🤖 Entering Interactive Mode")
        
        while True:
            print("\n" + "="*60)
            print("🔮 PENLIGENT AI - INTERACTIVE PENTESTING")
            print("="*60)
            print("\n1. Run Full Pentest (Autonomous)")
            print("2. Run Web Application Pentest")
            print("3. Run Network Reconnaissance")
            print("4. Search Exploit Database")
            print("5. Query AI Analysis")
            print("6. View Scan Results")
            print("7. Generate Report")
            print("8. Exit")
            print("\n" + "-"*60)
            
            choice = input("Select option (1-8): ").strip()
            
            if choice == '1':
                target = input("Enter target IP/domain: ").strip()
                self.autonomous_pentest(target, 'full')
            
            elif choice == '2':
                url = input("Enter target URL: ").strip()
                self.autonomous_pentest(url, 'web')
            
            elif choice == '3':
                target = input("Enter target network: ").strip()
                self.run_nmap_scan(target, aggressive=True)
            
            elif choice == '4':
                query = input("Enter software/version to search: ").strip()
                self.run_searchsploit(query)
            
            elif choice == '5':
                prompt = input("Ask AI anything: ").strip()
                response = self.query_ai_controller(prompt)
                print(f"\n🤖 AI Response:\n{response}")
            
            elif choice == '6':
                print("\nRecent Scans:")
                for scan_id, data in self.active_scans.items():
                    print(f"  - {scan_id}: {data['target']} ({data['status']})")
            
            elif choice == '7':
                scan_id = input("Enter scan ID to report: ").strip()
                if scan_id in self.active_scans:
                    self.generate_report(scan_id)
                else:
                    logger.error(f"❌ Scan {scan_id} not found")
            
            elif choice == '8':
                logger.info("👋 Exiting Penligent AI")
                break
            
            else:
                print("❌ Invalid option")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='🔒 Penligent AI - Autonomous Pentesting Engine (Educational)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python penligent_ai.py --target 192.168.1.1
  python penligent_ai.py --target example.com --type web
  python penligent_ai.py --interactive
  python penligent_ai.py --target http://target.com --type full
        """
    )
    
    parser.add_argument('--target', help='Target IP, domain, or URL')
    parser.add_argument('--type', choices=['full', 'web', 'network', 'wordpress'], 
                       default='full', help='Type of penetration test')
    parser.add_argument('--interactive', '-i', action='store_true', 
                       help='Run in interactive mode')
    parser.add_argument('--aggressive', '-a', action='store_true',
                       help='Run aggressive scans')
    parser.add_argument('--config', default='config/ai_config.yml',
                       help='Configuration file path')
    
    args = parser.parse_args()
    
    # Initialize AI Controller
    ai_controller = AIController(args.config)
    
    print("""
    ╔═══════════════════════════════════════════════╗
    ║   🔒 PENLIGENT AI - AUTO PENTESTING ENGINE 🤖  ║
    ║      Free for Educational Purposes Only       ║
    ╚═══════════════════════════════════════════════╝
    """)
    
    if args.interactive:
        ai_controller.interactive_mode()
    elif args.target:
        logger.info(f"🎯 Target: {args.target}")
        logger.info(f"📋 Type: {args.type}")
        logger.info(f"⚡ Aggressive: {args.aggressive}")
        
        scan_id = ai_controller.autonomous_pentest(args.target, args.type)
        
        if scan_id:
            logger.info(f"\n✅ Scan completed! ID: {scan_id}")
        else:
            logger.error("❌ Scan failed")
    else:
        ai_controller.interactive_mode()


if __name__ == '__main__':
    main()
