import untitled
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import os
import requests
import re
import Remove
import ttt_ad_config
import tta_ad_config
import ttt_online_config
import tta_online_config



class Main():


    def ttt_test(self):
        appid = ui.app_id.text()
        cha = ui.chan.text()
        apk_version = ui.apk_version.text()
        track_channel = ui.track_channel.currentText()
        ttt_cfg = ttt_online_config.ttt_test(appid,cha,apk_version,track_channel)
        remove_match_douhao = re.sub(',', '\n', str(ttt_cfg)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
        remove_match_danyinhao = remove_match_douhao.replace("'", '')
        ttt = remove_match_danyinhao.replace(' ', '')
        ui.ttt_def_info.setText(ttt)

    def tta_release(self):
        appid = ui.app_id.text()
        cha = ui.chan.text()
        apk_version = ui.apk_version.text()
        track_channel = ui.track_channel.currentText()
        tta_cfg = tta_online_config.tta_release(appid,cha,apk_version,track_channel)
        remove_match_douhao = re.sub(',', '\n', str(tta_cfg)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
        remove_match_danyinhao = remove_match_douhao.replace("'", '')
        tta = remove_match_danyinhao.replace(' ', '')
        ui.tta_def_info.setText(tta)

    def claer_project_info(self):
        ui.app_id.clear()
        ui.chan.clear()
        ui.apk_version.clear()

    def clear_on_txt(self):
        ui.tta_def_info.clear()
        ui.ttt_def_info.clear()

    def clear_ad_txt(self):
        ui.ttt_splash_name.clear()
        ui.ttt_splash_source.clear()
        ui.ttt_plaque_name.clear()
        ui.ttt_plaque_source.clear()
        ui.ttt_msg_name.clear()
        ui.ttt_msg_source.clear()
        ui.ttt_video_name.clear()
        ui.ttt_video_source.clear()
        ui.tta_splash_name.clear()
        ui.tta_splash_source.clear()
        ui.tta_plaque_name.clear()
        ui.tta_plaque_source.clear()
        ui.tta_video_name.clear()
        ui.tta_video_source.clear()
        ui.tta_msg_name.clear()
        ui.tta_msg_source.clear()

    def ttt_ad(self):
        appid = ui.app_id.text()
        out_pack = ui.out_pack_info.text()
        new_old = '待替换'
        peop = ui.new_old.currentText()
        if peop == '新用户':
            new_or_old = new_old.replace('待替换','1')
        if peop == '老用户':
            new_or_old = new_old.replace('待替换','2')
        tttad = ttt_ad_config.ttt_ad(new_or_old,appid,out_pack)
        if out_pack != '':
            if appid !='':
                splash_name_info = Remove.remove_punctuation_and_replace(tttad[0])
                ui.ttt_splash_name.setText(splash_name_info)
                video_name_info = Remove.remove_punctuation_and_replace(tttad[2])
                ui.ttt_video_name.setText(video_name_info)
                msg_name_info = Remove.remove_punctuation_and_replace(tttad[4])
                ui.ttt_msg_name.setText(msg_name_info)
                plaque_name_info = Remove.remove_punctuation_and_replace(tttad[6])
                ui.ttt_plaque_name.setText(plaque_name_info)

                splash_source_info = Remove.remove_punctuation_and_replace(tttad[1])
                ui.ttt_splash_source.setText(splash_source_info)
                video_source_info = Remove.remove_punctuation_and_replace(tttad[3])
                ui.ttt_video_source.setText(video_source_info)
                plaque_source_info = Remove.remove_punctuation_and_replace(tttad[7])
                ui.ttt_plaque_source.setText(plaque_source_info)
                msg_source_info = Remove.remove_punctuation_and_replace(tttad[5])
                ui.ttt_msg_source.setText(msg_source_info)


    def tta_ad(self):
        appid = ui.app_id.text()
        out_pack = ui.out_pack_info.text()
        new_old = '待替换'
        peop = ui.new_old.currentText()
        if peop == '新用户':
            new_or_old = new_old.replace('待替换','1')
        if peop == '老用户':
            new_or_old = new_old.replace('待替换','2')
        ttaad = tta_ad_config.tta_ad(new_or_old,appid,out_pack)

        splash_name_info = Remove.remove_punctuation_and_replace(ttaad[0])
        ui.tta_splash_name.setText(splash_name_info)
        video_name_info = Remove.remove_punctuation_and_replace(ttaad[2])
        ui.tta_video_name.setText(video_name_info)
        msg_name_info = Remove.remove_punctuation_and_replace(ttaad[4])
        ui.tta_msg_name.setText(msg_name_info)
        plaque_name_info = Remove.remove_punctuation_and_replace(ttaad[6])
        ui.tta_plaque_name.setText(plaque_name_info)

        splash_source_info = Remove.remove_punctuation_and_replace(ttaad[1])
        ui.tta_splash_source.setText(splash_source_info)
        video_source_info = Remove.remove_punctuation_and_replace(ttaad[3])
        ui.tta_video_source.setText(video_source_info)
        plaque_source_info = Remove.remove_punctuation_and_replace(ttaad[7])
        ui.tta_plaque_source.setText(plaque_source_info)
        msg_source_info = Remove.remove_punctuation_and_replace(ttaad[5])
        ui.tta_msg_source.setText(msg_source_info)


if __name__ == '__main__':
    # 初始化数据
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.ttt_on_button.clicked.connect(Main.ttt_test)
    ui.tta_on_button.clicked.connect(Main.tta_release)
    ui.clear_on_button.clicked.connect(Main.clear_on_txt)
    ui.ttt_ad_button.clicked.connect(Main.ttt_ad)
    ui.tta_ad_button.clicked.connect(Main.tta_ad)
    ui.clear_ad_txt.clicked.connect(Main.clear_ad_txt)
    ui.clear_project.clicked.connect(Main.claer_project_info)
    sys.exit(app.exec_())

