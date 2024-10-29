#Muhammad Farhan
#T202320308

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super (). __init__()
        layout=QHBoxLayout()
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")
        layout.addWidget(btn1, 1, Qt.AlignTop)
        layout.addWidget(btn2, 2, Qt.AlignBottom)
        layout.addWidget(btn3, 2, Qt.AlignCenter)
        layout.addWidget(btn4, 2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication ([])
window = MyWindow()
window.show()
app.exec_()