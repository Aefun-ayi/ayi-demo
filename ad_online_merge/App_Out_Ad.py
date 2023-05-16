import os
import uiautomator2 as u2
from Package_Acitivity import get_package_name, get_activity_name
from time import sleep
import datetime


class Out_Ad():
    def __init__(self, path):
        self.package = get_package_name(path)
        self.activity = get_activity_name(path)
        # print(self.package)
        self.filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')

    def connect_phone(self):
        self.dirver = u2.connect()
        return self.dirver.device_info

    def start_app(self):
        self.dirver = u2.connect()
        self.dirver.app_start(self.package, self.activity)

    def stop_app(self):
        self.dirver = u2.connect()
        self.dirver.app_stop(self.package)

    def img_dir(self):
        path = r'D:/keep/自动化截图存储'
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return path
        else:
            return path

    def lock_news(self):
        # self.img_dir()
        self.dirver.screen_off()
        sleep(2)
        self.dirver.screen_on()
        self.dirver.swipe_points([(0.485, 0.708), (0.481, 0.286)], 0.05)
        if self.dirver(text='推荐').wait(timeout=5.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}/{self.filetime}-锁屏新闻展示成功.jpg")
            return path
            # print('锁屏新闻展示成功')
        else:
            info = '锁屏新闻触发失败'
            print('锁屏新闻触发失败')
            return info

    def unlock_dig(self):
        self.dirver.swipe_points([(0.2, 0.5), (0.8, 0.5)], 0.5)
        if self.dirver(text='手机卫士').wait(timeout=5.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}/{self.filetime}-解锁后弹窗展示成功.jpg")
            print('解锁后弹窗展示成功')
            return path
        else:
            info = '解锁后弹窗展示失败'
            print('解锁后弹窗展示失败')
            return info

    def charge_dig(self):
        os.popen('adb shell dumpsys battery set status 2')  # 模拟充电状态
        sleep(1)
        os.popen('adb shell dumpsys battery set status 1')  # 模拟断电状态
        os.popen('adb shell dumpsys battery reset')  # 恢复电池原本状态
        if self.dirver(text='手机卫士').wait(timeout=5.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}\{self.filetime}-插拔电弹窗展示成功.jpg")
            print('插拔电弹窗展示成功')
            return path
        else:
            info = '插拔电弹窗展示失败'
            print('插拔电弹窗展示失败')
            return info

    def wifi_switch(self):
        os.popen('adb shell svc wifi disable')  # 控制wifi开关-关
        sleep(1)
        os.popen('adb shell svc wifi enable')  # 控制wifi开关-开
        if self.dirver(text='手机卫士').wait(timeout=5.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}\{self.filetime}-wifi切换弹窗展示成功.jpg")
            print('wifi切换弹窗展示成功')
            return path
        else:
            info = 'wifi切换弹窗弹窗展示失败'
            print('wifi切换弹窗展示失败')
            return info

    def home_dig(self):
        self.dirver.press("home")
        if self.dirver(text='手机卫士').wait(timeout=5.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}\{self.filetime}-home键弹窗展示成功.jpg")
            print('home键弹窗展示成功')
            return path
        else:
            info = 'home键弹窗弹窗展示失败'
            print('home键弹窗展示失败')
            return info

    def timming_dig(self):
        if self.dirver(text='手机卫士').wait(timeout=600.0):
            path = self.dirver.screenshot(fr"{self.img_dir()}\{self.filetime}-定时弹窗展示成功.jpg")
            print('定时弹窗展示成功')
            return path
        else:
            info = '定时弹窗展示失败'
            print('定时弹窗展示失败')
            return info

    def ad_dig(self):
        if self.dirver(text='正在进行优化').wait_gone(timeout=20):
            if self.dirver(text='反馈').wait(timeout=15.0) or self.dirver(text='跳过').wait(timeout=15.0):
                path = self.dirver.screenshot(fr"{self.img_dir()}\{self.filetime}-广告展示成功.jpg")
                print('广告展示成功')
                # 点击关闭
                sleep(30)
                self.dirver.click(0.891, 0.041)
                self.dirver.click(0.886, 0.074)
                self.dirver.press('back')
                self.dirver.press('home')
                self.dirver.press('back')
                return path
            else:
                info = '广告展示失败'
                print('广告展示失败')
                self.dirver.press('back')
                self.dirver.press('home')
                self.dirver.press('back')
                return info



# if __name__ == '__main__':
#     a = Out_Ad(
#         r"E:\csgj\createApk_1.4.4\createApk\outFloder\38726014_cn.kandroidzpz.ppctsfun_1.0.51_xmtxzn_20230515.apk")
    # a.img_dir()
    # a.connect_phone()
    # print(a.connect_phone())
    # a.lock_news()

    # a.start_app()
    # print(a.img_dir())
