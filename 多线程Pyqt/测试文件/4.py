from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time

class Worker(QThread):
    # 定义一个信号，用于更新进度条
    progress_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def run(self):
        for i in range(1, 101):
            time.sleep(0.1)
            # 发送信号，更新进度条
            self.progress_signal.emit(i)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('加载进度条')

        # 创建进度条和按钮
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, 70, 200, 20)
        self.start_button = QPushButton('开始', self)
        self.start_button.setGeometry(100, 120, 100, 30)

        # 绑定按钮点击事件
        self.start_button.clicked.connect(self.on_start_button_click)

    def on_start_button_click(self):
        # 创建工作线程
        self.worker = Worker()
        # 绑定信号和槽函数
        self.worker.progress_signal.connect(self.update_progress)
        # 启动工作线程
        self.worker.start()

    def update_progress(self, value):
        # 更新进度条
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
# ```
#
# 在你的脚本中可以这样使用：
#
# ```python
# from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
# from PyQt5.QtCore import QThread, pyqtSignal
# import sys
# import time
#
# class Worker(QThread):
#     # 定义一个信号，用于更新进度条
#     progress_signal = pyqtSignal(int)
#
#     def __init__(self, parent=None):
#         super(Worker, self).__init__(parent)
#
#     def run(self):
#         for i in range(1, 101):
#             time.sleep(0.1)
#             # 发送信号，更新进度条
#             self.progress_signal.emit(i)
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # 设置窗口大小和标题
#         self.setGeometry(100, 100, 300, 200)
#         self.setWindowTitle('加载进度条')
#
#         # 创建进度条和按钮
#         self.progress_bar = QProgressBar(self)
#         self.progress_bar.setGeometry(50, 70, 200, 20)
#         self.start_button = QPushButton('开始', self)
#         self.start_button.setGeometry(100, 120, 100, 30)
#
#         # 绑定按钮点击事件
#         self.start_button.clicked.connect(self.on_start_button_click)
#
#     def on_start_button_click(self):
#         # 创建工作线程
#         self.worker = Worker()
#         # 绑定信号和槽函数
#         self.worker.progress_signal.connect(self.update_progress)
#         # 启动工作线程
#         self.worker.start()
#
#     def update_progress(self, value):
#         # 更新进度条
#         self.progress_bar.setValue(value)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     ex.show()
#     sys.exit(app.exec_())