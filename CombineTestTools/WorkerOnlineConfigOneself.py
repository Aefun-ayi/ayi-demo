import datetime
import ApiConfig
import requests
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


class WorkerOnlineConfigOneselfMain(QThread):

    OnlineCfgLog = pyqtSignal(str)

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        appInfo = self.queue.get()
        cha = appInfo.split("&")[1]
        pid = appInfo.split("&")[0]
        try:
            url = f'{ApiConfig.centos()}/online_config_oneself'
            data = {'pid': pid,
                    'chan': cha}
            res = requests.post(url, data)
            filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='/', m='/', d='',
                                                                                                  h=':', f=':', s='')
            for i in res.json():
                self.OnlineCfgLog.emit(filetime + '      ' + i)
        except Exception as e:
            print(e)
            pass
