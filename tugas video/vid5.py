#Muhammad Farhan
#T202320308

from PyQt5.QtWidgets import  QFormLayout, QMainWindow, QWidget, QApplication, QLineEdit,QPushButton, QLabel
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super ().__init__()
        layout = QFormLayout()
        layout.addRow("Nama",QLineEdit())
        layout.addRow("Email",QLineEdit())
        label = QLabel("Alamat")
        Qedit = QLineEdit()
        layout.addRow(label,Qedit)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication ([])
window = MyWindow()
window.show()
app.exec_()