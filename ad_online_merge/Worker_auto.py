from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import os
from App_Out_Ad import Out_Ad
from time import sleep


class Worker_Auto(QThread):
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
        self.log.emit("自动化启动，本次自动化操作触发：锁屏新闻，解锁后弹窗，插拔电弹窗，wifi切换弹窗，home键弹窗，定时弹窗")
        self.log.emit(f"手机设备信息-->品牌：{driver_info['brand']}，系统版本：{driver_info['version']}，型号：{driver_info['model']}")
        self.d.start_app()
        sleep(5)
        self.d.stop_app()
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
        unlock = self.d.unlock_dig()
        if '解锁后弹窗展示成功' in unlock:
            self.log.emit(f'解锁后弹窗展示成功，已截图保存至{unlock}')
            self.unlock_img_path.emit(unlock)
            unlock_ad = self.d.ad_dig()
            if '广告展示成功' in unlock_ad:
                self.log.emit(f'解锁后弹窗广告展示成功，已截图保存至{unlock_ad}')
                self.unlock_ad_path.emit(unlock_ad)
            else:
                self.log.emit(f'解锁后弹窗{unlock_ad}，请手动排查失败原因')
        else:
            self.log.emit(unlock)
        sleep(3)
        charge = self.d.charge_dig()
        if '插拔电弹窗展示成功' in charge:
            self.log.emit(f'插拔电弹窗展示成功，已截图保存至{charge}')
            self.charge_img_path.emit(charge)
            charge_ad = self.d.ad_dig()
            if '广告展示成功' in charge_ad:
                self.log.emit(f'插拔电弹窗广告展示成功，已截图保存至{charge_ad}')
                self.charge_ad_path.emit(charge_ad)
            else:
                self.log.emit(f'插拔电弹窗{charge_ad}，请手动排查失败原因')
        else:
            self.log.emit(charge)
        sleep(3)
        wifi = self.d.wifi_switch()
        if 'wifi切换弹窗展示成功' in wifi:
            self.log.emit(f'wifi弹窗展示成功，已截图保存至{wifi}')
            self.wifi_img_path.emit(wifi)
            wifi_ad = self.d.ad_dig()
            if '广告展示成功' in wifi_ad:
                self.log.emit(f'wifi弹窗广告展示成功，已截图保存至{wifi_ad}')
                self.wifi_ad_path.emit(wifi_ad)
            else:
                self.log.emit(f'wifi弹窗{wifi_ad}，请手动排查失败原因')
        else:
            self.log.emit(wifi)
        sleep(3)
        home = self.d.home_dig()
        if 'home键弹窗展示成功' in home:
            self.log.emit(f'home弹窗展示成功，已截图保存至{home}')
            self.home_img_path.emit(home)
            home_ad = self.d.ad_dig()
            if '广告展示成功' in home_ad:
                self.log.emit(f'home弹窗广告展示成功，已截图保存至{home_ad}')
                self.home_ad_path.emit(home_ad)
            else:
                self.log.emit(f'home弹窗{home_ad}，请手动排查失败原因')
        else:
            self.log.emit(home)
        sleep(3)
        self.log.emit('开始等待定时弹窗触发...')
        timming = self.d.timming_dig()

        if '定时弹窗展示成功' in timming:
            self.log.emit(f'定时弹窗展示成功，已截图保存至{timming}')
            self.timing_img_path.emit(timming)
            timming_ad = self.d.ad_dig()
            if '广告展示成功' in timming_ad:
                self.log.emit(f'定时弹窗广告展示成功，已截图保存至{timming_ad}')
                self.timing_ad_path.emit(timming_ad)
            else:
                self.log.emit(f'定时弹窗{timming_ad}，请手动排查失败原因')
        else:
            self.log.emit(timming)