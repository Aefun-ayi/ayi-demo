from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from App_Out_Ad import Out_Ad
from time import sleep
import os


class Worker_Ash_Pross(QThread):
    log = pyqtSignal(str)
    lock_img_path = pyqtSignal(str)
    unlock_img_path = pyqtSignal(str)
    unlock_ad_path = pyqtSignal(str)
    charge_img_path = pyqtSignal(str)
    charge_ad_path = pyqtSignal(str)
    wifi_img_path = pyqtSignal(str)
    wifi_ad_path = pyqtSignal(str)
    home_img_path = pyqtSignal(str)
    home_ad_path = pyqtSignal(str)
    timing_img_path = pyqtSignal(str)
    timing_ad_path = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue



    def run(self):
        path = self.queue.get()
        driver_info = Out_Ad(path).connect_phone()
        self.d = Out_Ad(path)
        self.log.emit("自动化启动，本次自动化操作:启动app-->强停置灰app进程-->待进程拉起后-->触发锁屏新闻-->解锁后弹窗-->插拔电弹窗-->wifi切换弹窗-->home键弹窗-->定时弹窗")
        self.log.emit(f"手机设备信息-->品牌：{driver_info['brand']}，系统版本：{driver_info['version']}，型号：{driver_info['model']}")
        self.d.start_app()
        self.log.emit('正在启动app：'+self.d.appinfo())
        sleep(5)
        self.log.emit('开始执行强停操作')
        for i in range(8):
            sleep(1)
            self.d.stop_app()
            self.log.emit(f'使用adb命令执行强停操作{i+1}次')
        if self.d.proess_info():
            self.log.emit('强停8次后，进程存活，重新执行强停置灰操作')
            for ii in range(8):
                sleep(1)
                self.d.stop_app()
                self.log.emit(f'使用adb命令执行强停操作{ii+9}次')
                if self.d.proess_info():
                    self.log.emit('强停16次后，进程存活，通知超哥')
                else:
                    self.log.emit('进程已成功杀死，等待进程重新拉起...')
        else:
            self.log.emit('进程已成功杀死，等待进程重新拉起...')
        sleep(3)
        wait_time = 0
        for wait in range(45):
            wait_time += 20
            sleep(20)
            self.log.emit(f'已等待进程重启拉活：{wait_time}秒')
            if self.d.proess_info():
                self.log.emit('进程已成功拉起，开始执行应外弹窗触发操作')
                break
            else:
                self.log.emit(f'进程尚未拉起，继续等待')
                continue
        if self.d.proess_info():
            first_lock = self.d.lock_news()
            if '锁屏新闻展示成功' in first_lock:
                sleep(3)
                self.log.emit(f'首次锁屏新闻展示成功，已截图保存至{first_lock}，查看有无信息流广告')
                self.lock_img_path.emit(first_lock)
            else:
                self.log.emit('首次锁屏新闻触发失败，尝试二次触发')
                double_lock = self.d.lock_news()
                sleep(3)
                if '锁屏新闻展示成功' in double_lock:
                    self.log.emit(f'二次锁屏新闻展示成功，已截图保存至{double_lock}，查看有无信息流广告')
                    self.lock_img_path.emit(double_lock)
                else:
                    self.log.emit(f'二次{double_lock}，查看进程是否已挂掉')