import sys
from PyQt5.QtWidgets import QWidget, QApplication
import untitled
import requests

class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Refresh)  #按钮连接 click的动作触发refresh这个函数里面的逻辑

    def Refresh(self):
        zhanghao = self.label.text()  # 获取账号文本框的输入内容
        mima = self.label_2.text()   # 获取密码文本框的输入内容
        data = {f"{zhanghao}":f"{mima}"}
        req = requests.post('http://192.168.7.111:8008/api/post',json=data)# 接口发起请求
        self.textBrowser.setPlaceholderText(req.text)  # 发起请求后通过textBrowser来输出返回的信息




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())