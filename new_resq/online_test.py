import requests
import untitled
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import os


class New_Res():

    def __init__(self,appid, apk_version, cha):
        self.appid = appid
        self.apk_version = apk_version
        self.cha = cha
    #     self.appid = ui.app_id.text()
    #     self.cha = ui.app_chanl.text()
    #     self.apk_version = ui.apk_version.text()


    def aduit(self):
        # self.appid = ui.app_id.text()
        # self.cha = ui.app_chanl.text()
        # self.apk_version = ui.apk_version.text()
        # print(type(self.appid))

        url = ' https://ttt.yangguangzhujia.com/activity/get/state'
        head = {"Content-Type": "application/json",}
        data = {"app_id": f"{self.appid}","cha": f"{self.cha}","version": "1.0.1","apk_version": f"{self.apk_version}"}
        res = requests.post(url, headers=head, json=data)
        self.audit_state = res.json() # 0关闭审核  1开启审核
        # return self.audit_state['data']['audit_state']
        return self.audit_state
        # print(self.audit_state)
        # print(type(self.audit_state))
        # if audit_state == True:
        #     return '审核打开'
        # if audit_state == False:
        #     return '审核关闭'
        # return audit_state

    def show_info(self):
        show = []
        url = 'https://ttt.yangguangzhujia.com/activity/get/switch'
        head = {
            "Content-Type": "application/json",
            }
        data = {
            "app_id": f"{self.appid}",
            "cha": f"{self.cha}",
            "apk_version": f"{self.apk_version}",
            "track_channel": "default"
        }
        res = requests.post(url, headers=head, json=data)
        self.bh = str(res.json()['data']['app_alive_module'])+'保活模块开关'  # 保活模块
        self.outside = str(res.json()['data']['outside_activity'])+'站外营销模块开关'  # 站外营销模块
        self.ad_module = str(res.json()['data']['ad_module'])+'广告模块开关'  # 广告模块  0关闭 1开启
        show.append(self.bh)
        show.append(self.outside)
        show.append(self.ad_module)
        # print(res.json())
        return show

    def out_side(self):
        url = 'https://ttt.yangguangzhujia.com/activity/get/config/market'
        head = {
            "Content-Type": "application/json",
        }
        data = {
            "app_id": f"{self.appid}",
            "cha": f"{self.cha}",
            "apk_version": f"{self.apk_version}",
            "track_channel": "default"
        }
        res = requests.post(url, headers=head, json=data)
        return res.json()['data']['detail']

    def nqdt(self):
        ziranliang = self.out_side()['nqDt']
        return ziranliang

    def lock_on(self):
        lock_dig = self.out_side()['market_param']['lock']['lock_on']#锁屏弹窗开关
        return lock_dig

    def lock_first_time(self):
        lock_delay =self.out_side()['market_param']['lock']['lock_first_time']  #锁屏弹窗的首次延时
        return lock_delay

    def unlock_on(self):
        unlock_dig = self.out_side()['market_param']['unlock']['unlock_on']  # 解锁后弹窗开关
        return unlock_dig

    def unlock_super_on(self):
        unlock_qiangtan = self.out_side()['market_param']['unlock']['unlock_super_on']  # 解锁后弹窗强停开关
        return unlock_qiangtan

    def unlock_first_time(self):
        unlock_delay = self.out_side()['market_param']['unlock']['unlock_first_time']  # 解锁后弹窗首次延时
        return unlock_delay

    def unlock_rate_type(self):
        unlock_rate_type = self.out_side()['market_param']['unlock']['unlock_rate']['rate_type']  # 解锁后弹窗频次类型  1为时间间隔  2为次数间隔
        return unlock_rate_type

    def unlock_first_order(self):
        unlock_rate_first_order = self.out_side()['market_param']['unlock']['unlock_rate']['first_order']  # 解锁后弹窗频次次数间隔（首次在第几次触发）
        return unlock_rate_first_order

    def unlock_interval_num(self):
        unlock_rate_interval_num = self.out_side()['market_param']['unlock']['unlock_rate']['interval_num']  # 解锁后弹窗频次次数间隔-间隔次数
        return unlock_rate_interval_num

    def unlock_rate_value(self):
        unlock_rate_value = self.out_side()['market_param']['unlock']['unlock_rate']['rate_value']  # 解锁后弹窗时间间隔-数值，数值单位/秒
        return unlock_rate_value

    def home_on(self):
        home_dig = self.out_side()['market_param']['home']['home_on']  #home弹窗开关
        return home_dig

    def home_super_on(self):
        home_qiangtan = self.out_side()['market_param']['home']['home_on']['home_super_on'] #home弹窗广告强弹开关
        return home_qiangtan

    def home_first_time(self):
        home_delay = self.out_side()['market_param']['home']['home_on']['home_first_time']  # home弹窗首次延时
        return home_delay

    def home_rate_type(self):
        home_rate_type = self.out_side()['market_param']['home']['home_interval']['rate_type']  #home弹窗频次类型 1为时间间隔  2为次数间隔
        return home_rate_type

    def home_first_order(self):
        home_rate_first_order = self.out_side()['market_param']['home']['home_interval']['first_order']  # home弹窗频次次数间隔（首次在第几次触发）
        return home_rate_first_order

    def home_interval_num(self):
        home_rate_interval_num = self.out_side()['market_param']['home']['home_interval']['interval_num']  # home弹窗频次次数间隔-间隔次数
        return home_rate_interval_num

    def home_rate_value(self):
        home_rate_value = self.out_side()['market_param']['home']['home_interval']['rate_value']  # home弹窗时间间隔-数值，数值单位/秒
        return home_rate_value

    def electric_on(self):
        electric = self.out_side()['market_param']['electric']['electric_on']  #电量弹窗开关
        return electric

    def electric_super_on(self):
        electric_super_on = self.out_side()['market_param']['electric']['electric_super_on']  #电量弹窗广告强弹开关
        return electric_super_on

    def electric_pers(self):
        electric_pers = self.out_side()['market_param']['electric']['electric_pers']  #电量弹窗百分比配置
        return electric_pers

    def pop_method(self):
        pop_method = self.out_side()['market_param']['electric']['pop_method']  # 电量弹窗弹出方式 1马上弹出 2下次触发home时弹窗
        return pop_method

    def pop_interval(self):
        pop_interval = self.out_side()['market_param']['electric']['pop_interval']  # 电量弹窗的继续弹出间隔 单位秒
        return pop_interval

    def charge_on(self):
        charge_on = self.out_side()['market_param']['charge']['charge_on']  #充电弹窗开关
        return charge_on

    def charge_super_on(self):
        charge_super_on = self.out_side()['market_param']['charge']['charge_super_on']  #充电弹窗广告强弹开关
        return charge_super_on

    def wifi_on(self):
        wifi_on = self.out_side()['market_param']['wifi']['wifi_on']  # wifi弹窗开关
        return wifi_on

    def wifi_super_on(self):
        wifi_super_on = self.out_side()['market_param']['wifi']['wifi_super_on']  #wifi弹窗广告强弹开关
        return wifi_super_on

    def timer_on(self):
        timer_on = self.out_side()['market_param']['timer']['timer_on']  # 定时弹窗开关
        return timer_on

    def timer_super_on(self):
        timer_super_on = self.out_side()['market_param']['timer']['timer_super_on'] #定时弹窗广告强弹开关
        return timer_super_on

    def timer_first_time(self):
        timer_first_time = self.out_side()['market_param']['timer']['timer_first_time'] #定时弹窗首次触发时间
        return timer_first_time

    def timer_interval(self):
        timer_interval = self.out_side()['market_param']['timer']['timer_interval']  # 定时弹窗频次 单位秒
        return timer_interval

#     def ttt_test(self):
#         print(self.audit_state)
#         # print(self.aduit())
#
# if __name__ == '__main__':
#     # 初始化数据
#     # 。。。。。
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = untitled.Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     ui.test_ment.clicked.connect(New_Res.aduit)
#     sys.exit(app.exec_())
#
if __name__ == '__main__':
    a = New_Res('39523','1040','csj')
    # a.out_side()
    a.aduit()
    print(a.aduit())

#     a.aduit()
#     a.show_info()
#     a.out_side()
#     a.nqdt()
#     print(a.nqdt())
#     print(a.aduit())
#     print(a.timer_interval())
#     print(a.show_info())
#     print(a.aduit())
