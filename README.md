# Penligent-AI-Free

🔒 **Advanced AI-Powered Pentesting Suite with GUI & Kali Integration** — Free for Educational Purposes Only

A modern, open-source pentesting framework powered by AI and a user-friendly GUI. The AI acts as an intelligent controller orchestrating Kali Linux pentesting tools, automating reconnaissance, vulnerability assessment, exploitation, and security analysis with minimal user intervention.

---

## 🎯 Vision

Penligent AI transforms pentesting through intelligent automation:
- **AI-as-Controller**: Artificial intelligence intelligently manages and orchestrates all pentesting tools
- **GUI-Driven Interface**: Intuitive graphical interface controlled by the GUI layer, which communicates with the AI engine
- **Kali Tool Integration**: Full integration with all major Kali Linux pentesting tools and frameworks
- **Automated Workflows**: End-to-end automation from reconnaissance to reporting
- **Intelligent Decision Making**: AI analyzes scan results in real-time and suggests next steps
- **Educational Focus**: Learn security concepts with guided analysis and explanations

### Architecture Flow
```
User → GUI Interface → AI Controller → Kali Pentesting Tools → Results → AI Analysis → GUI Display
```

---

## ⚠️ Disclaimer

**For Educational Purposes Only** — This tool is designed for authorized security testing on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal. The authors are not responsible for any misuse or damage caused by this tool.

---

## 🚀 Key Features

### Phase 1: GUI & AI Controller Infrastructure
- [x] GUI Desktop Application (PyQt5/Tkinter based)
- [x] AI Controller Engine (LLM-based orchestration)
- [x] Tool management and routing system
- [x] Real-time command execution and monitoring
- [x] Local SQLite database for scan history

### Phase 2: Kali Tool Integration
- [ ] **Reconnaissance Tools**
  - Nmap integration (network scanning)
  - Shodan API integration
  - Whois/DNS enumeration
  - Google dorking automation
  
- [ ] **Network Analysis**
  - Wireshark integration
  - tcpdump automation
  - Burp Suite integration
  
- [ ] **Vulnerability Scanning**
  - OpenVAS integration
  - Nikto web scanning
  - SQLmap for SQL injection
  - WPScan for WordPress
  
- [ ] **Exploitation Tools**
  - Metasploit framework integration
  - ExifTool for metadata extraction
  - HashCat for password cracking
  
- [ ] **Credential Testing**
  - Hydra integration
  - Medusa integration
  - Ncrack integration

### Phase 3: AI-Driven Features
- [ ] Intelligent tool selection based on target analysis
- [ ] Automated report generation with remediation suggestions
- [ ] Real-time findings interpretation
- [ ] Vulnerability prioritization and risk scoring
- [ ] AI-assisted exploit selection and execution

### Phase 4: Advanced Features
- [ ] Multi-threaded scanning
- [ ] Distributed agent support
- [ ] Custom plugin system
- [ ] REST API server
- [ ] Advanced Web Dashboard
- [ ] Custom payload generation
- [ ] Social engineering automation

---

## 📋 Architecture

