#Muhammad Farhan
#T202320308

from PyQt5.QtWidgets import  QGridLayout, QMainWindow, QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super ().__init__()
        layout = QGridLayout()
        btn1 = QPushButton("btn baris 0 kolm 0")
        btn2 = QPushButton("btn baris 0 kolm 1")
        btn3 = QPushButton("btn baris 1 kolm 0")
        btn4 = QPushButton("btn baris 1 kolm 1")
        layout.addWidget(btn1,0,0)
        layout.addWidget(btn2,0,1)
        layout.addWidget(btn3,1,0)
        layout.addWidget(btn4,1,1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication ([])
window = MyWindow()
window.show()
app.exec_()