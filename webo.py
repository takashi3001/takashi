import sys
import os
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QTabWidget, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Digite o URL ou termo de pesquisa...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)

        self.add_new_tab()

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            background-color: #1e1e1e;
            color: #f0f0f0;
            QLineEdit { padding: 5px; }
        """)
        self.setWindowTitle('webo.py - Navegador da Web')
        self.setGeometry(100, 100, 1200, 800)

        # Atalho para fechar a aba atual (Ctrl + W)
        self.shortcut_ctrl_w = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut_ctrl_w.activated.connect(self.close_current_tab)

        # Atalho para abrir uma nova aba (Ctrl + T)
        self.shortcut_ctrl_t = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcut_ctrl_t.activated.connect(self.add_new_tab)

        # Atalho para recarregar a página atual (F5)
        self.shortcut_f5 = QShortcut(QKeySequence(Qt.Key_F5), self)
        self.shortcut_f5.activated.connect(self.reload_page)

        # Atalho para voltar para a página anterior (F6)
        self.shortcut_f6 = QShortcut(QKeySequence(Qt.Key_F6), self)
        self.shortcut_f6.activated.connect(self.go_back)

        # Atalho para avançar para a próxima página (F8)
        self.shortcut_f8 = QShortcut(QKeySequence(Qt.Key_F8), self)
        self.shortcut_f8.activated.connect(self.go_forward)

        # Atalho para ir para a página inicial (F10)
        self.shortcut_f10 = QShortcut(QKeySequence(Qt.Key_F10), self)
        self.shortcut_f10.activated.connect(self.go_home)

        self.show()

    def add_new_tab(self, qurl=QUrl('https://www.google.com'), label="Nova Aba"):
        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

    def close_current_tab(self):
        i = self.tabs.currentIndex()
        self.tabs.removeTab(i)

    def navigate_to_url(self):
        input_url = self.url_bar.text()
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl(input_url))

    def reload_page(self):
        current_tab = self.tabs.currentWidget()
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
        self.url_bar.setText(current_tab.url().toString())

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)
        else:
            self.close()

if __name__ == '__main__':
    os.environ['QTWEBENGINE_DISABLE_SANDBOX'] = '1'
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # Ativa o suporte para DPI alto antes de criar a instância da aplicação
    app.setStyle('Fusion')
    browser = WebBrowser()
    sys.exit(app.exec_())

