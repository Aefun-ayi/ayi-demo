import untitled
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
import os
from PyQt5.QtWidgets import QMessageBox
def click():
    # QMessageBox.critical('cuow','tishi')
    a = ui.lineEdit.text()
    print(a)
    if a == '':

        msg = QMessageBox(QMessageBox.Critical,'cuowu','cuowu')
        msg.exec_()


if __name__ == '__main__':
    # 初始化数据
    # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click)
    sys.exit(app.exec_())