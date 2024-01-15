import datetime
import os
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PackageAcitivity import GetPackageName
import subprocess



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
            android_version = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.build.version.release'],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
            result = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.product.brand'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            result1 = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.product.model'],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            version = android_version.stdout.decode('utf-8').strip()
            model = result.stdout.decode('utf-8').strip()
            model1 = result1.stdout.decode('utf-8').strip()
            rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
            if package_name in progress:
                self.ProcessInfo.emit(rtime + f'   设备信息：{model} {model1} 安卓版本:【{version}】/{devices_info}\n' + progress)
            else:
                self.ProcessInfo.emit(rtime + f'   设备信息：{model} {model1} 安卓版本:【{version}】/{devices_info}\n无进程信息\n')
        else:
            progress = os.popen(f'adb -s {devices_info} shell ps|findstr {path}').read()
            android_version = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.build.version.release'],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
            result = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.product.brand'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            result1 = subprocess.run(['adb', '-s', devices_info, 'shell', 'getprop', 'ro.product.model'],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            version = android_version.stdout.decode('utf-8').strip()
            model = result.stdout.decode('utf-8').strip()
            model1 = result1.stdout.decode('utf-8').strip()
            rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
            if path in progress:
                self.ProcessInfo.emit(rtime + f'   设备信息：{model} {model1} 安卓版本:【{version}】/{devices_info}\n' + progress)
            else:
                self.ProcessInfo.emit(rtime + f'   设备信息：{model} {model1} 安卓版本:【{version}】/{devices_info}\n无进程信息\n')
