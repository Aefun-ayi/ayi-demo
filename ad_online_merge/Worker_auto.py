from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import os




class Worker_Auto(QThread):
    log = pyqtSignal(str)
    sig2 = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        path = self.queue.get()
