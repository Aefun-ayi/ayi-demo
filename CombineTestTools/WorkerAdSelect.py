import requests
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import ApiConfig

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
        try:
            name_url = f'{ApiConfig.centos()}/ad_names'
            name_data = {'pid': pid,
                         'chan': chan
                         }
            name_res = requests.post(url=name_url, data=name_data)
            name_info = name_res.json()
            if len(name_info['msg_name']) == 0:
                pass
            else:
                for i in name_info['msg_name']:
                    self.MsgName.emit(i)
            if len(name_info['splash_name']) == 0:
                pass
            else:
                for i in name_info['splash_name']:
                    self.SplashName.emit(i)
            if len(name_info['plaque_name']) == 0:
                pass
            else:
                for i in name_info['plaque_name']:
                    self.PlaqueName.emit(i)
            if len(name_info['video_name']) == 0:
                pass
            else:
                for i in name_info['video_name']:
                    self.VideoName.emit(i)
            group_url = f'{ApiConfig.centos()}/ad_group'
            group_data = {'pid': pid,
                          'chan': chan
                          }
            group_res = requests.post(url=group_url, data=group_data)
            group_info = group_res.json()
            if len(group_info['all']) == 0:
                pass
            else:
                for i in group_info['all']:
                    self.AllGroup.emit(i)
            if len(group_info['a']) == 0:
                pass
            else:
                for i in group_info['a']:
                    self.AGroup.emit(i)
            if len(group_info['b']) == 0:
                pass
            else:
                for i in group_info['b']:
                    self.BGroup.emit(i)
            if len(group_info['c']) == 0:
                pass
            else:
                for i in group_info['c']:
                    self.CGroup.emit(i)
            sources_url = f'{ApiConfig.centos()}/ad_sources'
            sources_data = {'pid': pid,
                            'chan': chan
                            }
            sources_res = requests.post(url=sources_url, data=sources_data)
            sources_info = sources_res.json()
            if len(sources_info['msg_sources']) == 0:
                pass
            else:
                for i in sources_info['msg_sources']:
                    self.MsgSources.emit(i)
            if len(sources_info['splash_sources']) == 0:
                pass
            else:
                for i in sources_info['splash_sources']:
                    self.SplashSources.emit(i)
            if len(sources_info['plaque_sources']) == 0:
                pass
            else:
                for i in sources_info['plaque_sources']:
                    self.PlaqueSources.emit(i)
            if len(sources_info['video_sources']) == 0:
                pass
            else:
                for i in sources_info['video_sources']:
                    self.VideoSources.emit(i)
        except Exception as e:
            print(e)
            pass
