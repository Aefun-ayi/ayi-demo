from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from AdGroup import AdGroupCfg
from AdNames import AdNameCfg
from AdSources import AdSourcesCfg
from RemovePunctuation import Remove

class WorkerAdSelect(QThread):
    AllGroup = pyqtSignal(str)
    AGroup = pyqtSignal(str)
    BGroup = pyqtSignal(str)
    CGroup = pyqtSignal(str)
    SplashName = pyqtSignal(str)
    MsgName = pyqtSignal(str)
    PlaqueName = pyqtSignal(str)
    VideoName = pyqtSignal(str)
    SplashSources = pyqtSignal(str)
    MsgSources = pyqtSignal(str)
    PlaqueSources = pyqtSignal(str)
    VideoSources = pyqtSignal(str)


    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue


    def run(self):
        appInfo = self.queue.get()
        pid = appInfo.split("&")[0]
        chan = appInfo.split("&")[1]
        appid = pid[:5]
        group_info = AdGroupCfg(appid, pid, chan).ad_sid_select()
        all_info = Remove(group_info[0])
        a_info = Remove(group_info[1])
        b_info = Remove(group_info[2])
        c_info = Remove(group_info[3])
        if len(all_info) < 1:
            pass
        else:
            self.AllGroup.emit(all_info)
            # self.AllGroupText.document().setDefaultTextOption(self.option)
        if len(a_info) < 1:
            pass
        else:
            self.AGroup.emit(a_info)
            # self.AGroupText.document().setDefaultTextOption(self.option)
        if len(b_info) < 1:
            pass
        else:
            self.BGroup.emit(b_info)
            # self.BGroupText.document().setDefaultTextOption(self.option)
        if len(c_info) < 1:
            pass
        else:
            self.CGroup.emit(c_info)
            # self.CGroupText.document().setDefaultTextOption(self.option)
        adname = AdNameCfg(appid, pid, chan).ad_name_select()
        splash_name = Remove(adname[0])
        msg_name = Remove(adname[1])
        plaque_name = Remove(adname[2])
        video_name = Remove(adname[3])
        if len(adname[0]) < 1:
            pass
        else:
            self.SplashName.emit(splash_name)
            # self.SplashCfgText.document().setDefaultTextOption(self.option)
        if len(adname[1]) < 1:
            pass
        else:
            self.MsgName.emit(msg_name)
            # self.MsgCfgText.document().setDefaultTextOption(self.option)
        if len(adname[2]) < 1:
            pass
        else:
            self.PlaqueName.emit(plaque_name)
            # self.PlaqueCfgText.document().setDefaultTextOption(self.option)
        if len(adname[3]) < 1:
            pass
        else:
            self.VideoName.emit(video_name)
            # self.VideoCfgText.document().setDefaultTextOption(self.option)
        adsid = AdSourcesCfg(appid, pid, chan).ad_sids_select()
        splash_sid = Remove(adsid[0])
        msg_sid = Remove(adsid[1])
        plaque_sid = Remove(adsid[2])
        video_sid = Remove(adsid[3])
        if len(adsid[0]) < 1:
            pass
        else:
            self.SplashSources.emit(splash_sid)
            # self.SplashSourceText.document().setDefaultTextOption(self.option)
        if len(adsid[1]) < 1:
            pass
        else:
            self.MsgSources.emit(msg_sid)
            # self.MsgSourceText.document().setDefaultTextOption(self.option)
        if len(adsid[2]) < 1:
            pass
        else:
            self.PlaqueSources.emit(plaque_sid)
            # self.PlaqueSourceText.document().setDefaultTextOption(self.option)
        if len(adsid[3]) < 1:
            pass
        else:
            self.VideoSources.emit(video_sid)
            # self.VideoSourceText.document().setDefaultTextOption(self.option)
