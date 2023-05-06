import sys
import time
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import os
from event_paht import QEventHandler
import re
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QProgressDialog
import untitled
from pyaxmlparser import APK


class MainWindows():
    # def path_apk():
    #     path = ui.path_text.text()
    #     return path

    def clear_path():
        ui.path_text.clear()

    # def packaganame():
    #     path = ui.path_text.text()
    #
    #     apk = APK(path)
    #     # 获取包名
    #     package_name = apk.package
    #     return package_name
    #
    # def activityname():
    #     apk = APK()
    #     path = ui.path_text.text()
    #
    #     # 获取activity名
    #     act_name = apk.package
    #     return act_name

    def install():
        demo = ui.demo_app.currentText()
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        if demo == '模拟小米安装来源':
            xm = os.popen(f'adb install -i com.xiaomi.market {path}')  # 模拟小米商店安装
            # 提示框提示
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{xm.read()}')
            msg_box.exec_()
        elif demo == '模拟华为安装来源':
            hw = os.popen(f'adb install -i com.huawei.appmarket {path}')  # 模拟华为商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{hw.read()}')
            msg_box.exec_()
        elif demo == '模拟vivo安装来源':
            vi = os.popen(f'adb install -i com.bbk.appstore {path}')  # 模拟vivo商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{vi.read()}')
            msg_box.exec_()

        elif demo == '模拟oppo安装来源':
            op = os.popen(f'adb install -i com.heytap.market {path}')  # 模拟oppo商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{op.read()}')
            msg_box.exec_()

        elif demo == '正常安装':
            anzhaung = os.popen(f'adb install -r {path}')  # 正常强制安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{anzhaung.read()}')
            msg_box.exec_()

        elif demo == 'debug安装':
            file = open(r"D:\Test_ToolS\.debug.on", "w+")
            install = os.popen(fr'adb install {path}')  # 调用终端使用adb命令正常安装
            time.sleep(1)
            de = os.popen(f'adb push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()  # 将debug文件自动传输至包名文件夹内
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{install.read()}{de}')
            msg_box.exec_()

    def startapp():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        act_name = apk.get_main_activity()
        os.system(f'adb shell am start -n {package_name}/{act_name}')  # 调用终端输入adb命令

    def stopapp():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        os.popen(f'adb shell am force-stop {package_name}')

    def uninstallapp():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        os.system(f'adb uninstall {package_name}')

    def clearapp():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        os.system(f'adb shell pm clear {package_name}')

    def debug():
        file = open(r"D:\Test_ToolS\.debug.on", "w+")
        time.sleep(1)
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        debugfile = os.popen(f'adb push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', f'{debugfile}')
        msg_box.exec_()

    def undebug():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        os.popen(f'adb shell rm /sdcard/Android/data/{package_name}/cache/.debug.on')
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', '关闭成功~')
        msg_box.exec_()

    def checkpro():
        path = ui.path_text.text()
        apk = APK(path)
        # 获取包名
        package_name = apk.package
        progress = os.popen(f'adb shell ps|findstr {package_name}').read()
        rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
        if package_name in progress:
            ui.pro_text.append(rtime + '\n' + progress)
        else:
            ui.pro_text.append(rtime + '\n无进程信息\n')

    def clearpro():
        ui.pro_text.clear()

if __name__ == '__main__':
        # 初始化数据
        # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.path_text.installEventFilter(QEventHandler(ui.path_text))
    ui.install.clicked.connect(MainWindows.install)
    ui.path_clear.clicked.connect(MainWindows.clear_path)
    ui.start_app.clicked.connect(MainWindows.startapp)
    ui.stop_app.clicked.connect(MainWindows.stopapp)
    ui.uninstall_app.clicked.connect(MainWindows.uninstallapp)
    ui.clear_app.clicked.connect(MainWindows.clearapp)
    ui.debug.clicked.connect(MainWindows.debug)
    ui.undebug.clicked.connect(MainWindows.undebug)
    ui.check_pro.clicked.connect(MainWindows.checkpro)
    ui.pro_clear.clicked.connect(MainWindows.clearpro)
    sys.exit(app.exec_())