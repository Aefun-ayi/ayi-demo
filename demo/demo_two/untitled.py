# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(949, 851)
        Form.setMaximumSize(QtCore.QSize(949, 851))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Administrator/ad_online_merge/搜索_爱给网_aigei_com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1200, 891))
        self.tabWidget.setMinimumSize(QtCore.QSize(1200, 891))
        self.tabWidget.setMaximumSize(QtCore.QSize(1111, 891))
        self.tabWidget.setObjectName("tabWidget")
        self.online = QtWidgets.QWidget()
        self.online.setObjectName("online")
        self.line_apkdir_path = QtWidgets.QLineEdit(self.online)
        self.line_apkdir_path.setGeometry(QtCore.QRect(10, 40, 581, 71))
        self.line_apkdir_path.setStyleSheet("font: 14pt \"华文细黑\";")
        self.line_apkdir_path.setText("")
        self.line_apkdir_path.setObjectName("line_apkdir_path")
        self.label = QtWidgets.QLabel(self.online)
        self.label.setGeometry(QtCore.QRect(10, 10, 591, 31))
        self.label.setStyleSheet("font: 14pt \"幼圆\";")
        self.label.setObjectName("label")
        self.select_online = QtWidgets.QPushButton(self.online)
        self.select_online.setGeometry(QtCore.QRect(610, 10, 141, 101))
        self.select_online.setStyleSheet("font: 20pt \"幼圆\";\n"
"background-color: rgb(170, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/AeFun_script/test-demo/sscom.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_online.setIcon(icon1)
        self.select_online.setIconSize(QtCore.QSize(32, 32))
        self.select_online.setObjectName("select_online")
        self.suc_cfg = QtWidgets.QTextBrowser(self.online)
        self.suc_cfg.setGeometry(QtCore.QRect(500, 190, 371, 601))
        self.suc_cfg.setStyleSheet("font: 14pt \"幼圆\";")
        self.suc_cfg.setObjectName("suc_cfg")
        self.fail_cfg = QtWidgets.QTextBrowser(self.online)
        self.fail_cfg.setGeometry(QtCore.QRect(70, 190, 371, 601))
        self.fail_cfg.setStyleSheet("font: 14pt \"幼圆\";")
        self.fail_cfg.setObjectName("fail_cfg")
        self.label_3 = QtWidgets.QLabel(self.online)
        self.label_3.setGeometry(QtCore.QRect(230, 150, 41, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 14pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.online)
        self.label_4.setGeometry(QtCore.QRect(660, 150, 41, 31))
        self.label_4.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 14pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.clean_online_text = QtWidgets.QPushButton(self.online)
        self.clean_online_text.setGeometry(QtCore.QRect(780, 10, 141, 101))
        self.clean_online_text.setStyleSheet("font: 20pt \"幼圆\";\n"
"background-color: rgb(170, 170, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/ico储存/厕洗卫设备-垃圾桶-1_爱给网_aigei_com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clean_online_text.setIcon(icon2)
        self.clean_online_text.setIconSize(QtCore.QSize(32, 32))
        self.clean_online_text.setObjectName("clean_online_text")
        self.label_5 = QtWidgets.QLabel(self.online)
        self.label_5.setGeometry(QtCore.QRect(790, 120, 121, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.online, "")
        self.adcfg = QtWidgets.QWidget()
        self.adcfg.setObjectName("adcfg")
        self.label_2 = QtWidgets.QLabel(self.adcfg)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label_2.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_2.setObjectName("label_2")
        self.prid = QtWidgets.QLineEdit(self.adcfg)
        self.prid.setGeometry(QtCore.QRect(90, 20, 141, 31))
        self.prid.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.prid.setObjectName("prid")
        self.app_chan = QtWidgets.QLineEdit(self.adcfg)
        self.app_chan.setGeometry(QtCore.QRect(380, 20, 141, 31))
        self.app_chan.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.app_chan.setObjectName("app_chan")
        self.label_6 = QtWidgets.QLabel(self.adcfg)
        self.label_6.setGeometry(QtCore.QRect(330, 20, 54, 31))
        self.label_6.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_6.setObjectName("label_6")
        self.all_text = QtWidgets.QTextBrowser(self.adcfg)
        self.all_text.setGeometry(QtCore.QRect(20, 100, 211, 161))
        self.all_text.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.all_text.setObjectName("all_text")
        self.select_ad = QtWidgets.QPushButton(self.adcfg)
        self.select_ad.setGeometry(QtCore.QRect(590, 10, 111, 51))
        self.select_ad.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 24pt \"幼圆\";")
        self.select_ad.setIcon(icon1)
        self.select_ad.setIconSize(QtCore.QSize(24, 24))
        self.select_ad.setObjectName("select_ad")
        self.clean_ad_text = QtWidgets.QPushButton(self.adcfg)
        self.clean_ad_text.setGeometry(QtCore.QRect(720, 10, 111, 51))
        self.clean_ad_text.setStyleSheet("color: rgb(255, 255, 127);\n"
"background-color: rgb(140, 0, 0);\n"
"font: 24pt \"幼圆\";")
        self.clean_ad_text.setIcon(icon2)
        self.clean_ad_text.setIconSize(QtCore.QSize(24, 24))
        self.clean_ad_text.setObjectName("clean_ad_text")
        self.A_text = QtWidgets.QTextBrowser(self.adcfg)
        self.A_text.setGeometry(QtCore.QRect(250, 100, 211, 161))
        self.A_text.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.A_text.setObjectName("A_text")
        self.B_text = QtWidgets.QTextBrowser(self.adcfg)
        self.B_text.setGeometry(QtCore.QRect(480, 100, 211, 161))
        self.B_text.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.B_text.setObjectName("B_text")
        self.C_text = QtWidgets.QTextBrowser(self.adcfg)
        self.C_text.setGeometry(QtCore.QRect(710, 100, 211, 161))
        self.C_text.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.C_text.setObjectName("C_text")
        self.label_7 = QtWidgets.QLabel(self.adcfg)
        self.label_7.setGeometry(QtCore.QRect(90, 70, 121, 21))
        self.label_7.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.adcfg)
        self.label_8.setGeometry(QtCore.QRect(300, 70, 161, 21))
        self.label_8.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.adcfg)
        self.label_9.setGeometry(QtCore.QRect(520, 70, 171, 21))
        self.label_9.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.adcfg)
        self.label_10.setGeometry(QtCore.QRect(750, 70, 151, 21))
        self.label_10.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_10.setObjectName("label_10")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.adcfg)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 270, 1101, 621))
        self.tabWidget_2.setMinimumSize(QtCore.QSize(1101, 0))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(1101, 621))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 201, 21))
        self.label_11.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_11.setObjectName("label_11")
        self.splash_cfg_text = QtWidgets.QTextBrowser(self.tab)
        self.splash_cfg_text.setGeometry(QtCore.QRect(10, 40, 211, 481))
        self.splash_cfg_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.splash_cfg_text.setObjectName("splash_cfg_text")
        self.msg_cfg_text = QtWidgets.QTextBrowser(self.tab)
        self.msg_cfg_text.setGeometry(QtCore.QRect(240, 40, 211, 481))
        self.msg_cfg_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.msg_cfg_text.setObjectName("msg_cfg_text")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(250, 10, 201, 21))
        self.label_12.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_12.setObjectName("label_12")
        self.plaque_cfg_text = QtWidgets.QTextBrowser(self.tab)
        self.plaque_cfg_text.setGeometry(QtCore.QRect(470, 40, 211, 481))
        self.plaque_cfg_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.plaque_cfg_text.setObjectName("plaque_cfg_text")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(480, 10, 201, 21))
        self.label_13.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_13.setObjectName("label_13")
        self.video_cfg_text = QtWidgets.QTextBrowser(self.tab)
        self.video_cfg_text.setGeometry(QtCore.QRect(700, 40, 211, 481))
        self.video_cfg_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.video_cfg_text.setObjectName("video_cfg_text")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(710, 10, 201, 21))
        self.label_14.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_14.setObjectName("label_14")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.splash_source_text = QtWidgets.QTextBrowser(self.tab_2)
        self.splash_source_text.setGeometry(QtCore.QRect(10, 40, 211, 481))
        self.splash_source_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.splash_source_text.setObjectName("splash_source_text")
        self.plaque_source_text = QtWidgets.QTextBrowser(self.tab_2)
        self.plaque_source_text.setGeometry(QtCore.QRect(470, 40, 211, 481))
        self.plaque_source_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.plaque_source_text.setObjectName("plaque_source_text")
        self.msg_source_text = QtWidgets.QTextBrowser(self.tab_2)
        self.msg_source_text.setGeometry(QtCore.QRect(240, 40, 211, 481))
        self.msg_source_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.msg_source_text.setObjectName("msg_source_text")
        self.video_source_text = QtWidgets.QTextBrowser(self.tab_2)
        self.video_source_text.setGeometry(QtCore.QRect(700, 40, 211, 481))
        self.video_source_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.video_source_text.setObjectName("video_source_text")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 201, 21))
        self.label_15.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(250, 10, 201, 21))
        self.label_16.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(710, 10, 201, 21))
        self.label_17.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(480, 10, 201, 21))
        self.label_18.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_18.setObjectName("label_18")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.label_21 = QtWidgets.QLabel(self.adcfg)
        self.label_21.setGeometry(QtCore.QRect(100, 0, 54, 12))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.adcfg, "")
        self.than_cfg = QtWidgets.QWidget()
        self.than_cfg.setObjectName("than_cfg")
        self.label_19 = QtWidgets.QLabel(self.than_cfg)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.label_19.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_19.setObjectName("label_19")
        self.prid_2 = QtWidgets.QLineEdit(self.than_cfg)
        self.prid_2.setGeometry(QtCore.QRect(90, 30, 191, 31))
        self.prid_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.prid_2.setObjectName("prid_2")
        self.label_20 = QtWidgets.QLabel(self.than_cfg)
        self.label_20.setGeometry(QtCore.QRect(310, 30, 54, 31))
        self.label_20.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_20.setObjectName("label_20")
        self.app_chan_2 = QtWidgets.QLineEdit(self.than_cfg)
        self.app_chan_2.setGeometry(QtCore.QRect(370, 30, 171, 31))
        self.app_chan_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.app_chan_2.setObjectName("app_chan_2")
        self.select_ad_2 = QtWidgets.QPushButton(self.than_cfg)
        self.select_ad_2.setGeometry(QtCore.QRect(550, 10, 171, 111))
        self.select_ad_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 24pt \"幼圆\";")
        self.select_ad_2.setIcon(icon1)
        self.select_ad_2.setIconSize(QtCore.QSize(24, 24))
        self.select_ad_2.setObjectName("select_ad_2")
        self.clean_ad_text_2 = QtWidgets.QPushButton(self.than_cfg)
        self.clean_ad_text_2.setGeometry(QtCore.QRect(750, 10, 161, 111))
        self.clean_ad_text_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"background-color: rgb(140, 0, 0);\n"