```
penligent-ai-free/
├── src/
│   ├── gui/                  # GUI Interface (PyQt5/Tkinter)
│   │   ├── main_window.py    # Main GUI window
│   │   ├── dashboard.py      # Dashboard/status display
│   │   ├── tool_selector.py  # Tool selection interface
│   │   ├── results_viewer.py # Results display
│   │   └── settings.py       # Configuration GUI
│   │
│   ├── ai/                   # AI Controller Engine
│   │   ├── controller.py     # Main AI controller
│   │   ├── llm_engine.py     # LLM integration (OpenAI/Local)
│   │   ├── decision_maker.py # Intelligent decision making
│   │   ├── analyzer.py       # Results analysis
│   │   └── prompt_templates.py # AI prompts
│   │
│   ├── kali_tools/           # Kali Tool Integration
│   │   ├── base_tool.py      # Base tool wrapper
│   │   ├── recon/            # Reconnaissance tools
│   │   │   ├── nmap.py
│   │   │   ├── shodan.py
│   │   │   └── dns_enum.py
│   │   ├── scanning/         # Vulnerability scanning
│   │   │   ├── openvas.py
│   │   │   ├── nikto.py
│   │   │   ├── sqlmap.py
│   │   │   └── wpscan.py
│   │   ├── exploitation/     # Exploitation tools
│   │   │   ├── metasploit.py
│   │   │   ├── hashcat.py
│   │   │   └── exiftool.py
│   │   ├── credential/       # Credential testing
│   │   │   ├── hydra.py
│   │   │   ├── medusa.py
│   │   │   └── ncrack.py
│   │   └── analysis/         # Analysis tools
���   │       ├── burp_suite.py
│   │       ├── wireshark.py
│   │       └── tcpdump.py
│   │
│   ├── core/                 # Core Engine
│   │   ├── orchestrator.py   # Tool orchestration
│   │   ├── command_executor.py # Command execution
│   │   ├── result_parser.py  # Result parsing
│   │   └── workflow.py       # Workflow automation
│   │
│   ├── database/             # Database Layer
│   │   ├── models.py         # Data models
│   │   ├── repository.py     # Data access
│   │   └── migrations/       # DB migrations
│   │
│   ├── utils/                # Utilities
│   │   ├── logger.py
│   │   ├── config_manager.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   └── config/               # Configuration
│       ├── settings.yml
│       ├── kali_tools_config.yml
│       └── ai_config.yml
│
├── tests/                    # Test Suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── docs/                     # Documentation
│   ├── getting-started.md
│   ├── installation.md
│   ├── gui-guide.md
│   ├── ai-controller.md
│   ├── kali-integration.md
│   └── workflow-automation.md
│
├── examples/                 # Example Scripts
│   ├── basic_scan.py
│   ├── web_penetration.py
│   └── network_recon.py
│
├── requirements.txt          # Python Dependencies
├── requirements-kali.txt     # Kali Tool Requirements
├── setup.py
├── main.py                   # Application Entry Point
└── README.md
```

---

## 🛠️ Tech Stack

### Core Technologies
- **Language**: Python 3.10+
- **GUI Framework**: PyQt5 / PyQtGraph (modern UI with graphs)
- **Alternative GUI**: Tkinter (lightweight option)
- **AI/LLM**: OpenAI API / LangChain / LLaMA / Ollama
- **Database**: SQLite (local) / PostgreSQL (production)

### Pentesting & Security Tools
- **Network Scanning**: Nmap, Masscan
- **Vulnerability Assessment**: OpenVAS, Nikto, Trivy
- **Web Testing**: Burp Suite API, OWASP ZAP, SQLMap, WPScan
- **Exploitation**: Metasploit Framework, SearchSploit
- **Credential Testing**: Hydra, Medusa, Ncrack, HashCat
- **Metadata Analysis**: ExifTool
- **Network Analysis**: Wireshark, tcpdump, Scapy
- **Encoding/Decoding**: CyberChef API integration

### Additional Libraries
- **Task Queue**: Celery (for distributed scanning)
- **Web API**: FastAPI (REST endpoints)
- **Process Management**: Subprocess, asyncio
- **Data Processing**: Pandas, NumPy
- **Reporting**: ReportLab, FPDF

---

## 📦 Installation & Requirements

### System Requirements
- **OS**: Linux (Kali Linux recommended) / Ubuntu / Debian
- **Python**: 3.10 or higher
- **RAM**: Minimum 8GB (16GB recommended)
- **Disk Space**: 10GB minimum
- **CPU**: Multi-core processor

### Prerequisites & Dependencies

