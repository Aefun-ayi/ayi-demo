import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ProgressThread(QThread):
    update_progress = pyqtSignal(int)

    def run(self):
        for i in range(1, 101):
            self.update_progress.emit(i)
            time.sleep(0.1)

class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(30, 40, 200, 25)

        self.btn_start = QPushButton('Start', self)
        self.btn_start.move(50, 80)
        self.btn_start.clicked.connect(self.start_progress)

        self.btn_stop = QPushButton('Stop', self)
        self.btn_stop.move(150, 80)
        self.btn_stop.clicked.connect(self.stop_progress)

        self.progress_thread = ProgressThread()
        self.progress_thread.update_progress.connect(self.update_progress)

        self.setGeometry(300, 300, 280, 120)
        self.setWindowTitle('PyQt5 Progress Bar')
        self.show()

    def start_progress(self):
        self.progress_thread.start()

    def stop_progress(self):
        self.progress_thread.terminate()

    def update_progress(self, value):
        self.progress.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProgressBar()
    sys.exit(app.exec_())