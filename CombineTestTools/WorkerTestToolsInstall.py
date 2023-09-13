import os
import time
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PackageAcitivity import GetPackageName



class WorkerTestToolsInstallMain(QThread):
    InstallInfo = pyqtSignal(str)
    PutFile = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        infolist = self.queue.get()
        path = infolist.split("&")[0]
        demo = infolist.split("&")[1]
        devices_info = infolist.split("&")[2]
        package_name = GetPackageName(path)
        if '小米' in demo:
            xm = os.popen(f'adb -s {devices_info} install -i com.xiaomi.market {path}')  # 模拟小米商店安装
            self.InstallInfo.emit(str(xm.read()))
        elif '华为' in demo:
            hw = os.popen(f'adb -s {devices_info}  install -i com.huawei.appmarket {path}')  # 模拟华为商店安装
            self.InstallInfo.emit(str(hw.read()))
        elif 'vivo' in demo:
            vi = os.popen(f'adb -s {devices_info}  install -i com.bbk.appstore {path}')  # 模拟vivo商店安装
            self.InstallInfo.emit(str(vi.read()))
        elif 'oppo' in demo:
            op = os.popen(f'adb -s {devices_info}  install -i com.heytap.market {path}')  # 模拟oppo商店安装
            self.InstallInfo.emit(str(op.read()))
        elif '正常安装' in demo:
            anzhaung = os.popen(f'adb -s {devices_info} install -r {path}')  # 正常强制安装
            self.InstallInfo.emit(str(anzhaung))
        elif 'debug安装' in demo:
            file = open(r"D:\Test_ToolS\.debug.on", "w+")
            install = os.popen(fr'adb -s {devices_info} install {path}')  # 调用终端使用adb命令正常安装
            time.sleep(1)
            de = os.popen(f'adb -s {devices_info} push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()  # 将debug文件自动传输至包名文件夹内
            self.InstallInfo.emit(str(install.read()))
            self.PutFile.emit(str(de))