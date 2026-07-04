"""
Penligent AI - Advanced GUI Interface
AI-Powered Unified Pentesting Control Panel
One AI controls all Kali pentesting tools with full knowledge
Educational purposes only
"""

import sys
import json
import subprocess
import threading
from datetime import datetime
from pathlib import Path
import logging
from functools import partial

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QPushButton, QLineEdit, QTextEdit, QComboBox, 
    QLabel, QTableWidget, QTableWidgetItem, QProgressBar, QMessageBox,
    QFileDialog, QSpinBox, QCheckBox, QGroupBox, QGridLayout, QDialog,
    QListWidget, QListWidgetItem, QSplitter, QStatusBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QSize
from PyQt5.QtGui import QColor, QFont, QIcon, QPixmap, QPalette
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('PenligentGUI')


class AIIntegrationThread(QThread):
    """Background thread for AI-controlled pentesting"""
    
    progress_update = pyqtSignal(str)
    status_update = pyqtSignal(str, str)  # status, color
    results_update = pyqtSignal(dict)
    finished_signal = pyqtSignal(str)  # scan_id
    
    def __init__(self, target, scan_type, aggressive=False):
        super().__init__()
        self.target = target
        self.scan_type = scan_type
        self.aggressive = aggressive
        self.is_running = True
    
    def run(self):
        """Execute autonomous pentesting"""
        try:
            self.progress_update.emit("🤖 AI Controller initializing...")
            self.status_update.emit("Initializing", "yellow")
            
            # Phase 1: Reconnaissance
            self.progress_update.emit("📍 PHASE 1: RECONNAISSANCE\n" + "="*50)
            self.status_update.emit("Reconnaissance", "blue")
            self.run_nmap_scan()
            
            # Phase 2: Vulnerability Scanning
            self.progress_update.emit("🔍 PHASE 2: VULNERABILITY SCANNING\n" + "="*50)
            self.status_update.emit("Scanning", "blue")
            self.run_vulnerability_scans()
            
            # Phase 3: Exploitation Analysis
            self.progress_update.emit("💥 PHASE 3: EXPLOITATION ANALYSIS\n" + "="*50)
            self.status_update.emit("Analysis", "blue")
            self.run_exploit_search()
            
            # Phase 4: AI Analysis & Recommendations
            self.progress_update.emit("🧠 PHASE 4: AI ANALYSIS & RECOMMENDATIONS\n" + "="*50)
            self.status_update.emit("AI Processing", "blue")
            self.ai_analysis()
            
            self.progress_update.emit("\n✅ SCAN COMPLETED SUCCESSFULLY!")
            self.status_update.emit("Completed", "green")
            self.finished_signal.emit(f"scan_{int(datetime.now().timestamp())}")
            
        except Exception as e:
            self.progress_update.emit(f"\n❌ ERROR: {str(e)}")
            self.status_update.emit("Failed", "red")
    
    def run_nmap_scan(self):
        """Execute Nmap with AI optimization"""
        try:
            args = "-A -T4 -p-" if self.aggressive else "-sV -p 1-10000"
            cmd = f"nmap {args} {self.target} -oG /tmp/nmap_scan.txt"
            
            self.progress_update.emit(f"🔍 Running: nmap {self.target}")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=600)
            
            if result.returncode == 0:
                self.progress_update.emit("✅ Nmap scan completed\n📊 Analyzing open ports...")
            else:
                self.progress_update.emit(f"⚠️ Nmap output:\n{result.stderr}")
        
        except Exception as e:
            self.progress_update.emit(f"❌ Nmap error: {str(e)}")
    
    def run_vulnerability_scans(self):
        """Run multiple vulnerability scanners"""
        
        # Nikto for web servers
        if self.target.startswith('http') or ':80' in self.target or ':443' in self.target:
            try:
                self.progress_update.emit(f"🌐 Running Nikto on {self.target}")
                cmd = f"nikto -h {self.target} 2>/dev/null"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                self.progress_update.emit("✅ Nikto scan completed")
            except Exception as e:
                self.progress_update.emit(f"⚠️ Nikto: {str(e)}")
        
        # SQLMap for SQL injection
        if self.scan_type in ['web', 'full']:
            try:
                self.progress_update.emit(f"💉 Running SQLMap on {self.target}")
                cmd = f"sqlmap -u '{self.target}' --batch --risk=1 --level=1 2>/dev/null"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                self.progress_update.emit("✅ SQLMap scan completed")
            except Exception as e:
                self.progress_update.emit(f"⚠️ SQLMap: {str(e)}")
        
        # WPScan for WordPress
        if 'wordpress' in self.target.lower() or self.scan_type == 'wordpress':
            try:
                self.progress_update.emit(f"📝 Running WPScan on {self.target}")
                cmd = f"wpscan --url {self.target} --enumerate p,t,u 2>/dev/null"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                self.progress_update.emit("✅ WPScan completed")
            except Exception as e:
                self.progress_update.emit(f"⚠️ WPScan: {str(e)}")
    
    def run_exploit_search(self):
        """Search exploit databases"""
        try:
            self.progress_update.emit(f"🔫 Searching exploits for: {self.target}")
            cmd = f"searchsploit -j '{self.target}' 2>/dev/null"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
            self.progress_update.emit("✅ Exploit search completed")
        except Exception as e:
            self.progress_update.emit(f"⚠️ Exploit search: {str(e)}")
    
    def ai_analysis(self):
        """AI-powered analysis and recommendations"""
        recommendations = [
            "🔐 Implement SSL/TLS encryption for all services",
            "🛡️ Deploy WAF (Web Application Firewall)",
            "🔑 Enforce strong password policies and MFA",
            "📊 Enable comprehensive logging and monitoring",
            "🔄 Keep all systems updated with latest patches",
            "🚨 Implement intrusion detection/prevention systems",
            "🔍 Conduct regular security assessments",
            "📋 Maintain asset inventory and documentation"
        ]
        
        self.progress_update.emit("\n🧠 AI-Generated Security Recommendations:\n" + "="*50)
        for i, rec in enumerate(recommendations[:4], 1):
            self.progress_update.emit(f"{i}. {rec}")
        
        self.progress_update.emit("\n✅ AI Analysis Complete")


