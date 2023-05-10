import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import check_cfg_frame
from event_handler import QEventHandler
from PyQt5.QtWidgets import QMessageBox
from queue import Queue
from worke import Worker
import Remove
import ad_select
import ad_name
import ad_source
import ad_than_name

class MainWindow(QWidget, check_cfg_frame.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.queue = Queue()
        # 创建一个工作线程，并将其信号连接到updateLabel方法
        self.thread = Worker(self.queue)
        self.thread.sig1.connect(self.updateSucCfg)
        self.thread.sig2.connect(self.updateFailCfg)
        #连接按钮点击信号到buttonClicked方法
        line_apk_path = self.line_apkdir_path.installEventFilter(QEventHandler(self.line_apkdir_path))
        self.select_online.clicked.connect(self.online_select_click)
        self.clean_online_text.clicked.connect(self.online_clean_click)
        self.select_ad.clicked.connect(self.ad_select_click)
        self.clean_ad_text.clicked.connect(self.ad_clean_click)
        self.select_ad_2.clicked.connect(self.ad_name_than)
        self.clean_ad_text_2.clicked.connect(self.ad_name_clean)

    def online_select_click(self):
        path = self.line_apkdir_path.text()
        self.queue.put(path)
        #点击按钮时启动工作线程
        self.thread.start()

    def updateSucCfg(self, text):
        self.suc_cfg.append(text)

    def updateFailCfg(self, text):
        self.fail_cfg.append(text)

    def online_clean_click(self):
        ui.suc_cfg.clear()
        ui.fail_cfg.clear()

    def ad_select_click(self):
        try:
            pid = self.prid.text()
            chan = self.app_chan.text()
            # 输入项目id为空则弹窗提示
            if pid == '':
                pid_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入项目id')
                pid_msg_box.exec_()
            # 输入渠道标识为空则弹窗提示
            if chan == '':
                chan_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入渠道')
                chan_msg_box.exec_()
            else:
                appid = pid[:5]
                group_info = ad_select.Ad_Group_Cfg(appid, pid, chan).ad_select()
                all_info = Remove.remove_punctuation_and_replace(group_info[0])
                a_info = Remove.remove_punctuation_and_replace(group_info[1])
                b_info = Remove.remove_punctuation_and_replace(group_info[2])
                c_info = Remove.remove_punctuation_and_replace(group_info[3])
                if len(all_info)<1:
                    pass
                else:
                    self.all_text.setText(all_info)
                if len(a_info)<1:
                    pass
                else:
                    self.A_text.setText(a_info)
                if len(b_info)<1:
                    pass
                else:
                    self.B_text.setText(a_info)
                if len(c_info)<1:
                    pass
                else:
                    self.C_text.setText(a_info)
                adname = ad_name.Ad_Name_Cfg(appid,pid,chan).ad_select()
                splash_name = Remove.remove_punctuation_and_replace(adname[0])
                msg_name = Remove.remove_punctuation_and_replace(adname[1])
                plaque_name = Remove.remove_punctuation_and_replace(adname[2])
                video_name = Remove.remove_punctuation_and_replace(adname[3])
                if len(adname[0])<1:
                    pass
                else:
                    self.splash_cfg_text.setText(splash_name)
                if len(adname[1])<1:
                    pass
                else:
                    self.msg_cfg_text.setText(msg_name)
                if len(adname[2])<1:
                    pass
                else:
                    self.plaque_cfg_text.setText(plaque_name)
                if len(adname[3])<1:
                    pass
                else:
                    self.video_cfg_text.setText(video_name)
                adsid = ad_source.Ad_Sids_Cfg(appid, pid, chan).ad_select()
                splash_sid = Remove.remove_punctuation_and_replace(adsid[0])
                msg_sid = Remove.remove_punctuation_and_replace(adsid[1])
                plaque_sid = Remove.remove_punctuation_and_replace(adsid[2])
                video_sid = Remove.remove_punctuation_and_replace(adsid[3])
                if len(adsid[0])<1:
                    pass
                else:
                    self.splash_source_text.setText(splash_sid)
                if len(adsid[1])<1:
                    pass
                else:
                    self.msg_source_text.setText(msg_sid)
                if len(adsid[2])<1:
                    pass
                else:
                    self.plaque_source_text.setText(plaque_sid)
                if len(adsid[3])<1:
                    pass
                else:
                    self.video_source_text.setText(video_sid)

        except Exception as e:
            tips = QMessageBox(QMessageBox.Critical, '错误', f'程序错误:{e}')
            tips.exec_()

    def ad_clean_click(self):
        self.all_text.clear()
        self.A_text.clear()
        self.B_text.clear()
        self.C_text.clear()
        self.splash_cfg_text.clear()
        self.msg_cfg_text.clear()
        self.video_cfg_text.clear()
        self.plaque_cfg_text.clear()
        self.splash_source_text.clear()
        self.msg_source_text.clear()
        self.video_source_text.clear()
        self.plaque_source_text.clear()

    def ad_name_than(self):
        try:
            pid = self.prid_2.text()
            chan = self.app_chan_2.text()
            pro = self.package_info.text()
            # 输入项目id为空则弹窗提示
            if pid == '':
                pid_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入项目id')
                pid_msg_box.exec_()
            # 输入渠道标识为空则弹窗提示
            if chan == '':
                chan_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入渠道')
                chan_msg_box.exec_()
            if pro == '':
                pro_msg_box = QMessageBox(QMessageBox.Critical, '错误', 'key不可为空')
                pro_msg_box.exec_()
            else:
                appid = pid[:5]
                adthan = ad_than_name.Ad_Than_Cfg(appid, pid, chan, pro).ad_select()
                match = Remove.remove_punctuation_and_replace(adthan[0])
                short = Remove.remove_punctuation_and_replace(adthan[1])
                tmr = Remove.remove_punctuation_and_replace(adthan[2])
                self.match_text.setText(f"-----匹配的广告位-----\n{match}")
                if len(adthan[1]) < 1:
                    self.lack_text.setText('无缺少的广告位')
                else:
                    self.lack_text.setText(f"-----含有缺少的广告位-----\n{short}")
                if len(adthan[2]) < 1:
                    self.tmr_text.setText('无冗余的广告位')
                else:
                    self.tmr_text.setText(f"-----含有冗余的广告位-----\n{tmr}")
        except Exception as e:
            tips = QMessageBox(QMessageBox.Critical, '错误', f'程序错误:{e}')
            tips.exec_()

    def ad_name_clean(self):
        self.match_text.clear()
        self.tmr_text.clear()
        self.lack_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())