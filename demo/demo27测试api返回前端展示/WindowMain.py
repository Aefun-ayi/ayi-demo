import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget
import untitled

class MainWindow(QWidget, untitled.Ui_Form):

    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.select.clicked.connect(self.selectAd)

    def selectAd(self):
        pid = self.pid.text()
        chan = self.chan.text()
        url = 'http://192.168.80.128:8100/ad_names'
        data = {'pid': pid,
                'chan': chan
                }
        res = requests.post(url=url, data=data)
        info = res.json()
        print(info)

        # if len(info['match_ad_name']) == 0:
        #     self.info.append('无缺少的广告位')
        # else:
        #     for i in info['match_ad_name']:
        #         self.info.append(i)



        #
        # if len(info['msg_sources']) == 0:
        #     pass
        # else:
        #     for i in info['msg_sources']:
        #         self.info.append(i)

        if len(info['msg_name']) == 0:
            pass
        else:
            for i in info['msg_name']:
                self.info.append(i)

        # if len(info['all']) == 0:
        #     pass
        # else:
        #     for i in info['all']:
        #         self.info.append(i)
        # if len(info['a']) == 0:
        #     pass
        # else:
        #     for i in info['a']:
        #         self.info.append(i)
        # if len(info['b']) == 0:
        #     pass
        # else:
        #     for i in info['b']:
        #         self.info.append(i)
        # if len(info['c']) == 0:
        #     pass
        # else:
        #     for i in info['c']:
        #         self.info.append(i)

        # for i in info[0]:
        #     # for ii in i:
        #     self.info.append(i)
        # print(res.json())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())