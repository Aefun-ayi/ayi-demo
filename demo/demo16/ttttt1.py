# import requests
#
# url = 'http://192.168.7.111/aes.exe'
# res = requests.get(url)
# exe = 'aes.exe'
# with open(exe, 'wb') as f:
#     f.write(res.content)


# import os
#
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
# print(desktop_path)

# from lxml import etree
# import requests
# res = requests.get('https://www.baidu.com/')
# html = etree.HTML(res.text)
# print(html)
# from selenium import webdriver
# from time import sleep
# # 创建一个chrome浏览器实例
# browser = webdriver.Chrome()
# #访问百度首页
# browser.get('https://www.baidu.com/')
# sleep(5)
# browser.quit()


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(650, 400) # 窗口大小
        self.setWindowTitle("主窗口")

        # 开始计数按钮
        start_button = QPushButton("开始计数", self)
        # 关联到计数函数
        start_button.clicked.connect(self.start_calculation)

        # 终止计数按钮
        stop_button = QPushButton("终止计数", self)
        stop_button.clicked.connect(self.stop_calculation)

        # 布局
        layout = QGridLayout()
        layout.addWidget(start_button, 1, 1)
        layout.addWidget(stop_button, 1, 2)
        self.setLayout(layout)

        # 子窗口对象是否存在
        self.childWindowExist = False  # 默认为不存在

    # 开始计数
    def start_calculation(self):
        print("开始计数")
        self.num = 0  # 初始计数

        self.timer = QTimer()
        self.timer.start(1000)  # 间隔1秒钟执行一次操作
        self.timer.timeout.connect(self.calculation)

    # 终止计数
    def stop_calculation(self):
        print("停止计数")
        self.num = 0
        self.timer.stop()
        if self.childWindowExist:
            self.child_window.close()
        self.childWindowExist = False

    # 计数函数
    def calculation(self):
        # 每次加1
        self.num += 1
        print("当前计数为{}".format(self.num))

        if self.num % 10 == 0:
            self.childWindowExist = True
            # 如果能够整除10，则弹窗
            self.child_window = Child()
            self.child_window.window_show("当前计数为{}".format(self.num))
            self.child_window.show()

        else:
            if self.childWindowExist:
                self.child_window.close()

class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("子窗口")

    def window_show(self, text):

        # 展示内容
        self.label = QLabel(text)

        # 子窗口中的布局
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)

        self.setLayout(layout)

#运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())
