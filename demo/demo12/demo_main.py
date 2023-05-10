import time
import sys
from PyQt5.QtCore import QThread, pyqtSignal
from untitled import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 创建一个工作线程，并将其信号连接到updateLabel方法
        self.thread = Worker()
        self.thread.sig.connect(self.updateLabel)

        # #连接按钮点击信号到buttonClicked方法
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        # #点击按钮时启动工作线程
        self.thread.start()

    def updateLabel(self, text):
        # #用提供的文本更新标签文本
        self.label.setText(text)


class Worker(QThread):
    # 定义一个自定义的PyQtSignal，它接受一个字符串参数
    sig = pyqtSignal(str)

    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super(Worker, self).__init__(parent)
        self.count = 0

    def run(self):
        # #运行工作线程直到外部停止
        while True:
            # #暂停一秒钟
            time.sleep(1)

            # #增加计数值
            self.count += 1

            # #发出自定义信号每五秒与当前计数值
            if (self.count % 5 == 0):
                self.sig.emit(f"已执行{self.count}秒")
