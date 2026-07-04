"""PyQt5-based GUI for Penligent AI"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QComboBox, QTextEdit, QTableWidget,
    QTableWidgetItem, QTabWidget, QProgressBar, QSpinBox, QCheckBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QColor
from ..core.config import Config
from ..core.scanner import Scanner


class ScannerThread(QThread):
    """Background thread for scanning"""
    progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, scanner, target, scan_type):
        super().__init__()
        self.scanner = scanner
        self.target = target
        self.scan_type = scan_type

    def run(self):
        try:
            self.progress.emit(f"Starting scan on {self.target}...")
            # Simulation - would call actual scanner
            self.progress.emit("Scan completed")
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))


class PenligentGUI(QMainWindow):
    """Main GUI window for Penligent AI"""

    def __init__(self):
        super().__init__()
        self.config = Config()
        self.scanner = Scanner(self.config)
        self.setup_ui()
        self.setWindowTitle("Penligent AI - Advanced Pentesting Suite")
        self.setGeometry(100, 100, 1200, 800)

    def setup_ui(self):
        """Setup the user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Create tabs
        tabs = QTabWidget()
        
        # Scan Tab
        scan_tab = self.create_scan_tab()
        tabs.addTab(scan_tab, "Scan")
        
        # Results Tab
        results_tab = self.create_results_tab()
        tabs.addTab(results_tab, "Results")
        
        # Analysis Tab
        analysis_tab = self.create_analysis_tab()
        tabs.addTab(analysis_tab, "AI Analysis")
        
        # Settings Tab
        settings_tab = self.create_settings_tab()
        tabs.addTab(settings_tab, "Settings")
        
        layout.addWidget(tabs)
        central_widget.setLayout(layout)

    def create_scan_tab(self) -> QWidget:
        """Create scanning interface tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Target input
        target_layout = QHBoxLayout()
        target_layout.addWidget(QLabel("Target:"))
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText("Enter IP address or hostname")
        target_layout.addWidget(self.target_input)
        layout.addLayout(target_layout)
        
        # Scan type
        scan_type_layout = QHBoxLayout()
        scan_type_layout.addWidget(QLabel("Scan Type:"))
        self.scan_type_combo = QComboBox()
        self.scan_type_combo.addItems(["Quick", "Standard", "Aggressive", "Full"])
        scan_type_layout.addWidget(self.scan_type_combo)
        layout.addLayout(scan_type_layout)
        
        # Options
        self.enable_ai_checkbox = QCheckBox("Enable AI Analysis")
        self.enable_ai_checkbox.setChecked(True)
        layout.addWidget(self.enable_ai_checkbox)
        
        self.enable_nmap_checkbox = QCheckBox("Use Nmap")
        self.enable_nmap_checkbox.setChecked(True)
        layout.addWidget(self.enable_nmap_checkbox)
        
        # Start button
        start_btn = QPushButton("Start Scan")
        start_btn.clicked.connect(self.start_scan)
        start_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        layout.addWidget(start_btn)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        
        # Status
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setPlaceholderText("Scan status will appear here...")
        layout.addWidget(self.status_text)
        
        widget.setLayout(layout)
        return widget

    def create_results_tab(self) -> QWidget:
        """Create results display tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(5)
        self.results_table.setHorizontalHeaderLabels(["Port", "Service", "State", "Version", "Vulnerability"])
        layout.addWidget(self.results_table)
        
        widget.setLayout(layout)
        return widget

    def create_analysis_tab(self) -> QWidget:
        """Create AI analysis tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("AI-Powered Vulnerability Analysis"))
        
        self.analysis_text = QTextEdit()
        self.analysis_text.setReadOnly(True)
        self.analysis_text.setPlaceholderText("AI analysis results will appear here...")
        layout.addWidget(self.analysis_text)
        
        analyze_btn = QPushButton("Generate AI Analysis")
        analyze_btn.clicked.connect(self.generate_analysis)
        layout.addWidget(analyze_btn)
        
        widget.setLayout(layout)
        return widget

    def create_settings_tab(self) -> QWidget:
        """Create settings tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # API Key
        api_layout = QHBoxLayout()
        api_layout.addWidget(QLabel("OpenAI API Key:"))
        self.api_key_input = QLineEdit()
        self.api_key_input.setEchoMode(QLineEdit.Password)
        api_layout.addWidget(self.api_key_input)
        layout.addLayout(api_layout)
        
        # LLM Provider
        provider_layout = QHBoxLayout()
        provider_layout.addWidget(QLabel("LLM Provider:"))
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(["OpenAI", "Local LLM", "Hugging Face"])
        provider_layout.addWidget(self.provider_combo)
        layout.addLayout(provider_layout)
        
        # Thread count
        threads_layout = QHBoxLayout()
        threads_layout.addWidget(QLabel("Max Threads:"))
        self.threads_spinbox = QSpinBox()
        self.threads_spinbox.setValue(10)
        self.threads_spinbox.setMinimum(1)
        self.threads_spinbox.setMaximum(100)
        threads_layout.addWidget(self.threads_spinbox)
        layout.addLayout(threads_layout)
        
        # Save settings button
        save_btn = QPushButton("Save Settings")
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def start_scan(self):
        """Start a new scan"""
        target = self.target_input.text()
        if not target:
            self.status_text.setText("Error: Please enter a target")
            return
        
        scan_type = self.scan_type_combo.currentText().lower()
        self.status_text.setText(f"Starting {scan_type} scan on {target}...")
        self.progress_bar.setValue(0)

    def generate_analysis(self):
        """Generate AI analysis of results"""
        self.analysis_text.setText("Generating AI-powered analysis...\n")
        # Would call AI analysis here
        self.analysis_text.append("Analysis complete!")

    def save_settings(self):
        """Save settings"""
        # Would save settings here
        pass


def run_gui():
    """Run the GUI application"""
    app = QApplication(sys.argv)
    window = PenligentGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_gui()
