import sys
import os
import asyncio
import aiohttp
import ssl
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QFileDialog, QLineEdit, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from colorama import Fore, Style, init

init(autoreset=True)

# --- Directory Scanner Logic in Thread ---
class ScannerThread(QThread):
    log_signal = pyqtSignal(str)
    done_signal = pyqtSignal()

    def __init__(self, url, wordlist_path, extensions):
        super().__init__()
        self.url = url.rstrip('/')
        self.wordlist_path = wordlist_path
        self.extensions = extensions
        self.found_urls = []
        self.forbidden_urls = []
        self.stop_flag = False

    def get_random_headers(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Googlebot/2.1 (+http://www.google.com/bot.html)",
        ]
        headers = {
            "User-Agent": random.choice(user_agents),
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
        }
        return headers

    def load_wordlist(self):
        if not os.path.exists(self.wordlist_path):
            self.log_signal.emit(f"{Fore.RED}❌ File not found: {self.wordlist_path}{Style.RESET_ALL}")
            return []
        with open(self.wordlist_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]

    async def check_directory(self, session, url):
        if self.stop_flag:
            return
        try:
            async with session.get(url, headers=self.get_random_headers()) as resp:
                if resp.status == 200:
                    self.log_signal.emit(f"{Fore.GREEN}✅ [200] FOUND: {url}{Style.RESET_ALL}")
                    self.found_urls.append(url)
                elif resp.status == 403:
                    self.log_signal.emit(f"{Fore.YELLOW}🔒 [403] FORBIDDEN: {url}{Style.RESET_ALL}")
                    self.forbidden_urls.append(url)
                elif resp.status == 404:
                    self.log_signal.emit(f"{Fore.RED}❌ [404] NOT FOUND: {url}{Style.RESET_ALL}")
        except Exception as e:
            self.log_signal.emit(f"{Fore.RED}⚠️ Error: {e}{Style.RESET_ALL}")

    async def scan(self):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        wordlist = self.load_wordlist()
        if not wordlist:
            return

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            tasks = []
            for word in wordlist:
                for ext in self.extensions:
                    full_url = f"{self.url}/{word}{ext}"
                    tasks.append(self.check_directory(session, full_url))
            await asyncio.gather(*tasks)

        self.log_signal.emit("\n--- Scan Summary ---")
        self.log_signal.emit(f"{Fore.GREEN}✅ Found ({len(self.found_urls)}):{Style.RESET_ALL}")
        for u in self.found_urls:
            self.log_signal.emit(f"{Fore.GREEN}- {u}{Style.RESET_ALL}")
        self.log_signal.emit(f"{Fore.YELLOW}🔒 Forbidden ({len(self.forbidden_urls)}):{Style.RESET_ALL}")
        for u in self.forbidden_urls:
            self.log_signal.emit(f"{Fore.YELLOW}- {u}{Style.RESET_ALL}")
        self.done_signal.emit()

    def run(self):
        asyncio.run(self.scan())

    def stop(self):
        self.stop_flag = True


# --- GUI Class ---
class ScannerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RedOpsScanner GUI - Directory Reconnaissance")
        self.setGeometry(300, 200, 800, 600)

        layout = QVBoxLayout()

        # Inputs
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter target URL (e.g., https://example.com)")
        self.wordlist_input = QLineEdit()
        self.wordlist_input.setPlaceholderText("Select wordlist file...")

        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_wordlist)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.wordlist_input)
        hlayout.addWidget(browse_btn)

        self.ext_input = QLineEdit(".php .html .js")
        self.ext_input.setPlaceholderText("Extensions (e.g., .php .html)")

        # Buttons
        self.scan_btn = QPushButton("Start Scan")
        self.scan_btn.clicked.connect(self.start_scan)
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.stop_scan)
        self.stop_btn.setEnabled(False)

        # Output area
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)

        layout.addWidget(QLabel("Target URL:"))
        layout.addWidget(self.url_input)
        layout.addWidget(QLabel("Wordlist File:"))
        layout.addLayout(hlayout)
        layout.addWidget(QLabel("Extensions (space-separated):"))
        layout.addWidget(self.ext_input)
        layout.addWidget(self.scan_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(QLabel("Scan Output:"))
        layout.addWidget(self.log_output)

        self.setLayout(layout)
        self.scanner_thread = None

    def browse_wordlist(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Wordlist File", "", "Text Files (*.txt)")
        if file:
            self.wordlist_input.setText(file)

    def start_scan(self):
        url = self.url_input.text().strip()
        wordlist_path = self.wordlist_input.text().strip()
        extensions = self.ext_input.text().strip().split()

        if not url or not wordlist_path:
            self.log_output.append("❌ Please enter URL and select wordlist.")
            return

        self.log_output.clear()
        self.scan_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

        self.scanner_thread = ScannerThread(url, wordlist_path, extensions)
        self.scanner_thread.log_signal.connect(self.append_log)
        self.scanner_thread.done_signal.connect(self.scan_finished)
        self.scanner_thread.start()

    def stop_scan(self):
        if self.scanner_thread:
            self.scanner_thread.stop()
            self.scan_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            self.append_log("🛑 Scan stopped manually.")

    def append_log(self, message):
        self.log_output.append(message)

    def scan_finished(self):
        self.scan_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.append_log("\n✅ Scan completed.")

# --- Main ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ScannerGUI()
    gui.show()
    sys.exit(app.exec_())
