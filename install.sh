#!/bin/bash

################################################################################
#                                                                              #
#  🔒 PENLIGENT AI - AUTO INSTALLATION & SETUP SCRIPT                        #
#  Automated setup for Kali Linux - Educational Purposes Only                 #
#                                                                              #
################################################################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

clear_screen() {
    clear
}

print_header() {
    echo ""
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                                                                ║"
    echo "║  🔒 PENLIGENT AI - AUTONOMOUS PENTESTING PLATFORM 🤖          ║"
    echo "║                                                                ║"
    echo "║      Auto Installation & Setup for Kali Linux                 ║"
    echo "║      Educational Purposes Only                                ║"
    echo "║                                                                ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
}

check_root() {
    if [[ $EUID -ne 0 ]]; then
        log_warning "This script should be run as root for optimal installation"
        log_info "Attempting to continue with sudo..."
    fi
}

check_kali_linux() {
    if [ ! -f /etc/os-release ]; then
        log_error "Cannot determine OS"
        exit 1
    fi
    
    source /etc/os-release
    if [[ "$ID" != "kali" && "$PRETTY_NAME" != *"Kali"* ]]; then
        log_warning "Not running on Kali Linux. Some tools may not be available."
        log_info "Continuing installation anyway..."
    else
        log_success "Detected Kali Linux"
    fi
}

update_system() {
    log_info "Updating system packages..."
    sudo apt update
    sudo apt upgrade -y
    log_success "System packages updated"
}

install_python_dependencies() {
    log_info "Installing Python 3.10+ (if needed)..."
    
    if ! command -v python3.10 &> /dev/null && ! command -v python3.11 &> /dev/null && ! command -v python3.12 &> /dev/null; then
        sudo apt install -y python3 python3-pip python3-venv python3-dev
        log_success "Python 3 installed"
    else
        log_success "Python 3 already installed"
    fi
    
    # Install pip
    sudo apt install -y python3-pip
    sudo pip3 install --upgrade pip setuptools wheel
    log_success "Python dependencies installed"
}

install_kali_tools() {
    log_info "Installing essential Kali pentesting tools..."
    
    TOOLS=(
        # Core tools
        "nmap"
        "masscan"
        "curl"
        "wget"
        "netcat-openbsd"
        
        # Web testing
        "nikto"
        "wpscan"
        "sqlmap"
        "dirb"
        "gobuster"
        
        # Exploitation
        "metasploit-framework"
        "searchsploit"
        "exploitdb"
        
        # Network analysis
        "wireshark"
        "tcpdump"
        "tshark"
        
        # Credential testing
        "hydra"
        "medusa"
        "ncrack"
        "hashcat"
        "john"
        
        # OSINT
        "whois"
        "dnsutils"
        "git"
        
        # Utilities
        "vim"
        "nano"
        "curl"
        "jq"
        "tmux"
    )
    
    for tool in "${TOOLS[@]}"; do
        if ! command -v "$tool" &> /dev/null; then
            log_info "Installing $tool..."
            sudo apt install -y "$tool" 2>/dev/null || log_warning "Failed to install $tool"
        else
            log_success "$tool already installed"
        fi
    done
}

install_python_packages() {
    log_info "Installing Python packages from requirements.txt..."
    
    if [ -f "requirements.txt" ]; then
        python3 -m pip install --upgrade pip
        python3 -m pip install -r requirements.txt
        log_success "Python packages installed"
    else
        log_error "requirements.txt not found"
        return 1
    fi
}

install_optional_tools() {
    log_info "Installing optional advanced tools..."
    
    OPTIONAL_TOOLS=(
        "burp-suite-community"
        "zaproxy"
        "beef-xss"
        "responder"
        "impacket"
        "aircrack-ng"
        "kismet"
        "wireshark"
    )
    
    for tool in "${OPTIONAL_TOOLS[@]}"; do
        read -p "Install $tool? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            sudo apt install -y "$tool" 2>/dev/null || log_warning "Could not install $tool"
        fi
    done
}

install_local_llm() {
    log_info "Setting up local AI model (Ollama)..."
    
    if ! command -v ollama &> /dev/null; then
        log_info "Downloading and installing Ollama..."
        curl -fsSL https://ollama.ai/install.sh | sh
        log_success "Ollama installed"
        
        log_info "Pulling LLaMA 2 model (this may take a few minutes)..."
        ollama pull llama2 &
        OLLAMA_PID=$!
        log_info "Model download started in background (PID: $OLLAMA_PID)"
    else
        log_success "Ollama already installed"
    fi
}

create_directories() {
    log_info "Creating application directories..."
    
    mkdir -p config
    mkdir -p reports
    mkdir -p logs
    mkdir -p data
    mkdir -p src
    mkdir -p tests
    
    log_success "Directories created"
}

