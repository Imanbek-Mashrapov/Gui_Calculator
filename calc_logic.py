import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "calculator_design.ui")
        uic.loadUi(ui_path, self)






