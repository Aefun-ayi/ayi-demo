import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from queue import Queue
from Worker_run import Worker
import check_cfg_frame
from event_handler import QEventHandler
import Remove
import Ad_Sid
import Ad_Name
import Ad_Source
import Ad_Contrast
import os
import Screen_Img
import Mkdir_name
import Mk_five_dirname
from Worker_auto import Worker_Auto
from qt_material import apply_stylesheet
from Worker_Ash import Worker_Ash_Pross


class MainWindow(QWidget, check_cfg_frame.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.queue = Queue()
        self.auto_queue = Queue()
        self.ash_queue = Queue()
        # 创建一个工作线程，并将其信号连接到updateLabel方法
        self.thread = Worker(self.queue)
        self.thread.sig1.connect(self.updateSucCfg)
        self.thread.sig2.connect(self.updateFailCfg)
        self.auto_thread = Worker_Auto(self.auto_queue)
        self.auto_thread.log.connect(self.updateAutoCfg)
        self.auto_thread.lock_img_path.connect(self.Lock_update)
        self.auto_thread.unlock_img_path.connect(self.Unlock_update)
        self.auto_thread.unlock_ad_path.connect(self.Unlock_Ad_update)
        self.auto_thread.charge_img_path.connect(self.Charge_updata)
        self.auto_thread.charge_ad_path.connect(self.Charge_Ad_update)
        self.auto_thread.wifi_img_path.connect(self.Wifi_update)
        self.auto_thread.wifi_ad_path.connect(self.Wifi_Ad_update)
        self.auto_thread.home_img_path.connect(self.Home_update)
        self.auto_thread.home_ad_path.connect(self.Home_Ad_update)
        self.auto_thread.timing_img_path.connect(self.Timing_update)
        self.auto_thread.timing_ad_path.connect(self.Timing_Ad_update)
        self.ash_thread = Worker_Ash_Pross(self.ash_queue)
        self.ash_thread.log.connect(self.Update_Ash_Cfg)
        self.ash_thread.lock_img_path.connect(self.Ash_Lock_update)
        self.ash_thread.unlock_img_path.connect(self.Ash_Unlock_update)
        self.ash_thread.unlock_ad_path.connect(self.Ash_Unlock_Ad_update)
        self.ash_thread.charge_img_path.connect(self.Ash_Charge_updata)
        self.ash_thread.charge_ad_path.connect(self.Ash_Charge_Ad_update)
        self.ash_thread.wifi_img_path.connect(self.Ash_Wifi_update)
        self.ash_thread.wifi_ad_path.connect(self.Ash_Wifi_Ad_update)
        self.ash_thread.home_img_path.connect(self.Ash_Home_update)
        self.ash_thread.home_ad_path.connect(self.Ash_Home_Ad_update)
        self.ash_thread.timing_img_path.connect(self.Ash_Timing_update)
        self.ash_thread.timing_ad_path.connect(self.Ash_Timing_Ad_update)

        #连接按钮点击信号到buttonClicked方法
        line_apk_path = self.line_apkdir_path.installEventFilter(QEventHandler(self.line_apkdir_path))
        auto_path = self.auto_path.installEventFilter(QEventHandler(self.auto_path))
        ash_path = self.ash_auto_path.installEventFilter(QEventHandler(self.ash_auto_path))
        self.auto_path.setPlaceholderText("请拖入安装包获取路径开始操作")
        self.ash_auto_path.setPlaceholderText("请拖入安装包获取路径开始操作")
        self.select_online.clicked.connect(self.online_select_click)
        self.clean_online_text.clicked.connect(self.online_clean_click)
        self.select_ad.clicked.connect(self.ad_select_click)
        self.clean_ad_text.clicked.connect(self.ad_clean_click)
        self.select_ad_2.clicked.connect(self.ad_name_than)
        self.clean_ad_text_2.clicked.connect(self.ad_name_clean)
        self.mkdir_dir_2.clicked.connect(self.linetxt)
        self.scr1_2.clicked.connect(self.scra)
        self.scr2_2.clicked.connect(self.scrb)
        self.scr3_2.clicked.connect(self.scrc)
        self.scr4_2.clicked.connect(self.scrd)
        self.scr5_2.clicked.connect(self.scre)
        self.mkdir_name.clicked.connect(self.mk_dir_name)
        self.clear_dirtxt.clicked.connect(self.clear_dir_text)
        int_num = QIntValidator()
        int_num.setRange(1, 99999999)
        self.prid.setValidator(int_num)
        self.app_chan.setValidator(QRegExpValidator(QRegExp("[a-z]{12}")))
        self.option = QTextOption()
        self.option.setAlignment(Qt.AlignCenter)
        self.acition_auto.clicked.connect(self.auto_driver)
        self.clear_auto_path.clicked.connect(self.clear_Auto_text)
        self.ash_acition_auto.clicked.connect(self.Ash_Auto_Driver)
        self.ash_clear_auto_path.clicked.connect(self.Clear_Ash_Text)

    def Ash_Lock_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_lock_img.width(), self.ash_lock_img.height())
        # 展示图片，达到预览效果
        self.ash_lock_img.setPixmap(showImage)
        self.ash_lock_path.setText(text)

    def Ash_Unlock_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_unlock_img.width(), self.ash_unlock_img.height())
        # 展示图片，达到预览效果
        self.ash_unlock_img.setPixmap(showImage)
        self.ash_unlock_path.setText(text)

    def Ash_Unlock_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_unlock_ad_img.width(), self.ash_unlock_ad_img.height())
        # 展示图片，达到预览效果
        self.ash_unlock_ad_img.setPixmap(showImage)
        self.ash_unlock_ad_path.setText(text)

    def Ash_Charge_updata(self,text):
        showImage = QPixmap(text).scaled(self.ash_charge_img.width(), self.ash_charge_img.height())
        # 展示图片，达到预览效果
        self.ash_charge_img.setPixmap(showImage)
        self.ash_charge_path.setText(text)

    def Ash_Charge_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_charge_ad_img.width(), self.ash_charge_ad_img.height())
        # 展示图片，达到预览效果
        self.ash_charge_ad_img.setPixmap(showImage)
        self.ash_charge_ad_path.setText(text)

    def Ash_Wifi_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_wifi_img.width(), self.ash_wifi_img.height())
        # 展示图片，达到预览效果
        self.ash_wifi_img.setPixmap(showImage)
        self.ash_wifi_path.setText(text)

    def Ash_Wifi_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_wifi_ad_img.width(), self.ash_wifi_ad_img.height())
        # 展示图片，达到预览效果
        self.ash_wifi_ad_img.setPixmap(showImage)
        self.ash_wifi_ad_path.setText(text)

    def Ash_Home_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_home_img.width(), self.ash_home_img.height())
        # 展示图片，达到预览效果
        self.ash_home_img.setPixmap(showImage)
        self.ash_home_path.setText(text)

    def Ash_Home_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_home_ad_img.width(), self.ash_home_ad_img.height())
        # 展示图片，达到预览效果
        self.ash_home_ad_img.setPixmap(showImage)
        self.ash_home_ad_path.setText(text)

    def Ash_Timing_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_timing_img.width(), self.ash_timing_img.height())
        # 展示图片，达到预览效果
        self.ash_timing_img.setPixmap(showImage)
        self.ash_timing_path.setText(text)

    def Ash_Timing_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.ash_timming_ad_img.width(), self.ash_timming_ad_img.height())
        # 展示图片，达到预览效果
        self.ash_timming_ad_img.setPixmap(showImage)
        self.ash_timming_ad_path.setText(text)

    def Update_Ash_Cfg(self, text):
        self.ash_auto_info.append(text)

    def Ash_Auto_Driver(self):
        auto_path = self.ash_auto_path.text()
        self.ash_queue.put(auto_path)
        self.ash_thread.start()

    def Clear_Ash_Text(self):
        self.ash_auto_path.clear()

    def clear_Auto_text(self):
        self.auto_path.clear()

    def Lock_update(self,text):
        showImage = QPixmap(text).scaled(self.lock_img.width(), self.lock_img.height())
        # 展示图片，达到预览效果
        self.lock_img.setPixmap(showImage)
        self.lock_path.setText(text)

    def Unlock_update(self,text):
        showImage = QPixmap(text).scaled(self.unlock_img.width(), self.unlock_img.height())
        # 展示图片，达到预览效果
        self.unlock_img.setPixmap(showImage)
        self.unlock_path.setText(text)

    def Unlock_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.unlock_ad_img.width(), self.unlock_ad_img.height())
        # 展示图片，达到预览效果
        self.unlock_ad_img.setPixmap(showImage)
        self.unlock_ad_path.setText(text)

    def Charge_updata(self,text):
        showImage = QPixmap(text).scaled(self.charge_img.width(), self.charge_img.height())
        # 展示图片，达到预览效果
        self.charge_img.setPixmap(showImage)
        self.charge_path.setText(text)

    def Charge_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.charge_ad_img.width(), self.charge_ad_img.height())
        # 展示图片，达到预览效果
        self.charge_ad_img.setPixmap(showImage)
        self.charge_ad_path.setText(text)

    def Wifi_update(self,text):
        showImage = QPixmap(text).scaled(self.wifi_img.width(), self.wifi_img.height())
        # 展示图片，达到预览效果
        self.wifi_img.setPixmap(showImage)
        self.wifi_path.setText(text)

    def Wifi_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.wifi_ad_img.width(), self.wifi_ad_img.height())
        # 展示图片，达到预览效果
        self.wifi_ad_img.setPixmap(showImage)
        self.wifi_ad_path.setText(text)

    def Home_update(self,text):
        showImage = QPixmap(text).scaled(self.home_img.width(), self.home_img.height())
        # 展示图片，达到预览效果
        self.home_img.setPixmap(showImage)
        self.home_path.setText(text)

    def Home_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.home_ad_img.width(), self.home_ad_img.height())
        # 展示图片，达到预览效果
        self.home_ad_img.setPixmap(showImage)
        self.home_ad_path.setText(text)

    def Timing_update(self,text):
        showImage = QPixmap(text).scaled(self.timing_img.width(), self.timing_img.height())
        # 展示图片，达到预览效果
        self.timing_img.setPixmap(showImage)

        self.timing_path.setText(text)

    def Timing_Ad_update(self,text):
        showImage = QPixmap(text).scaled(self.timming_ad_img.width(), self.timming_ad_img.height())
        # 展示图片，达到预览效果
        self.timming_ad_img.setPixmap(showImage)
        self.timming_ad_path.setText(text)

    def updateAutoCfg(self, text):
        self.auto_info.append(text)

    def auto_driver(self):
        auto_path = self.auto_path.text()
        self.auto_queue.put(auto_path)
        self.auto_thread.start()

    def online_select_click(self):
        path = self.line_apkdir_path.text()
        self.queue.put(path)
        #点击按钮时启动工作线程
        self.thread.start()

    def updateSucCfg(self, text):
        self.suc_cfg.append(text)
        self.suc_cfg.document().setDefaultTextOption(self.option)

    def updateFailCfg(self, text):
        self.fail_cfg.append(text)
        self.fail_cfg.document().setDefaultTextOption(self.option)

    def online_clean_click(self):
        self.suc_cfg.clear()
        self.fail_cfg.clear()

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
                group_info = Ad_Sid.Ad_Group_Cfg(appid, pid, chan).ad_sid_select()
                all_info = Remove.remove_punctuation_and_replace(group_info[0])
                a_info = Remove.remove_punctuation_and_replace(group_info[1])
                b_info = Remove.remove_punctuation_and_replace(group_info[2])
                c_info = Remove.remove_punctuation_and_replace(group_info[3])
                if len(all_info)<1:
                    pass
                else:
                    self.all_text.setText(all_info)
                    self.all_text.document().setDefaultTextOption(self.option)
                if len(a_info)<1:
                    pass
                else:
                    self.A_text.setText(a_info)
                    self.A_text.document().setDefaultTextOption(self.option)
                if len(b_info)<1:
                    pass
                else:
                    self.B_text.setText(b_info)
                    self.B_text.document().setDefaultTextOption(self.option)
                if len(c_info)<1:
                    pass
                else:
                    self.C_text.setText(c_info)
                    self.C_text.document().setDefaultTextOption(self.option)
                adname = Ad_Name.Ad_Name_Cfg(appid,pid,chan).ad_name_select()
                splash_name = Remove.remove_punctuation_and_replace(adname[0])
                msg_name = Remove.remove_punctuation_and_replace(adname[1])
                plaque_name = Remove.remove_punctuation_and_replace(adname[2])
                video_name = Remove.remove_punctuation_and_replace(adname[3])
                if len(adname[0])<1:
                    pass
                else:
                    self.splash_cfg_text.setText(splash_name)
                    self.splash_cfg_text.document().setDefaultTextOption(self.option)
                if len(adname[1])<1:
                    pass
                else:
                    self.msg_cfg_text.setText(msg_name)
                    self.msg_cfg_text.document().setDefaultTextOption(self.option)
                if len(adname[2])<1:
                    pass
                else:
                    self.plaque_cfg_text.setText(plaque_name)
                    self.plaque_cfg_text.document().setDefaultTextOption(self.option)
                if len(adname[3])<1:
                    pass
                else:
                    self.video_cfg_text.setText(video_name)
                    self.video_cfg_text.document().setDefaultTextOption(self.option)
                adsid = Ad_Source.Ad_Sids_Cfg(appid, pid, chan).ad_sids_select()
                splash_sid = Remove.remove_punctuation_and_replace(adsid[0])
                msg_sid = Remove.remove_punctuation_and_replace(adsid[1])
                plaque_sid = Remove.remove_punctuation_and_replace(adsid[2])
                video_sid = Remove.remove_punctuation_and_replace(adsid[3])
                if len(adsid[0])<1:
                    pass
                else:
                    self.splash_source_text.setText(splash_sid)
                    self.splash_source_text.document().setDefaultTextOption(self.option)
                if len(adsid[1])<1:
                    pass
                else:
                    self.msg_source_text.setText(msg_sid)
                    self.msg_source_text.document().setDefaultTextOption(self.option)
                if len(adsid[2])<1:
                    pass
                else:
                    self.plaque_source_text.setText(plaque_sid)
                    self.plaque_source_text.document().setDefaultTextOption(self.option)
                if len(adsid[3])<1:
                    pass
                else:
                    self.video_source_text.setText(video_sid)
                    self.video_source_text.document().setDefaultTextOption(self.option)

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
                adthan = Ad_Contrast.Ad_Than_Cfg(appid, pid, chan, pro).ad_contrast_select()
                match = Remove.remove_punctuation_and_replace(adthan[0])
                short = Remove.remove_punctuation_and_replace(adthan[1])
                tmr = Remove.remove_punctuation_and_replace(adthan[2])
                self.match_text.setText(f"-----匹配的广告位-----\n{match}")
                self.match_text.document().setDefaultTextOption(self.option)
                if len(adthan[1]) < 1:
                    self.lack_text.setText('无缺少的广告位')
                    self.lack_text.document().setDefaultTextOption(self.option)
                else:
                    self.lack_text.setText(f"-----含有缺少的广告位-----\n{short}")
                    self.lack_text.document().setDefaultTextOption(self.option)
                if len(adthan[2]) < 1:
                    self.tmr_text.setText('无冗余的广告位')
                    self.tmr_text.document().setDefaultTextOption(self.option)
                else:
                    self.tmr_text.setText(f"-----含有冗余的广告位-----\n{tmr}")
                    self.tmr_text.document().setDefaultTextOption(self.option)
        except Exception as e:
            tips = QMessageBox(QMessageBox.Critical, '错误', f'程序错误:{e}')
            tips.exec_()

    def ad_name_clean(self):
        self.match_text.clear()
        self.tmr_text.clear()
        self.lack_text.clear()

    def linetxt(self):
        Mk_five_dirname.linetxt(self.dir_name_2.text())

    def scra(self):
        path = Screen_Img.scr(self.dir_name_2.text())
        showImage = QPixmap(path).scaled(self.img6.width(), self.img6.height())
        # 展示图片，达到预览效果
        self.img6.setPixmap(showImage)

    def scrb(self):
        path = Screen_Img.scr(self.dir_name_2.text())
        showImage = QPixmap(path).scaled(self.img2_2.width(), self.img2_2.height())
        # 展示图片，达到预览效果
        self.img2_2.setPixmap(showImage)

    def scrc(self):
        path = Screen_Img.scr(self.dir_name_2.text())
        showImage = QPixmap(path).scaled(self.img3_2.width(), self.img3_2.height())
        # 展示图片，达到预览效果
        self.img3_2.setPixmap(showImage)

    def scrd(self):
        path = Screen_Img.scr(self.dir_name_2.text())
        showImage = QPixmap(path).scaled(self.img4_2.width(), self.img4_2.height())
        # 展示图片，达到预览效果
        self.img4_2.setPixmap(showImage)

    def scre(self):
        path = Screen_Img.scr(self.dir_name_2.text())
        showImage = QPixmap(path).scaled(self.img5_2.width(), self.img5_2.height())
         # 展示图片，达到预览效果
        self.img5_2.setPixmap(showImage)

    def mk_dir_name(self):
        Mkdir_name.mk_dir_name(self.mkdir_txt.toPlainText())

    def clear_dir_text(self):
        self.mkdir_txt.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())