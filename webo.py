import sys
import os
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QTabWidget, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search term...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
                color: #f0f0f0;
            }
            QLineEdit {
                padding: 5px;
                background-color: #2a2a2a;
                border: 1px solid #3a3a3a;
                color: #f0f0f0;
                selection-background-color: #444444;
                selection-color: #f0f0f0;
            }
            QLineEdit:focus {
                border: 2px solid #4a4a4a;
            }
            QTabWidget::pane {
                border: 0;
            }
            QTabBar::tab {
                background-color: #2a2a2a;
                color: #f0f0f0;
                padding: 8px;
                border: 1px solid #3a3a3a;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #1e1e1e;
                border-bottom: none;
            }
            QTabBar::tab:hover {
                background-color: #1e1e1e;
            }
        """)

        self.setWindowTitle('webo.py - Web Browser')
        self.setGeometry(100, 100, 1200, 800)

        self.create_shortcut("Ctrl+W", self.close_current_tab)
        self.create_shortcut("Ctrl+T", self.add_new_tab)
        self.create_shortcut("F5", self.reload_page)
        self.create_shortcut("F6", self.go_back)
        self.create_shortcut("F8", self.go_forward)
        self.create_shortcut("F10", self.go_home)

        os.environ['QTWEBENGINE_DISABLE_SANDBOX'] = '1'
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app.setStyle('Fusion')

        self.browser_settings = QWebEngineSettings.defaultSettings()
        self.browser_settings.setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
        self.browser_settings.setAttribute(QWebEngineSettings.WebGLEnabled, True)

        self.show()
        self.add_new_tab()

    def create_shortcut(self, key_sequence, action):
        shortcut = QShortcut(QKeySequence(key_sequence), self)
        shortcut.activated.connect(action)

    def add_new_tab(self, qurl=QUrl('https://www.google.com'), label="New Tab"):
        browser = QWebEngineView()
        browser.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)

        browser.load(qurl)
        self.tabs.addTab(browser, label)
        self.tabs.setCurrentWidget(browser)

    def close_current_tab(self):
        i = self.tabs.currentIndex()
        if i != -1:
            self.tabs.removeTab(i)

    def navigate_to_url(self):
        input_url = self.url_bar.text()
        if not input_url.startswith(('http://', 'https://')):
            input_url = 'http://' + input_url
            self.url_bar.setText(input_url)

        current_tab = self.tabs.currentWidget()
        current_tab.load(QUrl(input_url))

    def reload_page(self):
        current_tab = self.tabs.currentWidget()
        if current_tab.url().isValid():
            current_tab.reload()

    def go_back(self):
        current_tab = self.tabs.currentWidget()
        current_tab.back()

    def go_forward(self):
        current_tab = self.tabs.currentWidget()
        current_tab.forward()

    def go_home(self):
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl('https://www.google.com'))

    def update_url_bar(self, i):
        current_tab = self.tabs.widget(i)
        if current_tab:
            self.url_bar.setText(current_tab.url().toString())

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)
        else:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebBrowser()
    sys.exit(app.exec_())

