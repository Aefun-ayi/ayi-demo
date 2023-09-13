from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from AdContrast import AdContrastCfg
from RemovePunctuation import Remove

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
        appid = pid[:5]
        adthan = AdContrastCfg(appid, pid, chan, pro).ad_contrast_select()
        match = Remove(adthan[0])
        short = Remove(adthan[1])
        tmr = Remove(adthan[2])
        self.Match.emit(f"-----匹配的广告位-----\n{match}")
        if len(adthan[1]) < 1:
            self.Lack.emit('无缺少的广告位')
        else:
            self.Lack.emit(f"-----含有缺少的广告位-----\n{short}")
        if len(adthan[2]) < 1:
            self.Tmr.emit('无冗余的广告位')
        else:
            self.Tmr.emit(f"-----含有冗余的广告位-----\n{tmr}")
