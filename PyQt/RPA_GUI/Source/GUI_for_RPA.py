import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set Quit button
        btn = QPushButton('Quit', self)
        btn.move(350, 400)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
    
        self.setWindowTitle('GUI for RPA')
        self.setWindowIcon(QIcon('..\Image\Apple.png'))
        self.setGeometry(400, 200, 500, 500)
        self.show()
        


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())