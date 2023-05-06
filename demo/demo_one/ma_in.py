import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
import untitled

def click():
    ui.textBrowser.append('测试使用1')
    ui.textBrowser_2.append('测试使用2')


if __name__ == '__main__':
    # 初始化数据
    # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 设置默认数据
    # ui.textBrowser_2.setText('123123')
    # ui.textBrowser.setText('456456')
    ui.pushButton.clicked.connect(click)
    # 事件监听
	# 。。。。。
    sys.exit(app.exec_())
