#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
import qdarkstyle

'''
这只是模仿进度条--其实并没有真的达到进度条功能
很耗时的程序，将到99%停住，直到工作进程结束，但是不至于卡死
耗时几天终于把基本思路搞了，暂时只能一个线程，而且不是很懂
接下来就打算继续------
疑问：每用一次线程就得重新写一个线程类？这样太麻烦了把，有没有办法直接调用现在的线程类，直接改run函数中的工作函数呢
'''


def work1():
    # 超级耗时的工作函数，比如抓包1000多条数据
    # 模拟耗时
    for i in range(5000000):
        print(i)


# 主窗口
class main_w(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.te = QPushButton("进度条", self)
        self.layout1 = QHBoxLayout()
        self.setLayout(self.layout1)
        self.layout1.addWidget(self.te)
        self.te.clicked.connect(self.show1)

    def show1(self):
        self.w2 = Bar()
        self.w2.show()


class WorkThread(QThread):
    # 实例化一个信号对象
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        # 将你工作的函数放到这里来
        # 例如
        work1()
        # 循环完毕后发出信号
        self.trigger.emit()


class Bar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.timer = QBasicTimer()
        self.btn = QPushButton('正在处理，请等待----', self)
        self.btn.move(40, 80)
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        self.setFixedSize(500, 50)
        self.main_layout.addWidget(self.pbar, 1, 0)
        self.main_layout.addWidget(self.btn, 1, 1)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.btn.clicked.connect(self.close)
        self.work()
        self.step = 0

    def timerEvent(self, e):
        if self.step >= 99:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def work(self):
        self.btn.setEnabled(False)  # 不可按
        self.timer.start(100, self)
        self.work_thread = WorkThread()
        self.work_thread.start()
        self.work_thread.trigger.connect(self.stopend)

    def stopend(self):
        if self.step != 99:
            self.temp = 100 - self.step
            while (self.temp):
                self.step = 1 + self.step
                self.pbar.setValue(self.step)
                self.temp -= 1
        else:
            self.step += 1
            self.pbar.setValue(self.step)
        time.sleep(1)
        self.btn.setText('完成')
        self.btn.setEnabled(True)  # 可按
        # self.close()#想要让进度条结束后自己消失


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # qss模板
    ex = main_w()  # 如果想要进度条直接跑---ex = Bar()
    # ex = Bar()
    ex.show()
    sys.exit(app.exec_())