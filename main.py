from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    homePage  = 'https://google.com'
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.layout()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)

        # browser navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        prev_btn = QAction('>>', self)
        prev_btn.triggered.connect(self.browser.forward)
        navbar.addAction(prev_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
    def navigate_home(self):
        self.browser.setUrl(QUrl(self.homePage))

        

app = QApplication(sys.argv)
QApplication.setApplicationName('Brosify')
window = MainWindow()

app.exec()

