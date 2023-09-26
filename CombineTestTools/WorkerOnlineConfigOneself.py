from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from OnlineConfig import OnlineCfg


class WorkerOnlineConfigOneselfMain(QThread):

    OnlineCfgLog = pyqtSignal(str)

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def exception_handling(self, func):
        try:
            func()
        except Exception as e:
            return None

    def run(self):
        appInfo = self.queue.get()

        cha = appInfo.split("&")[1]
        pid = appInfo.split("&")[0]
        appid = pid[:-3]
        self.API = OnlineCfg(appid, cha, pid)

        if len(self.API.audit()) < 1 or self.API.audit()[0]['app_audit'] == 0:
            self.OnlineCfgLog.emit("审核关闭")
            if self.API.jh()['status']:
                if self.API.jh()['status'] == '1':
                    self.OnlineCfgLog.emit("V2锁屏开关：打开")
                    if self.API.jh()['lockSwitch'] == '1':
                        self.OnlineCfgLog.emit("锁屏新闻开关：打开")
                    elif self.API.jh()['lockSwitch'] == '0':
                        self.OnlineCfgLog.emit("锁屏新闻开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到锁屏新闻配置")

                    if self.API.jh()['unLockSwitch'] == '1':
                        self.OnlineCfgLog.emit("解锁后弹窗开关：打开")
                        self.OnlineCfgLog.emit(f"解锁后弹窗频次：{self.API.jh()['unLockInterval']}")
                    elif self.API.jh()['unLockSwitch'] == '0':
                        self.OnlineCfgLog.emit("解锁后弹窗开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到解锁后弹窗配置")

                    if self.API.jh()['homeSwitch'] == '1':
                        self.OnlineCfgLog.emit("home键弹窗开关：打开")
                        self.OnlineCfgLog.emit(f"home键弹窗频次：{self.API.jh()['homeInterval']}")
                    elif self.API.jh()['homeSwitch'] == '0':
                        self.OnlineCfgLog.emit("home键弹窗开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到home键弹窗配置")

                    if self.API.jh()['dianLiangSwitch'] == '1':
                        self.OnlineCfgLog.emit("电量场景开关：打开")
                    elif self.API.jh()['dianLiangSwitch'] == '0':
                        self.OnlineCfgLog.emit("电量场景开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到电量场景配置")

                    if self.API.jh()['chongdianSwitch'] == '1':
                        self.OnlineCfgLog.emit("充电场景开关：打开")
                    elif self.API.jh()['chongdianSwitch'] == '0':
                        self.OnlineCfgLog.emit("充电场景开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到充电场景配置")

                    if self.API.jh()['taSw'] == '1':
                        self.OnlineCfgLog.emit("定时弹窗场景开关：打开")
                        self.OnlineCfgLog.emit(f"定时弹窗频次：{self.API.jh()['taIt']}")
                    elif self.API.jh()['taSw'] == '0':
                        self.OnlineCfgLog.emit("定时弹窗场景开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("找不到定时弹窗配置")
                if self.API.jh()['nqDt'] == '0':
                    self.OnlineCfgLog.emit(f"自然量延时{self.API.jh()['nqDt']}秒")
                else:
                    self.OnlineCfgLog.emit(f"自然量延时{self.API.jh()['nqDt']}秒")
                if self.API.jh()['city'] == '4403' and self.API.jh()['cityStatus'] == '1':
                    self.OnlineCfgLog.emit("V2锁屏在线配置已屏蔽深圳")
                else:
                    self.OnlineCfgLog.emit("V2锁屏在线配置未屏蔽深圳")

            elif self.API.jh()['status'] == '0':
                self.OnlineCfgLog.emit("V2锁屏开关：关闭")

            elif not self.API.jh()['status']:
                self.OnlineCfgLog.emit('v2锁屏配置为空')

            if len(self.API.v3fk()['list']) < 1:
                self.OnlineCfgLog.emit(f"v3风控配置为空：{self.API.v3fk()['list']}，默认打开")
            else:
                print(self.API.v3fk())
                if self.API.v3fk()['enable'] == '0':
                    self.OnlineCfgLog.emit("v3风控关闭")
                else:
                    self.OnlineCfgLog.emit("v3风控打开")

            if len(self.API.custom()) < 1:
                self.OnlineCfgLog.emit(f"vpush风控配置为空：{self.API.custom()}，未配自定义参数，默认打开")
                self.OnlineCfgLog.emit(f"无感壁纸配置为空：{self.API.custom()}，未配自定义参数，默认关闭")
                self.OnlineCfgLog.emit(f"无感壁纸类型配置为空：{self.API.custom()}，未配自定义参数，默认关闭")
            else:
                print(self.API.custom())
                if '"vivo_push_safe_check": "0"' in self.API.custom()['params']:
                    self.OnlineCfgLog.emit("vpush风控关闭")
                else:
                    self.OnlineCfgLog.emit("vpush风控打开")
                if '"vivo_use_dk": "1"' in self.API.custom()['params']:
                    self.OnlineCfgLog.emit("无感壁纸状态：打开")
                else:
                    self.OnlineCfgLog.emit("无感壁纸状态：关闭")
                if '"vivo_setWallpaper_type": "3"' in self.API.custom()['params']:
                    self.OnlineCfgLog.emit("无感壁纸类型正确")
                else:
                    self.OnlineCfgLog.emit(f"无感壁纸类型非3或无配置")

            try:
                if 'd_status' in self.API.jh():
                    if self.API.jh()['d_status'] == '1':
                        self.OnlineCfgLog.emit("D模式配置开关：打开")
                        self.OnlineCfgLog.emit(f"D模式上报比例：{self.API.jh()['d_rate']}")
                        self.OnlineCfgLog.emit(f"D模式延时时间：{self.API.jh()['d_atTime']}")
                    elif self.API.jh()['d_status'] == '0':
                        self.OnlineCfgLog.emit("D模式配置开关：关闭")
                    else:
                        self.OnlineCfgLog.emit("D模式配置为空")
                else:
                    self.OnlineCfgLog.emit("D模式配置为空")
            except:
                self.OnlineCfgLog.emit('D模参数有误，请手动检查')
        else:
            self.OnlineCfgLog.emit("审核打开")
            if len(self.API.first()['list']) < 1:
                self.OnlineCfgLog.emit(f"合规化配置为空：{self.API.first()['list']}，默认关闭")
            else:
                if self.API.first()['list'][0]['audit'] == '0':
                    self.OnlineCfgLog.emit("合规化关闭")
                else:
                    self.OnlineCfgLog.emit("合规化打开")