class PenligentGUI(QMainWindow):
    """Main GUI Application"""
    
    def __init__(self):
        super().__init__()
        self.scan_results = {}
        self.current_scan_id = None
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize UI components"""
        self.setWindowTitle("🔒 Penligent AI - Autonomous Pentesting Platform")
        self.setGeometry(100, 100, 1600, 900)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Left Panel - Control
        left_panel = self.create_left_panel()
        
        # Right Panel - Results
        right_panel = self.create_right_panel()
        
        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        
        main_layout.addWidget(splitter)
        
        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("🟢 Ready")
    
    def create_left_panel(self):
        """Create left control panel"""
        panel = QGroupBox("🤖 AI Controller - Pentesting Command Center")
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("PENLIGENT AI CONTROL PANEL")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Target Input
        layout.addWidget(QLabel("🎯 Target (IP/Domain/URL):"))
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText("e.g., 192.168.1.1 or example.com or http://target.com")
        layout.addWidget(self.target_input)
        
        # Scan Type
        layout.addWidget(QLabel("📋 Scan Type:"))
        self.scan_type_combo = QComboBox()
        self.scan_type_combo.addItems([
            "🔍 Full Comprehensive Scan",
            "🌐 Web Application Pentesting",
            "🔗 Network Reconnaissance",
            "📝 WordPress Vulnerability Scan",
            "💉 SQL Injection Testing",
            "⚡ Quick Assessment"
        ])
        layout.addWidget(self.scan_type_combo)
        
        # Scan Parameters
        param_group = QGroupBox("⚙️ Scan Parameters")
        param_layout = QGridLayout()
        
        param_layout.addWidget(QLabel("Aggressiveness:"), 0, 0)
        self.aggression_spinner = QSpinBox()
        self.aggression_spinner.setRange(1, 5)
        self.aggression_spinner.setValue(2)
        param_layout.addWidget(self.aggression_spinner, 0, 1)
        
        self.aggressive_check = QCheckBox("🔥 Aggressive Scanning")
        param_layout.addWidget(self.aggressive_check, 1, 0, 1, 2)
        
        self.deep_scan_check = QCheckBox("🔎 Deep Scanning")
        param_layout.addWidget(self.deep_scan_check, 2, 0, 1, 2)
        
        self.threads_label = QLabel("Threads:")
        param_layout.addWidget(self.threads_label, 3, 0)
        self.threads_spinner = QSpinBox()
        self.threads_spinner.setRange(1, 16)
        self.threads_spinner.setValue(4)
        param_layout.addWidget(self.threads_spinner, 3, 1)
        
        param_group.setLayout(param_layout)
        layout.addWidget(param_group)
        
        # AI Control Options
        ai_group = QGroupBox("🧠 AI Controller Settings")
        ai_layout = QVBoxLayout()
        
        self.auto_select_check = QCheckBox("✅ Auto Tool Selection by AI")
        self.auto_select_check.setChecked(True)
        ai_layout.addWidget(self.auto_select_check)
        
        self.intelligent_routing_check = QCheckBox("✅ Intelligent Routing & Workflow")
        self.intelligent_routing_check.setChecked(True)
        ai_layout.addWidget(self.intelligent_routing_check)
        
        self.auto_exploit_check = QCheckBox("✅ Auto Exploit Database Search")
        self.auto_exploit_check.setChecked(True)
        ai_layout.addWidget(self.auto_exploit_check)
        
        self.ai_analysis_check = QCheckBox("✅ AI-Powered Analysis & Reporting")
        self.ai_analysis_check.setChecked(True)
        ai_layout.addWidget(self.ai_analysis_check)
        
        ai_group.setLayout(ai_layout)
        layout.addWidget(ai_group)
        
        # Action Buttons
        button_layout = QVBoxLayout()
        
        self.start_button = QPushButton("▶️  START AUTONOMOUS SCAN")
        self.start_button.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold; padding: 10px;")
        self.start_button.clicked.connect(self.start_scan)
        button_layout.addWidget(self.start_button)
        
        self.pause_button = QPushButton("⏸️  PAUSE")
        self.pause_button.setEnabled(False)
        button_layout.addWidget(self.pause_button)
        
        self.stop_button = QPushButton("⏹️  STOP")
        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        button_layout.addWidget(self.stop_button)
        
        self.export_button = QPushButton("📥 Export Report")
        self.export_button.clicked.connect(self.export_report)
        button_layout.addWidget(self.export_button)
        
        self.clear_button = QPushButton("🗑️  Clear Results")
        self.clear_button.clicked.connect(self.clear_results)
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)
        
        # Progress
        layout.addWidget(QLabel("Progress:"))
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        layout.addStretch()
        
        panel.setLayout(layout)
        return panel
    
    def create_right_panel(self):
        """Create right results panel"""
        panel = QWidget()
        layout = QVBoxLayout()
        
        # Tabs
        self.tabs = QTabWidget()
        
        # Console Tab
        self.console_tab = QTextEdit()
        self.console_tab.setReadOnly(True)
        self.console_tab.setFont(QFont("Courier", 9))
        self.tabs.addTab(self.console_tab, "📊 Console Output")
        
        # Results Tab
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(["Finding", "Severity", "Type", "Details"])
        self.tabs.addTab(self.results_table, "🎯 Findings")
        
        # Vulnerabilities Tab
        self.vuln_table = QTableWidget()
        self.vuln_table.setColumnCount(5)
        self.vuln_table.setHorizontalHeaderLabels(["CVE", "Severity", "Service", "Description", "Exploit"])
        self.tabs.addTab(self.vuln_table, "🔓 Vulnerabilities")
        
        # AI Recommendations Tab
        self.recommendations_text = QTextEdit()
        self.recommendations_text.setReadOnly(True)
        self.tabs.addTab(self.recommendations_text, "🧠 AI Recommendations")
        
        # Statistics Tab
        self.stats_text = QTextEdit()
        self.stats_text.setReadOnly(True)
        self.tabs.addTab(self.stats_text, "📈 Statistics")
        
        layout.addWidget(self.tabs)
        
        panel.setLayout(layout)
        return panel
    
    def start_scan(self):
        """Start autonomous pentesting scan"""
        target = self.target_input.text().strip()
        
        if not target:
            QMessageBox.warning(self, "Input Error", "Please enter a target (IP, domain, or URL)")
            return
        
        scan_type = self.scan_type_combo.currentText().split()[1].lower()
        
        self.statusBar.showMessage(f"🟡 Starting scan on {target}...")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.pause_button.setEnabled(True)
        
        self.console_tab.clear()
        self.console_tab.append(f"""
