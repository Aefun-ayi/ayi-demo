import requests
from PyQt5.QtCore import QThread, pyqtSignal, QMutex

class WorkerAdContrast(QThread):
    Match = pyqtSignal(str)
    Lack = pyqtSignal(str)
    Tmr = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        appInfo = self.queue.get()
        pid = appInfo.split("&")[0]
        chan = appInfo.split("&")[1]
        pro = appInfo.split("&")[2]
        try:
            url = 'http://192.168.7.188:8101/ad_contrast'
            data = {'pid': pid,
                    'chan': chan,
                    'pro': pro
                    }
            res = requests.post(url=url, data=data)
            info = res.json()
            print(info)
            if len(info['match_ad_name']) == 0:
                self.Match.emit('无匹配的广告位')
            else:
                for i in info['match_ad_name']:
                    self.Match.emit(i)
            if len(info['short_ad_name']) == 0:
                self.Lack.emit('无缺少的广告位')
            else:
                for i in info['short_ad_name']:
                    self.Lack.emit(i)
            if len(info['tmr_ad_name']) == 0:
                self.Tmr.emit('无冗余的广告位')
            else:
                for i in info['tmr_ad_name']:
                    self.Tmr.emit(i)
        except Exception as e:
            print(e)
            pass