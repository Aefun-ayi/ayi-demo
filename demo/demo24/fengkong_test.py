import os
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal


class DownloaderThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url, stream=True)
        total_size = int(response.headers.get('Content-Length', 0))
        downloaded_size = 0
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 定义桌面路径 获取任意使用的当前电脑的桌面路径
        exe = fr'{desktop_path}\ceshi.html'  # 文件存放地址

        with open(exe, 'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                downloaded_size += len(data)
                f.write(data)
                self.progress.emit(int(downloaded_size * 100 / total_size))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("下载进度条")
        self.resize(1143, 723)
        # self.button = QPushButton("开始下载")
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(
            "QProgressBar { border: 2px solid grey; "
            "border-radius: 5px; "
            "background-color: #FFFFFF;"
            " text-align: center;}"
            "QProgressBar::chunk {background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1  #DB7093); }")

        layout = QVBoxLayout()
        # layout.addWidget(self.button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

        # self.button.clicked.connect(self.start_download)
        self.start_download()

    def start_download(self):
        # self.button.setEnabled(False)

        url = 'http://192.168.7.111/ceshi.html'
        self.downloader_thread = DownloaderThread(url)
        self.downloader_thread.progress.connect(self.update_progress)
        self.downloader_thread.finished.connect(self.download_finished)
        self.downloader_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def download_finished(self):
        # self.button.setEnabled(True)
        self.progress_bar.setValue(100)
        print("下载完成")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())