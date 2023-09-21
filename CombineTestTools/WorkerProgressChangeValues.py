from PyQt5.QtCore import QThread, pyqtSignal
import requests
import os

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
        exe = fr'{desktop_path}\测试工具箱V1.2.exe'  # 文件存放地址

        with open(exe, 'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                downloaded_size += len(data)
                f.write(data)
                self.progress.emit(int(downloaded_size * 100 / total_size))