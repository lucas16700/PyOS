from PyQt6.QtWidgets import *
import sys
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import *

class janela_main(QMainWindow):
    def  __init__(self, nome):
        super(janela_main, self).__init__()
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        QApplication.setApplicationName(nome)
        
app = QApplication(sys.argv)
window=janela_main("browser brabo")
app.exec()