from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLCDNumber, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("倒计时")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.lcd_number = QLCDNumber()
        self.lcd_number.setDigitCount(8)  # 设置显示的位数为8位

        layout.addWidget(self.lcd_number)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(1000)  # 每秒更新一次
        self.timer.timeout.connect(self.update_time)

        self.start_countdown()

    def start_countdown(self):
        self.timer.start()
        self.update_time()

    def update_time(self):

        current_time = QTime.currentTime()
        target_time = QTime(18, 30)  # 设置截止时间
        remaining_time = current_time.secsTo(target_time)

        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        seconds = remaining_time % 60

        # 格式化成时分秒的字符串
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

        self.lcd_number.display(time_str)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.start_countdown()
    window.show()
    sys.exit(app.exec())