#### Python Dependencies
```bash
# Core framework
flask==3.0.0
fastapi==0.104.0
uvicorn==0.24.0
pydantic==2.0.0

# GUI
PyQt5==5.15.9
PyQtGraph==0.13.3
matplotlib==3.8.0
seaborn==0.13.0

# AI/LLM Integration
openai==1.3.0
langchain==0.1.0
transformers==4.35.0
ollama==0.1.0
lxml==4.9.3
beautifulsoup4==4.12.2

# Database
sqlalchemy==2.0.23
psycopg2-binary==2.9.9

# Security & Cryptography
cryptography==41.0.7
paramiko==3.4.0
requests==2.31.0

# Data Processing
pandas==2.1.3
numpy==1.26.2
networkx==3.2.1

# Task Automation
celery==5.3.4
redis==5.0.1

# Utilities
python-dotenv==1.0.0
pyyaml==6.0.1
click==8.1.7
typer==0.9.0
tqdm==4.66.1
loguru==0.7.2

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
```

#### Kali Linux Tools (Required)
```bash
# Reconnaissance
nmap
masscan
whois
dnsutils (dig, nslookup)
curl
wget

# Vulnerability Scanning
nikto
wpscan
sqlmap
openvas-scanner

# Exploitation & Post-Exploitation
metasploit-framework
searchsploit
exiftool
hashcat
aircrack-ng

# Credential Testing
hydra
medusa
ncrack
john
rockyou

# Network Analysis
wireshark
tcpdump
tshark
scapy
netcat

# Web Application Testing
burp-suite (community)
zaproxy
dirb
gobuster

# Encoding/Decoding
xxd
base64
hexdump
```

#### Optional Tools
```bash
# Advanced Exploitation
beef-xss
responder
impacket
bloodhound

# OSINT
maltego
shodan-cli
theHarvester

# Password Cracking
hashcat
john-the-ripper
crunch

# Wireless
aircrack-ng
kismet
wifite2
```

### Installation Steps

#### 1. Clone Repository
```bash
git clone https://github.com/zubair123-hub/Penligent-AI-Free-.git
cd Penligent-AI-Free-
```

#### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-kali.txt
```

#### 4. Install Kali Tools (on Kali Linux)
```bash
# Update package lists
sudo apt update

# Install tools from package list
sudo apt install -y nmap nikto sqlmap wpscan metasploit-framework \
  hydra medusa ncrack wireshark tcpdump exiftool hashcat aircrack-ng

# Alternative: Use the included installation script
sudo bash install-kali-tools.sh
```

#### 5. Configure AI Engine
```bash
# Copy configuration template
cp config/ai_config.yml.template config/ai_config.yml

# Edit with your API keys (OpenAI, Shodan, etc.)
nano config/ai_config.yml
```

#### 6. Initialize Database
```bash
python -m penligent_ai init-db
```

#### 7. Verify Installation
```bash
python main.py --version
python main.py gui  # Start GUI
```

---

## 🎮 Quick Start Guide

### GUI Mode (Recommended)
```bash
# Start the GUI application
python main.py gui

# Or directly
python main.py
```

### Command-Line Mode
```bash
# Initialize a new pentesting project
penligent init --project "MyTest" --target 192.168.1.0/24

# Run AI-guided reconnaissance
penligent scan recon --target example.com --aggressive

# Analyze results with AI
penligent analyze --project "MyTest"

# Generate comprehensive report
penligent report --project "MyTest" --format pdf --include-remediation

# Interactive AI mode
penligent interactive
```

### Workflow Examples

#### Example 1: Web Application Testing
```bash
penligent workflow run web-pentesting \
  --target http://target.com \
  --ai-mode aggressive \
  --include-tools "nikto,sqlmap,wpscan,burp"
```

#### Example 2: Network Reconnaissance
```bash
penligent workflow run network-recon \
  --target 192.168.1.0/24 \
  --ai-mode smart \
  --depth full
```

#### Example 3: Full Penetration Test
```bash
penligent workflow run full-pentest \
  --target target.com \
  --scope external \
  --reporting enabled
