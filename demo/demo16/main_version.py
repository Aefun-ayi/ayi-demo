import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import untitled
import requests
from PyQt5.QtCore import QCoreApplication



class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.current_version = '1.0'
        self.session = requests.Session()
        self.check_version()

    def check_version(self):
        try:
            sion = self.session.get('http://192.168.7.111:8008/version')
            remote_version = sion.text
            print(remote_version)
            if self.current_version != remote_version:
                QMessageBox.warning(self, "提示", "开始版本更新")
                url = 'http://192.168.7.111/main_version_V1.1.exe'  # 地址写下一代的版本号 预设版本号
                res = requests.get(url)
                exe = r'D:\\keep\\公用-储存安装包\\05_moon\\0523-11-37头-充电多多\\main_version_V1.1.exe'
                with open(exe, 'wb') as f:
                    f.write(res.content)
                QMessageBox.warning(self, "提示", "更新完成")
                self.session.close()
                QCoreApplication.instance().quit()
                QApplication.exit()

        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

