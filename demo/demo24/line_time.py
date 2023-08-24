import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber
from PyQt5.QtCore import QTimer, QTime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("倒计时")
        self.setGeometry(100, 100, 200, 100)

        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(50, 30, 100, 30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.end_time = QTime(18, 30)  # 设置截止时间为12点
        self.lcd.setDigitCount(5)  # 设置显示位数

    def start_timer(self):
        current_time = QTime.currentTime()
        remaining_time = current_time.secsTo(self.end_time)

        if remaining_time < 0:  # 如果当前时间已经超过截止时间，则将截止时间设置为次日的12点
            next_day = current_time.addDays(1)
            self.end_time = QTime(12, 0)
            remaining_time = current_time.secsTo(next_day)

        self.lcd.display(remaining_time)  # 显示截止时间剩余的秒数
        self.timer.start(1000)  # 每隔1秒触发一次timeout事件

    def update_timer(self):
        current_time = QTime.currentTime()
        remaining_time = current_time.secsTo(self.end_time)

        if remaining_time < 0:
            self.timer.stop()  # 倒计时结束，停止计时器
            self.lcd.display(0)  # 设置显示为0
        else:
            self.lcd.display(remaining_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start_timer()
    sys.exit(app.exec_())