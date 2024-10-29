#Muhammad Farhan
#T202320308

from PyQt5.QtWidgets import QDesktopWidget, QMainWindow,QWidget,QApplication, QPushButton, QLabel
from PyQt5 import QtCore
class MyWindow(QMainWindow):
     def __init__(self):
        super(). __init__()
        self.label = QLabel(self)
        self.label.setText("myLabel")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("belajar pyqt5")
        cwa = self.frameGeometry()
        cwc = QDesktopWidget().availableGeometry().center()
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(500,500)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint,False)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False)
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
        