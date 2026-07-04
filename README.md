# Penligent AI - Complete Installation Guide

## 🔒 Penligent AI - Autonomous Pentesting Platform with King AI Chat

**Free for Educational Purposes Only**

A revolutionary AI-powered pentesting framework where one intelligent "King AI" understands natural human language and autonomously controls all Kali Linux pentesting tools. Communicate with the AI through a red & black themed chat interface and watch it execute complete penetration tests automatically.

---

## 📋 Quick Installation

### For Impatient Users - 3 Command Setup

```bash
# 1. Clone repository
git clone https://github.com/zubair123-hub/Penligent-AI-Free-.git && cd Penligent-AI-Free-

# 2. Run automatic installation (includes all tools)
sudo bash install.sh

# 3. Launch GUI with King AI Chat
./launch_gui.sh
```

**That's it!** You'll see the King AI chat interface ready to receive your commands.

---

## 🎮 King AI Chat Interface Features

### Red & Black Design Theme
- **Professional Security Aesthetic**: Red warning indicators, black background
- **Real-time Console**: Live pentesting tool output
- **Chat History**: Full conversation logs preserved
- **Status Indicators**: Visual feedback on AI actions

### One "King AI" Controls Everything
- **Natural Language Understanding**: Chat in English, AI understands hacking requests
- **Autonomous Execution**: AI selects tools, runs scans, analyzes results - no manual intervention
- **Real-time Response**: AI responds with findings and recommendations instantly
- **Context Aware**: AI remembers conversation history and previous scans

---

## 📦 Detailed Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/zubair123-hub/Penligent-AI-Free-.git
cd Penligent-AI-Free-
```

### Step 2: Automatic Installation Script

The `install.sh` script will automatically:

```bash
sudo bash install.sh
```

**Installation Process:**

1. ✅ **Update System** - Latest Kali packages
2. ✅ **Install Python 3.10+** - Required Python version
3. ✅ **Install Kali Tools** - All pentesting tools (30+):
   - Nmap, Nikto, SQLMap, WPScan
   - Metasploit Framework
   - Hydra, Medusa, Ncrack
   - Wireshark, tcpdump
   - And 20+ more tools
4. ✅ **Install Python Packages** - All dependencies from requirements.txt
5. ❓ **Optional Tools** - BeEF, Burp Suite, etc. (user choice)
6. ❓ **Local AI Model** - Ollama with LLaMA 2 (user choice)
7. ✅ **Create Virtual Environment** - Isolated Python environment
8. ✅ **Initialize Database** - SQLite for storing scans
9. ✅ **Create Launch Scripts** - Easy startup shortcuts
10. ✅ **Verify Installation** - Confirm all components working

**Installation takes 15-30 minutes depending on internet and system speed.**

### Step 3: Verify Installation

```bash
# Check Python
python3 --version

# Check Nmap
nmap --version

# Check key packages
python3 -c "import PyQt5; print('✅ PyQt5 installed')"
python3 -c "import yaml; print('✅ PyYAML installed')"
```

### Step 4: Start the Application

#### Option A: GUI with King AI Chat (Recommended)

```bash
./launch_gui.sh
```

#### Option B: CLI Interactive Mode

```bash
./launch_cli.sh --interactive
```

#### Option C: Direct Command

```bash
./launch_cli.sh --target 192.168.1.1 --type full --aggressive
```

---

## 💬 Chat with King AI - Examples

### The King AI Chat Interface

You'll see a split screen:
- **Left**: Chat with King AI
- **Right**: Real-time pentesting output in red & black theme

### Example Conversations

#### Example 1: Simple Network Scan

```
User: "Scan 192.168.1.0/24 for open ports and services"

King AI: 🤖 Starting network reconnaissance scan on 192.168.1.0/24
         Using Nmap with service detection...
         
[Output shows real-time Nmap scanning in console]

King AI: ✅ Scan complete! Found 5 active hosts:
         - 192.168.1.1: OpenSSH (port 22)
         - 192.168.1.50: Apache (port 80)
         - 192.168.1.100: MySQL (port 3306)
         
         Recommending: Vulnerability assessment next?
```

#### Example 2: Web Application Testing

```
User: "Test example.com for web vulnerabilities including SQL injection"

King AI: 🤖 Initializing web application penetration test on example.com
         Running: Nikto, SQLMap, WPScan in parallel...
         
