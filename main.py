# C:\Users\User\AppData\Roaming\Python\Python311\Scripts\pyqt6-tools.exe designer
from calc_logic import MyWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('css_style.txt', 'r') as f:
        app.setStyleSheet(f.read())

    window = MyWindow()
    window.show()
    sys.exit(app.exec())

