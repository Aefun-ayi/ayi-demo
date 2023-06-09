from PyQt5.Qt import QApplication, QWidget, QPushButton, QThread, QMutex, pyqtSignal
import sys
import time


class PreventFastClickThreadMutex(QThread):  # 线程1
    qmut = QMutex()  # 创建线程锁
    def __init__(self):
        super().__init__()


    def run(self):
        self.qmut.lock()  # 加锁
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠
        self.qmut.unlock()  # 解锁


class PreventFastClickThreadSignal(QThread):  # 线程2
    _signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)
        self._signal.emit()


class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        # 按钮初始化
        self.btn_1 = QPushButton('按钮1', self)
        self.btn_1.setCheckable(True)
        self.btn_1.move(120, 80)
        self.btn_1.clicked.connect(self.click_1)  # 绑定槽函数

        self.btn_2 = QPushButton('按钮2', self)
        self.btn_2.setCheckable(True)
        self.btn_2.move(120, 120)
        self.btn_2.clicked.connect(self.click_2)  # 绑定槽函数

    def click_1(self):
        self.thread_1 = PreventFastClickThreadMutex()  # 创建线程
        self.thread_1.start()  # 开始线程

    def click_2(self):
        self.btn_2.setEnabled(False)
        self.thread_2 = PreventFastClickThreadSignal()
        self.thread_2._signal.connect(self.set_btn)
        self.thread_2.start()

    def set_btn(self):
        self.btn_2.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWin()
    myshow.show()
    sys.exit(app.exec_())

