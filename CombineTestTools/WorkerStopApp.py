import os
from PackageAcitivity import GetPackageName
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


class WorkerStopAppMain(QThread):

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        infolist = self.queue.get()
        path = infolist.split("&")[0]
        devices_info = infolist.split("&")[1]
        if '/' in path:
            package_name = GetPackageName(path)
            os.popen(f'adb -s {devices_info} shell am force-stop {package_name}')
        else:
            os.popen(f'adb -s {devices_info} shell am force-stop {path}')