import os
import time
from PackageAcitivity import GetPackageName
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


class WorkerDebugAppMain(QThread):
    DebugInfo = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        infolist = self.queue.get()
        path = infolist.split("&")[0]
        devices_info = infolist.split("&")[1]
        file = open(r"D:\Test_ToolS\.debug.on", "w+")
        if '/' in path:
            time.sleep(1)
            package_name = GetPackageName(path)
            debugfile = os.popen( f'adb -s {devices_info} push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()
            self.DebugInfo.emit(debugfile)

        else:
            time.sleep(1)
            debugfile = os.popen(f'adb -s {devices_info} push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{path}/cache/.debug.on').read()
            self.DebugInfo.emit(debugfile)
