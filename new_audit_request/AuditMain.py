import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import AuditFrame
import AuditRequest
import qtawesome as qta
from qt_material import apply_stylesheet
from PyQt5 import QtCore



class Main(QWidget, AuditFrame.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(Main, self).__init__(parent)
        self.setupUi(self)

        SelectIcon = qta.icon('msc.search', color='green')
        self.select.setIcon(SelectIcon)
        self.select.setIconSize(QtCore.QSize(50, 50))
        ClearIcon = qta.icon('fa.trash-o', color='green')
        self.clear.setIcon(ClearIcon)
        self.clear.setIconSize(QtCore.QSize(50, 50))
        self.clear.clicked.connect(self.ClearInfo)
        self.select.clicked.connect(self.Audit_info)

    def ClearInfo(self):
        self.test_info.clear()
        self.release_info.clear()

    def Audit_info(self):
        pid = self.pid.text()
        ver = self.ver.text()
        brand = self.brand.text()
        cha = 'csj'
        uid = 10001
        self.request_info_test = AuditRequest.AuditRequest(pid, cha, brand, ver, uid).Audit_request_test()
        # print(self.request_info)
        if self.request_info_test['data'] != []:
            if 'pass' in dict(self.request_info_test['data']).keys():
                if self.request_info_test['data']['pass'] is True:
                    self.test_info.append(f"过审开关状态：{self.request_info_test['data']['pass']}，当前应为B包状态")

                elif self.request_info_test['data']['pass'] is False:
                    self.test_info.append(f"过审开关状态：{self.request_info_test['data']['pass']}，当前应为A包状态")
            else:
                self.test_info.append('查询不到配置信息')

            if 'popup' in dict(self.request_info_test['data']).keys():
                if self.request_info_test['data']['popup'] is True:
                    self.test_info.append(f"隐私弹窗状态：{self.request_info_test['data']['popup']}，首次启动时应有隐私弹窗")

                elif self.request_info_test['data']['popup'] is False:
                    self.test_info.append(f"隐私弹窗状态：{self.request_info_test['data']['popup']}，启动时没有隐私弹窗")

            else:
                self.test_info.append('查询不到隐私弹窗字段信息，隐私弹窗默认关闭')

        else:
            self.test_info.append('查询不到配置信息')

        self.request_info_release = AuditRequest.AuditRequest(pid, cha, brand, ver, uid).Audit_request_release()
        # print(self.request_info)
        if self.request_info_release['data'] != []:
            if 'pass' in dict(self.request_info_release['data']).keys():
                if self.request_info_release['data']['pass'] is True:
                    self.release_info.append(f"过审开关状态：{self.request_info_release['data']['pass']}，当前应为B包状态")

                elif self.request_info_release['data']['pass'] is False:
                    self.release_info.append(f"过审开关状态：{self.request_info_release['data']['pass']}，当前应为A包状态")
            else:
                self.release_info.append('查询不到配置信息')

            if 'popup' in dict(self.request_info_release['data']).keys():
                if self.request_info_release['data']['popup'] is True:
                    self.release_info.append(f"隐私弹窗状态：{self.request_info_release['data']['popup']}，首次启动时应有隐私弹窗")

                elif self.request_info_release['data']['popup'] is False:
                    self.release_info.append(f"隐私弹窗状态：{self.request_info_release['data']['popup']}，启动时没有隐私弹窗")

            else:
                self.release_info.append('查询不到隐私弹窗字段信息，隐私弹窗默认关闭')

        else:
            self.release_info.append('查询不到配置信息')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    window.show()
    sys.exit(app.exec_())