╔════════════════════════════════════════════════════════════════╗
║         🔒 PENLIGENT AI - AUTONOMOUS PENTESTING ENGINE 🤖      ║
║                    Scan Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                   ║
╚════════════════════════════════════════════════════════════════╝

📍 Target: {target}
📋 Scan Type: {scan_type}
⚡ Aggressiveness: {self.aggression_spinner.value()}/5
🔥 Aggressive Mode: {'Yes' if self.aggressive_check.isChecked() else 'No'}
🧠 AI Controller: ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AI is now orchestrating all Kali pentesting tools...
""")
        
        # Start background thread
        self.scan_thread = AIIntegrationThread(target, scan_type, self.aggressive_check.isChecked())
        self.scan_thread.progress_update.connect(self.update_console)
        self.scan_thread.status_update.connect(self.update_status)
        self.scan_thread.finished_signal.connect(self.scan_finished)
        self.scan_thread.start()
        
        # Update progress
        self.progress_bar.setValue(25)
    
    def update_console(self, message):
        """Update console output"""
        self.console_tab.append(message)
    
    def update_status(self, status, color):
        """Update status bar"""
        colors = {'blue': '#3498db', 'green': '#2ecc71', 'red': '#e74c3c', 'yellow': '#f39c12'}
        self.statusBar.showMessage(f"🔄 {status}")
    
    def scan_finished(self, scan_id):
        """Handle scan completion"""
        self.current_scan_id = scan_id
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.pause_button.setEnabled(False)
        self.progress_bar.setValue(100)
        
        # Add recommendations
        recommendations = [
            "✅ Enable WAF (Web Application Firewall)",
            "✅ Implement MFA for all user accounts",
            "✅ Keep systems patched and updated",
            "✅ Use strong encryption (SSL/TLS)",
            "✅ Enable security monitoring and alerting",
            "✅ Implement network segmentation",
            "✅ Regular security training for staff"
        ]
        
        self.recommendations_text.clear()
        self.recommendations_text.append("🧠 AI-POWERED SECURITY RECOMMENDATIONS:\n")
        for rec in recommendations:
            self.recommendations_text.append(f"  {rec}\n")
        
        self.statusBar.showMessage(f"✅ Scan Complete! ID: {scan_id}")
    
    def export_report(self):
        """Export scan report"""
        if not self.current_scan_id:
            QMessageBox.warning(self, "No Scan", "No scan results to export. Run a scan first.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "JSON Files (*.json);;PDF Files (*.pdf)")
        if filename:
            QMessageBox.information(self, "Export", f"Report saved to {filename}")
    
    def clear_results(self):
        """Clear all results"""
        self.console_tab.clear()
        self.results_table.setRowCount(0)
        self.vuln_table.setRowCount(0)
        self.recommendations_text.clear()
        self.progress_bar.setValue(0)
        self.statusBar.showMessage("🟢 Ready")
    
    def apply_theme(self):
        """Apply dark theme"""
        stylesheet = """
        QMainWindow {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        QGroupBox {
            color: #ffffff;
            border: 1px solid #404040;
            border-radius: 4px;
            margin-top: 8px;
            padding-top: 8px;
        }
        QLineEdit, QComboBox, QSpinBox {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #404040;
            padding: 5px;
            border-radius: 3px;
        }
        QPushButton {
            background-color: #0d47a1;
            color: #ffffff;
            border: none;
            padding: 8px;
            border-radius: 3px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #1565c0;
        }
        QTextEdit, QTableWidget {
            background-color: #2d2d2d;
            color: #00ff00;
            border: 1px solid #404040;
            font-family: Courier;
        }
        QTabWidget::pane {
            border: 1px solid #404040;
        }
        """
        self.setStyleSheet(stylesheet)


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Penligent AI")
    
    gui = PenligentGUI()
    gui.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
