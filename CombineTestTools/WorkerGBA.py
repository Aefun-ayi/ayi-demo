from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import MD5_encrypt
import datetime
import os


class WorkerGBAMain(QThread):
    DevicesInfo = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        devices_info = self.queue.get()
        rtime = datetime.datetime.now().strftime('%Y%m%d')
        input_string = f"loveChina{rtime[2:]}6"
        encrypted_result = MD5_encrypt.md5_encrypt(input_string)
        GBA_main = os.system(f"adb -s {devices_info} shell setprop log.tag.LOG_TAG {encrypted_result}")