setup_configuration() {
    log_info "Setting up configuration files..."
    
    if [ ! -f "config/ai_config.yml" ]; then
        log_info "Configuration file not found, copying template..."
        # Config will be created if not exists
    else
        log_success "Configuration file exists"
    fi
}

create_venv() {
    log_info "Creating Python virtual environment..."
    
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        log_success "Virtual environment created"
    else
        log_success "Virtual environment already exists"
    fi
    
    log_info "Activating virtual environment..."
    source venv/bin/activate
    log_success "Virtual environment activated"
}

verify_installation() {
    log_info "Verifying installation..."
    
    FAILED=0
    
    # Check Python
    if python3 --version &> /dev/null; then
        log_success "Python 3: $(python3 --version)"
    else
        log_error "Python 3 not found"
        FAILED=$((FAILED+1))
    fi
    
    # Check nmap
    if command -v nmap &> /dev/null; then
        log_success "Nmap: installed"
    else
        log_error "Nmap not found"
        FAILED=$((FAILED+1))
    fi
    
    # Check required Python packages
    python3 -c "import PyQt5" 2>/dev/null && log_success "PyQt5: installed" || log_warning "PyQt5: not found"
    python3 -c "import yaml" 2>/dev/null && log_success "PyYAML: installed" || log_warning "PyYAML: not found"
    
    if [ $FAILED -gt 0 ]; then
        log_warning "$FAILED essential components missing"
        return 1
    else
        log_success "Installation verification complete"
        return 0
    fi
}

setup_permissions() {
    log_info "Setting up file permissions..."
    
    chmod +x penligent_ai.sh 2>/dev/null || true
    chmod +x src/penligent_ai.py 2>/dev/null || true
    chmod +x src/gui_interface.py 2>/dev/null || true
    
    log_success "Permissions set"
}

create_launch_scripts() {
    log_info "Creating launch scripts..."
    
    # GUI launcher
    cat > launch_gui.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python3 src/gui_interface.py
EOF
    chmod +x launch_gui.sh
    
    # CLI launcher
    cat > launch_cli.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python3 src/penligent_ai.py "$@"
EOF
    chmod +x launch_cli.sh
    
    log_success "Launch scripts created"
}

create_database() {
    log_info "Initializing database..."
    
    python3 << 'EOF'
import sqlite3
import os

db_path = "data/penligent.db"
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        id TEXT PRIMARY KEY,
        target TEXT,
        scan_type TEXT,
        start_time TIMESTAMP,
        end_time TIMESTAMP,
        status TEXT,
        results TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vulnerabilities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_id TEXT,
        severity TEXT,
        title TEXT,
        description TEXT,
        recommendation TEXT,
        FOREIGN KEY(scan_id) REFERENCES scans(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS findings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_id TEXT,
        type TEXT,
        data TEXT,
        FOREIGN KEY(scan_id) REFERENCES scans(id)
    )
''')

conn.commit()
conn.close()

print("Database initialized successfully!")
EOF
    
    log_success "Database initialized"
}

main() {
    clear_screen
    print_header
    
    log_info "Starting Penligent AI installation..."
    echo ""
    
    check_root
    check_kali_linux
    
    log_info "Installation will proceed in the following order:"
    echo "  1. Update system packages"
    echo "  2. Install Python dependencies"
    echo "  3. Install Kali pentesting tools"
    echo "  4. Install Python packages"
    echo "  5. Optional: Install additional tools"
    echo "  6. Optional: Install local AI (Ollama)"
    echo "  7. Create directories and configuration"
    echo "  8. Setup Python virtual environment"
    echo "  9. Create launch scripts"
    echo "  10. Initialize database"
    echo "  11. Verify installation"
    echo ""
    
    read -p "Continue? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Installation cancelled"
        exit 1
    fi
    
    echo ""
    log_info "Beginning installation process..."
    echo ""
    
    # Run installation steps
    update_system
    install_python_dependencies
    install_kali_tools
    create_venv
    install_python_packages
    
    read -p "Install optional tools? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_optional_tools
    fi
    
    read -p "Install local AI model (Ollama)? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_local_llm
    fi
    
    create_directories
    setup_configuration
    setup_permissions
    create_launch_scripts
    create_database
    verify_installation
    
    echo ""
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                                                                ║"
    echo "║  ✅ INSTALLATION COMPLETE!                                    ║"
    echo "║                                                                ║"
    echo "║  To start Penligent AI:                                        ║"
    echo "║                                                                ║"
    echo "║  GUI Mode:                                                     ║"
    echo "║    ./launch_gui.sh                                             ║"
    echo "║                                                                ║"
    echo "║  CLI Mode:                                                     ║"
    echo "║    ./launch_cli.sh --target <target> --type full              ║"
    echo "║                                                                ║"
    echo "║  Interactive Mode:                                             ║"
    echo "║    ./launch_cli.sh --interactive                              ║"
    echo "║                                                                ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    
    log_success "Penligent AI is ready to use!"
}

# Run main function
main
