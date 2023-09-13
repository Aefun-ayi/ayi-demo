import datetime
import os
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PackageAcitivity import GetPackageName


class WorkerCheckProcessMain(QThread):
    ProcessInfo = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        info = self.queue.get()
        path = info.split("&")[0]
        devices_info = info.split("&")[-1]
        if '/' in path:
            package_name = GetPackageName(path)
            progress = os.popen(f'adb -s {devices_info} shell ps|findstr {package_name}').read()
            rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
            if package_name in progress:
                self.ProcessInfo.emit(rtime + '\n' + progress)
            else:
                self.ProcessInfo.emit(rtime + '\n无进程信息\n')
        else:
            progress = os.popen(f'adb -s {devices_info} shell ps|findstr {path}').read()
            rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
            if path in progress:
                self.ProcessInfo.emit(rtime + '\n' + progress)
            else:
                self.ProcessInfo.emit(rtime + '\n无进程信息\n')