[Real-time console shows all tools running]

King AI: ⚠️ VULNERABILITIES FOUND:
         1. SQL Injection in search parameter (HIGH)
         2. Outdated WordPress 4.9.1 (MEDIUM)
         3. Missing Security Headers (LOW)
         
         💡 Recommendations:
         - Apply input validation and parameterized queries
         - Update WordPress to latest version
         - Implement WAF (Web Application Firewall)
```

#### Example 3: Exploit Search

```
User: "What exploits are available for Apache 2.4.41?"

King AI: 🤖 Searching exploit databases for Apache 2.4.41...
         Found 12 relevant exploits:
         
         CRITICAL (CVSS 9.8):
         - CVE-2021-41773: Path Traversal RCE
         
         HIGH (CVSS 7.5):
         - CVE-2021-42013: Exploitation of path traversal
         
         ⚠️ Note: These are for educational/authorized testing only
```

#### Example 4: Aggressive Full Penetration Test

```
User: "Run a full aggressive penetration test on 10.0.0.50"

King AI: 🤖 Starting comprehensive penetration test with aggressive settings
         
         Phase 1: RECONNAISSANCE
         [Running Nmap aggressive scan...]
         Found: 8 open ports, 5 services
         
         Phase 2: VULNERABILITY SCANNING
         [Running Nikto on HTTP services...]
         [Running SQLMap on database ports...]
         Found: 7 vulnerabilities
         
         Phase 3: EXPLOITATION ANALYSIS
         [Searching Metasploit modules...]
         Found: 3 potential exploits
         
         Phase 4: AI ANALYSIS & RECOMMENDATIONS
         [AI processing results...]
         
King AI: ✅ TEST COMPLETE - SUMMARY:
         Critical: 2 vulnerabilities
         High: 3 vulnerabilities
         Medium: 2 vulnerabilities
         
         Risk Score: 8.5/10
         
         📊 Report generated: reports/penligent_report_timestamp.json
```

---

## 🎯 Chat Commands Reference

### Natural Language Examples

```
Scanning & Reconnaissance:
- "Scan 192.168.1.1"
- "Network reconnaissance on 10.0.0.0/8"
- "Port enumeration for target.com"
- "Service discovery on host"

Web Testing:
- "Test example.com for vulnerabilities"
- "SQL injection testing on target.com"
- "WordPress vulnerability scan"
- "Web application penetration test"

Exploit & Vulnerability:
- "Find exploits for Apache 2.4"
- "Search CVE database for PHP 7.2"
- "Available Metasploit modules for Windows"

Configuration:
- "Set threads to 8"
- "Aggressive mode enabled"
- "Change timeout to 600 seconds"
- "Save results to file"

Analysis & Reporting:
- "Analyze previous scan"
- "Generate security report"
- "Risk assessment"
- "Show recommendations"
```

---

## 🔴 Red & Black GUI Theme

### Interface Appearance

```
╔════════════════════════════════════════════════════════��═══════╗
║                    PENLIGENT AI - KING AI CHAT                 ║
║  [⬛ BLACK BACKGROUND WITH RED ACCENTS]                        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  LEFT PANEL (RED & BLACK):        RIGHT PANEL (RED TEXT):     ║
║  ┌──────────────────────────┐    ┌────────────────────────┐  ║
║  │ 🤖 King AI Chat          │    │ 🔴 PENLIGENT CONSOLE   │  ║
║  │                          │    │                        │  ║
║  │ User: "Scan 192.168..."  │    │ [RED] Nmap scanning... │  ║
║  │ ________________________  │    │ [RED] Found port 22    │  ║
║  │                          │    │ [RED] SSH service      │  ║
║  │ King AI: Starting scan.. │    │ [RED] Found port 80    │  ║
║  │ King AI: Found 5 ports   │    │ [RED] HTTP service     │  ║
║  │ King AI: Analyzing...    │    │ [RED] Scanning SQL... │  ║
║  │                          │    │ [RED] ✅ Complete      │  ║
║  │                          │    │                        │  ║
║  └──────────────────────────┘    └────────────────────────┘  ║
║                                                                ║
║  STATUS: 🟢 Ready | SCAN: 192.168.1.1 | FINDINGS: 3          ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 🛠️ What install.sh Installs

### System Tools (Kali Linux)