```

---

## 🤖 AI Controller Features

The AI acts as an intelligent orchestrator:

1. **Tool Selection**: Automatically selects appropriate Kali tools based on target analysis
2. **Workflow Optimization**: Determines the optimal sequence of tool execution
3. **Result Interpretation**: Analyzes findings and identifies vulnerabilities
4. **Risk Prioritization**: Ranks vulnerabilities by severity and impact
5. **Exploit Recommendation**: Suggests relevant exploits from Metasploit
6. **Adaptive Execution**: Adjusts strategy based on intermediate results
7. **Report Generation**: Creates professional penetration test reports with remediation

---

## 📚 Documentation

Comprehensive guides available in `/docs`:
- [Getting Started](docs/getting-started.md)
- [Installation & Setup](docs/installation.md)
- [GUI User Guide](docs/gui-guide.md)
- [AI Controller Documentation](docs/ai-controller.md)
- [Kali Tools Integration](docs/kali-integration.md)
- [Workflow Automation](docs/workflow-automation.md)
- [API Reference](docs/api-reference.md)
- [Configuration Guide](docs/configuration.md)
- [Plugin Development](docs/plugin-development.md)

---

## 🔌 API Integration Examples

### REST API
```bash
# Start API server
penligent api-server --port 8000

# API Examples
curl -X POST http://localhost:8000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "full"}'

curl http://localhost:8000/api/results/<scan_id>
```

### Python SDK
```python
from penligent_ai import PenligentAI

ai = PenligentAI(api_key="your-api-key")

# Start scan
scan = ai.start_scan(
    target="example.com",
    scan_type="web-pentesting",
    ai_mode="aggressive"
)

# Get results
results = ai.get_results(scan.id)
print(results.summary())
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

Licensed under Apache License 2.0 — see [LICENSE](LICENSE) file for details.

**Note**: Use this tool responsibly and legally. Always obtain written authorization before conducting penetration tests. The authors are not responsible for misuse.

---

## 📞 Support & Feedback

- **Issues**: Report bugs on [GitHub Issues](https://github.com/zubair123-hub/Penligent-AI-Free-/issues)
- **Discussions**: Share ideas on [GitHub Discussions](https://github.com/zubair123-hub/Penligent-AI-Free-/discussions)
- **Wiki**: Community knowledge base on [GitHub Wiki](https://github.com/zubair123-hub/Penligent-AI-Free-/wiki)
- **Email**: penligent-ai@example.com

---

## 📖 Educational Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [PentesterLab](https://pentesterlab.com/)
- [eLearnSecurity](https://elearnsecurity.com/)
- [Kali Linux Documentation](https://www.kali.org/docs/)

---

## 🌟 Roadmap

| Phase | Timeline | Deliverables |
|-------|----------|--------------|
| **Phase 1** | Q3 2026 | GUI framework, AI controller foundation, basic Kali integration |
| **Phase 2** | Q4 2026 | Full Kali tool integration, LLM enhancement, workflow automation |
| **Phase 3** | Q1 2027 | Web dashboard, REST API, advanced reporting |
| **Phase 4** | Q2 2027 | Plugin system, distributed agents, enterprise features |

---

## 🔐 Security Notice

- This tool requires root/admin privileges for some operations
- Run on isolated networks or in virtualized environments
- Never use on systems without explicit authorization
- Keep Kali tools and database updated regularly
- Review all generated reports before sharing

---

## 🎓 Disclaimer & Legal

**Unauthorized Access is Illegal**

The Penligent-AI-Free project is intended for authorized security testing, educational purposes, and by authorized security professionals only. Users are responsible for:

- Obtaining written authorization before testing any systems
- Complying with all applicable laws and regulations
- Using the tool ethically and responsibly
- Not accessing systems without explicit permission

The authors assume no liability for misuse, unauthorized access, damage, or legal consequences.

---

**Remember**: *With great power comes great responsibility. Use this tool wisely and ethically.*

**Last Updated**: July 2026  
**Maintained by**: Penligent-AI Community