"font: 24pt \"幼圆\";")
        self.clean_ad_text_2.setIcon(icon2)
        self.clean_ad_text_2.setIconSize(QtCore.QSize(24, 24))
        self.clean_ad_text_2.setObjectName("clean_ad_text_2")
        self.lack_text = QtWidgets.QTextBrowser(self.than_cfg)
        self.lack_text.setGeometry(QtCore.QRect(340, 240, 261, 551))
        self.lack_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.lack_text.setObjectName("lack_text")
        self.match_text = QtWidgets.QTextBrowser(self.than_cfg)
        self.match_text.setGeometry(QtCore.QRect(40, 240, 261, 551))
        self.match_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.match_text.setObjectName("match_text")
        self.tmr_text = QtWidgets.QTextBrowser(self.than_cfg)
        self.tmr_text.setGeometry(QtCore.QRect(640, 240, 261, 551))
        self.tmr_text.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.tmr_text.setObjectName("tmr_text")
        self.label_22 = QtWidgets.QLabel(self.than_cfg)
        self.label_22.setGeometry(QtCore.QRect(70, 190, 241, 41))
        self.label_22.setStyleSheet("font: 16pt \"幼圆\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.than_cfg)
        self.label_23.setGeometry(QtCore.QRect(380, 190, 231, 41))
        self.label_23.setStyleSheet("font: 16pt \"幼圆\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.than_cfg)
        self.label_24.setGeometry(QtCore.QRect(680, 190, 221, 41))
        self.label_24.setStyleSheet("font: 16pt \"幼圆\";")
        self.label_24.setObjectName("label_24")
        self.package_info = QtWidgets.QLineEdit(self.than_cfg)
        self.package_info.setGeometry(QtCore.QRect(110, 70, 431, 41))
        self.package_info.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.package_info.setText("")
        self.package_info.setObjectName("package_info")
        self.label_25 = QtWidgets.QLabel(self.than_cfg)
        self.label_25.setGeometry(QtCore.QRect(10, 70, 101, 41))
        self.label_25.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.than_cfg, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.app_id = QtWidgets.QLineEdit(self.tab_3)
        self.app_id.setGeometry(QtCore.QRect(100, 40, 121, 31))
        self.app_id.setStyleSheet("font: 14pt \"幼圆\";")
        self.app_id.setObjectName("app_id")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(20, 40, 71, 31))
        self.label_26.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(250, 40, 61, 31))
        self.label_27.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_27.setObjectName("label_27")
        self.app_chanl = QtWidgets.QLineEdit(self.tab_3)
        self.app_chanl.setGeometry(QtCore.QRect(320, 40, 121, 31))
        self.app_chanl.setStyleSheet("font: 14pt \"幼圆\";")
        self.app_chanl.setObjectName("app_chanl")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(470, 40, 111, 31))
        self.label_28.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_28.setObjectName("label_28")
        self.apk_version = QtWidgets.QLineEdit(self.tab_3)
        self.apk_version.setGeometry(QtCore.QRect(590, 40, 121, 31))
        self.apk_version.setStyleSheet("font: 14pt \"幼圆\";")
        self.apk_version.setObjectName("apk_version")
        self.test_ment = QtWidgets.QPushButton(self.tab_3)
        self.test_ment.setGeometry(QtCore.QRect(740, 40, 75, 41))
        self.test_ment.setObjectName("test_ment")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 40, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(210, 100, 571, 641))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询配置"))
        self.label.setText(_translate("Form", "拖入出包文件夹生成路径（注意路径不可带中文）："))
        self.select_online.setText(_translate("Form", "查询"))
        self.fail_cfg.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Form", "失败"))
        self.label_4.setText(_translate("Form", "通过"))
        self.clean_online_text.setText(_translate("Form", "清空"))
        self.label_5.setText(_translate("Form", "清空失败、通过的信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.online), _translate("Form", "查询在线配置"))
        self.label_2.setText(_translate("Form", "项目id："))
        self.label_6.setText(_translate("Form", "渠道："))
        self.select_ad.setText(_translate("Form", "查询"))
        self.clean_ad_text.setText(_translate("Form", "清空"))
        self.label_7.setText(_translate("Form", "all分组："))
        self.label_8.setText(_translate("Form", "1066A_A分组："))
        self.label_9.setText(_translate("Form", "1066B_B分组："))
        self.label_10.setText(_translate("Form", "1066C_C分组："))
        self.label_11.setText(_translate("Form", "已配置的开屏广告位："))
        self.label_12.setText(_translate("Form", "已配置的信息流广告位："))
        self.label_13.setText(_translate("Form", "已配置的插屏广告位："))
        self.label_14.setText(_translate("Form", "已配置的视频广告位："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Form", "广告位"))
        self.label_15.setText(_translate("Form", "已配置的开屏广告源："))
        self.label_16.setText(_translate("Form", "已配置的信息流广告源："))
        self.label_17.setText(_translate("Form", "已配置的视频广告源："))
        self.label_18.setText(_translate("Form", "已配置的插屏广告源："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "广告源"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adcfg), _translate("Form", "查询广告配置"))
        self.label_19.setText(_translate("Form", "项目id："))
        self.label_20.setText(_translate("Form", "渠道："))
        self.select_ad_2.setText(_translate("Form", "查询"))
        self.clean_ad_text_2.setText(_translate("Form", "清空"))
        self.label_22.setText(_translate("Form", "匹配的广告位"))
        self.label_23.setText(_translate("Form", "缺少的广告位"))
        self.label_24.setText(_translate("Form", "冗余的广告位"))
        self.label_25.setText(_translate("Form", "出包备注："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.than_cfg), _translate("Form", "确认广告配置"))
        self.label_26.setText(_translate("Form", "App_id"))
        self.label_27.setText(_translate("Form", "chanl"))
        self.label_28.setText(_translate("Form", "Apk_version"))
        self.test_ment.setText(_translate("Form", "测试环境"))
        self.pushButton_2.setText(_translate("Form", "正式环境"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "页"))