```
✅ Nmap               - Network scanning
✅ Nikto              - Web server scanning
✅ SQLMap             - SQL injection testing
✅ WPScan             - WordPress scanning
✅ Metasploit         - Exploitation framework
✅ Searchsploit       - Exploit database
✅ Hydra              - Credential brute force
✅ Medusa             - Password cracking
✅ Ncrack             - Network authentication cracker
✅ Hashcat            - GPU password cracking
✅ Wireshark          - Network packet analysis
✅ tcpdump            - Network traffic capture
✅ curl, wget         - Web utilities
✅ dnsutils           - DNS tools
✅ whois              - Domain information
... and 15+ more tools
```

### Python Packages

```
✅ PyQt5              - GUI framework
✅ pyyaml             - Configuration files
✅ requests           - HTTP library
✅ BeautifulSoup      - HTML parsing
✅ cryptography       - Encryption
✅ paramiko           - SSH client
✅ sqlalchemy         - Database ORM
✅ And 20+ more packages
```

---

## 📋 Troubleshooting

### Problem: "Command not found: nmap"

**Solution:**
```bash
# Re-run installation script
sudo bash install.sh

# Or manually install
sudo apt install nmap
```

### Problem: "PyQt5 import error"

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall PyQt5
pip install PyQt5 --force-reinstall
```

### Problem: "Permission denied: ./launch_gui.sh"

**Solution:**
```bash
chmod +x launch_gui.sh
chmod +x launch_cli.sh
./launch_gui.sh
```

### Problem: "AI model not found"

**Solution:**
```bash
# Install Ollama (optional, for local AI)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull LLaMA 2 model
ollama pull llama2
```

### Problem: Database errors

**Solution:**
```bash
# Reinitialize database
rm -f data/penligent.db
python3 << 'EOF'
import sqlite3
conn = sqlite3.connect('data/penligent.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS scans (id TEXT PRIMARY KEY, target TEXT)')
conn.commit()
print('Database initialized')
EOF
```

---

## 🔐 Security Notes

### Only Use On Authorized Systems
- ✅ Your own infrastructure
- ✅ Systems with written authorization
- ❌ Public systems
- ❌ Systems you don't own

### Best Practices
- Run in isolated/virtual environment
- Keep Kali tools updated
- Use strong authentication
- Review reports before sharing
- Log all pentesting activities

---

## 📊 System Requirements Check

```bash
# Verify requirements
python3 --version        # Should be 3.10+
nmap --version          # Should be installed
nikto -version          # Should be installed
python3 -c "import PyQt5; print('✅ GUI ready')"
```

---

## 🚀 Performance Tips

### Faster Scanning
```bash
# Increase threads
In GUI: Set Threads to 16 (default 4)

# CLI Mode
./launch_cli.sh --target 192.168.1.1 --threads 8
```

### Better Analysis
```
Aggressive Mode: For thorough testing
Deep Scanning: For complete vulnerability discovery
Multi-tool: Uses all relevant tools in parallel
```

---

## 📞 Getting Help

- **Bugs**: https://github.com/zubair123-hub/Penligent-AI-Free-/issues
- **Questions**: https://github.com/zubair123-hub/Penligent-AI-Free-/discussions
- **Documentation**: Check `/docs` directory

---

## 🎓 Next Steps

1. **Run First Scan**: Start with "Scan 192.168.1.1"
2. **Try Examples**: Use examples from chat commands
3. **Read Reports**: Check generated JSON reports
4. **Explore Features**: Experiment with different scan types
5. **Learn More**: Check OWASP and Kali documentation

---

## ✨ Summary

**Penligent AI** is now installed and ready to use!

```bash
# Start King AI Chat Interface
./launch_gui.sh

# Chat Examples:
# "Scan 192.168.1.0/24"
# "Test example.com for SQL injection"
# "Full penetration test on 10.0.0.50"
# "Search exploits for Apache 2.4"
```

**The King AI will:**
1. 🧠 Understand your request
2. 🔍 Select appropriate tools
3. ⚡ Execute automatically
4. 📊 Analyze results
5. 💬 Respond with findings

---

```
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║     🔒 Welcome to Penligent AI - Autonomous Pentesting 🤖     ║
║                                                                ║
║     One King AI. All Kali Tools. Complete Automation.          ║
║                                                                ║
║     Educational Purposes Only                                 ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

**Version**: 1.0  
**Last Updated**: July 2026  
**Maintained by**: Penligent AI Community
