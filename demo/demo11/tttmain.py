import untitled
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
import pandas as pd



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())