from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


class WorkerLookHome(QThread):
    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        info = self.queue.get()
        img = Image.open(info)
        img.show()