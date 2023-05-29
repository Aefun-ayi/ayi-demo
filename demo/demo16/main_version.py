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
            sion = self.session.get('http://192.168.7.111:8008/version')  # http://192.168.7.43:8008/version
            remote_version = sion.text
            print(remote_version)
            if self.current_version != remote_version:
                QMessageBox.warning(self, "提示", "开始版本更新")
                url = 'http://192.168.7.111/main_version_V1.1.exe'  # 地址写下一代的版本号 预设版本号
                res = requests.get(url)
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                exe = fr'{desktop_path}\main_version_V1.1.exe'  # 文件存放地址
                with open(exe, 'wb') as f:
                    f.write(res.content)
                QMessageBox.warning(self, "提示", "更新完成")
                self.session.close()  # 关闭接口链接
                QCoreApplication.instance().quit()  # 退出程序页面
                QApplication.exit()

        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

