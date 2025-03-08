# C:\Users\User\AppData\Roaming\Python\Python311\Scripts\pyqt6-tools.exe designer
from PyQt6 import QtCore, QtGui, QtWidgets
from calc import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())