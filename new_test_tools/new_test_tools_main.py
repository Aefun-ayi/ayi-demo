from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QStyleFactory
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import re
import sys
import datetime
import time
from device_list import get_connected_device_models
import new_test_tools_frame
from event_path import QEventHandler

# import qdarkstyle
# import qdarkgraystyle
import qdarkstyle



class Main(QWidget, new_test_tools_frame.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(Main, self).__init__(parent)
        self.setupUi(self)
        line_apk_path = self.path_text.installEventFilter(QEventHandler(self.path_text))
        self.path_text.setPlaceholderText("拖入安装包获取路径（注意路径中不能带有中文！！！）")
        self.refresh.clicked.connect(self.ReFresh)
        self.devices_list.currentTextChanged.connect(self.devices_info)
        self.install_app.clicked.connect(self.install)
        self.clean_path.clicked.connect(self.clear_path)
        self.start_app.clicked.connect(self.startapp)
        self.stop_app.clicked.connect(self.stopapp)
        self.uninstall_app.clicked.connect(self.uninstallapp)
        self.clean_app.clicked.connect(self.clearapp)
        self.debug_app.clicked.connect(self.debug)
        self.undebug_app.clicked.connect(self.undebug)
        self.check_pro.clicked.connect(self.checkpro)
        self.clean_pro.clicked.connect(self.clearpro)
        self.ReFresh()

    def ReFresh(self):
        self.devices_list.clear()
        for i in get_connected_device_models():
            self.devices_list.addItem(f'{i}')

    def devices_info(self):
        devices_id = self.devices_list.currentText()
        id = devices_id.split("/")[-1]
        return id

    def get_packagename(self):
        path = self.path_text.text()
        aapt = []
        with open(r"D:\Test_ToolS\apk_info_test.txt", "w+") as file:
            file.write(' ')
        os.system(fr'aapt dump badging {path} > D:\Test_ToolS\apk_info_test.txt')
        with open(r'D:\Test_ToolS\apk_info_test.txt', 'rb') as f:
            p1 = "package: name='(.+?)'"
            results1 = re.finditer(pattern=p1, string=f.readline().decode('utf-8'))
            for r in results1:
                packagename = r.group(1)
                aapt.append(packagename)
        return str(aapt)[2:-2]

    def get_activityname(self):
        path = self.path_text.text()
        aapt = []
        with open(r"D:\Test_ToolS\apk_info_test.txt", "w+") as file:
            file.write(' ')
        os.system(fr'aapt dump badging {path} > D:\Test_ToolS\apk_info_test.txt')
        with open(r'D:\Test_ToolS\apk_info_test.txt', 'rb') as f:
            p2 = "launchable-activity: name='(.+?)'"
            st = str(f.readlines())
            results2 = re.findall(p2, st)
            activity = str(results2[0])
            aapt.append(activity)
        return str(aapt)[2:-2]

    def clear_path(self):
        self.path_text.clear()

    def install(self):
        path = self.path_text.text()
        demo = self.demo_app.currentText()
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        if demo == '模拟小米安装来源':
            xm = os.popen(f'adb -s {devices_info} install -i com.xiaomi.market {path}')  # 模拟小米商店安装
            # 提示框提示
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{xm.read()}')
            msg_box.exec_()
        elif demo == '模拟华为安装来源':
            hw = os.popen(f'adb -s {devices_info}  install -i com.huawei.appmarket {path}')  # 模拟华为商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{hw.read()}')
            msg_box.exec_()
        elif demo == '模拟vivo安装来源':
            vi = os.popen(f'adb -s {devices_info}  install -i com.bbk.appstore {path}')  # 模拟vivo商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{vi.read()}')
            msg_box.exec_()
        elif demo == '模拟oppo安装来源':
            op = os.popen(f'adb -s {devices_info}  install -i com.heytap.market {path}')  # 模拟oppo商店安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{op.read()}')
            msg_box.exec_()
        elif demo == '正常安装':
            anzhaung = os.popen(f'adb -s {devices_info} install -r {path}')  # 正常强制安装
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{anzhaung.read()}')
            msg_box.exec_()
        elif demo == 'debug安装（安装后同时开启debug）':
            file = open(r"D:\Test_ToolS\.debug.on", "w+")
            install = os.popen(fr'adb -s {devices_info} install {path}')  # 调用终端使用adb命令正常安装
            time.sleep(1)
            de = os.popen(f'adb -s {devices_info} push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()  # 将debug文件自动传输至包名文件夹内
            msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{install.read()}{de}')
            msg_box.exec_()

    def startapp(self):
        package_name = self.get_packagename()
        act_name = self.get_activityname()
        devices_info = self.devices_info()
        os.system(f'adb -s {devices_info} shell am start -n {package_name}/{act_name}')  # 调用终端输入adb命令

    def stopapp(self):
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        os.popen(f'adb -s {devices_info} shell am force-stop {package_name}')

    def uninstallapp(self):
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        os.system(f'adb -s {devices_info} uninstall {package_name}')

    def clearapp(self):
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        os.system(f'adb -s {devices_info} shell pm clear {package_name}')


    def debug(self):
        file = open(r"D:\Test_ToolS\.debug.on", "w+")
        time.sleep(1)
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        debugfile = os.popen(f'adb -s {devices_info} push "D:\Test_ToolS\.debug.on" /sdcard/Android/data/{package_name}/cache/.debug.on').read()
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', f'{debugfile}')
        msg_box.exec_()

    def undebug(self):
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        os.popen(f'adb -s {devices_info} shell rm /sdcard/Android/data/{package_name}/cache/.debug.on')
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', '关闭成功~')
        msg_box.exec_()

    def checkpro(self):
        package_name = self.get_packagename()
        devices_info = self.devices_info()
        progress = os.popen(f'adb -s {devices_info} shell ps|findstr {package_name}').read()
        rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间戳
        if package_name in progress:
            self.pro_text.append(rtime + '\n' + progress)
        else:
            self.pro_text.append(rtime + '\n无进程信息\n')

    def clearpro(self):
        self.pro_text.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    from qt_material import apply_stylesheet
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    window = Main()
    window.show()

    sys.exit(app.exec_())

