import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QLabel, QApplication, QDialog
from Worker_Progress_Change_Value import DownloaderThread
from PyQt5 import QtCore


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("更新进度")
        self.resize(275, 69)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(
            "QProgressBar { border: 2px solid grey; "
            "border-radius: 5px; "
            "background-color: #FFFFFF;"
            " text-align: center;}"
            "QProgressBar::chunk {background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1  #DB7093); }")
        layout = QVBoxLayout()
        self.lable = QLabel()
        self.lable.setText('下载进度：')
        self.lable.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lable)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
        self.show()
        self.start_download()

    def start_download(self):
        url = 'http://192.168.7.111/查询配置V2.5.exe'
        self.downloader_thread = DownloaderThread(url)
        self.downloader_thread.progress.connect(self.update_progress)
        self.downloader_thread.finished.connect(self.download_finished)
        self.downloader_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def download_finished(self):
        self.progress_bar.setValue(100)
        self.close()

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())