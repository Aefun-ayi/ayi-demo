import datetime
import uiautomator2 as u2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import check_cfg_frame
from event_handler import QEventHandler
from PyQt5.QtWidgets import QMessageBox
from queue import Queue
from Worker_run import Worker
import Remove
import Ad_Sid
import Ad_Name
import Ad_Source
import Ad_Contrast
import os

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
                if len(a_info)<1:
                    pass
                else:
                    self.A_text.setText(a_info)
                if len(b_info)<1:
                    pass
                else:
                    self.B_text.setText(b_info)
                if len(c_info)<1:
                    pass
                else:
                    self.C_text.setText(c_info)
                adname = Ad_Name.Ad_Name_Cfg(appid,pid,chan).ad_name_select()
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
                adsid = Ad_Source.Ad_Sids_Cfg(appid, pid, chan).ad_sids_select()
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
                adthan = Ad_Contrast.Ad_Than_Cfg(appid, pid, chan, pro).ad_contrast_select()
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

    def linetxt(self):
        dir_name = self.dir_name_2.text()
        dir_path = dir_name.replace('	','_')
        isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            path = os.makedirs(fr'D:\keep\五图截图\{dir_path}')
            msg_box = QMessageBox(QMessageBox.Information, '提示', fr'D:\keep\五图截图\{dir_path}' + ' 创建成功')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录已存在')
            msg_box.exec_()
            # 如果目录存在则不创建，并提示目录已存在

    def scra(self):
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect()
        except RuntimeError as run:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
            msg_box.exec_()
        dir_name = self.dir_name_2.text()
        # 判断输入为空处理
        if dir_name =='':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
            msg_box.exec_()
        else:
            # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
            dir_path = dir_name.replace('	', '_')
            isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
            # 进入判断是否存在这个文件夹
            if isExists:
                # 时间戳
                filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
                # 截图路径
                path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-1.png")
                # 展示图片时根据label的尺寸调整大小
                showImage = QPixmap(path).scaled(self.img6.width(), self.img6.height())
                # 展示图片，达到预览效果
                self.img6.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def scrb(self):
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect()
        except RuntimeError as run:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
            msg_box.exec_()
        dir_name = self.dir_name_2.text()
        # 判断输入为空处理
        if dir_name =='':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
            msg_box.exec_()
        else:
            # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
            dir_path = dir_name.replace('	', '_')
            isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
            # 进入判断是否存在这个文件夹
            if isExists:
                # 时间戳
                filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
                # 截图路径
                path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-2.png")
                # 展示图片时根据label的尺寸调整大小
                showImage = QPixmap(path).scaled(self.img2_2.width(), self.img2_2.height())
                # 展示图片，达到预览效果
                self.img2_2.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def scrc(self):
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect()
        except RuntimeError as run:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
            msg_box.exec_()
        dir_name = self.dir_name_2.text()
        # 判断输入为空处理
        if dir_name =='':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
            msg_box.exec_()
        else:
            # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
            dir_path = dir_name.replace('	', '_')
            isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
            # 进入判断是否存在这个文件夹
            if isExists:
                # 时间戳
                filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
                # 截图路径
                path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-3.png")
                # 展示图片时根据label的尺寸调整大小
                showImage = QPixmap(path).scaled(self.img3_2.width(), self.img3_2.height())
                # 展示图片，达到预览效果
                self.img3_2.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def scrd(self):
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect()
        except RuntimeError as run:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
            msg_box.exec_()
        dir_name = self.dir_name_2.text()
        # 判断输入为空处理
        if dir_name =='':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
            msg_box.exec_()
        else:
            # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
            dir_path = dir_name.replace('	', '_')
            isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
            # 进入判断是否存在这个文件夹
            if isExists:
                # 时间戳
                filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
                # 截图路径
                path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-4.png")
                # 展示图片时根据label的尺寸调整大小
                showImage = QPixmap(path).scaled(self.img4_2.width(), self.img4_2.height())
                # 展示图片，达到预览效果
                self.img4_2.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def scre(self):
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect()
        except RuntimeError as run:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
            msg_box.exec_()
        dir_name = self.dir_name_2.text()
        # 判断输入为空处理
        if dir_name =='':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
            msg_box.exec_()
        else:
            # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
            dir_path = dir_name.replace('	', '_')
            isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
            # 进入判断是否存在这个文件夹
            if isExists:
                # 时间戳
                filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
                # 截图路径
                path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-5.png")
                # 展示图片时根据label的尺寸调整大小
                showImage = QPixmap(path).scaled(self.img5_2.width(), self.img5_2.height())
                # 展示图片，达到预览效果
                self.img5_2.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def mk_dir_name(self):
        a = self.mkdir_txt.toPlainText()
        info_list = a.split('\n')
        project_name = info_list[1]
        chan = info_list[2]
        prid = info_list[3]
        de_channl = info_list[4]
        packageinfo = info_list[7] + info_list[8] + info_list[9]
        want = info_list[-2]
        now = datetime.datetime.now()
        date = now.strftime('%m')
        pro_date = now.strftime('%m%d-%H-%M')
        isExists = os.path.exists(fr'D:\keep\公用-储存安装包\{date}_moon')
        # 进入判断是否存在这个文件夹
        if not isExists:
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon')
            msg_box = QMessageBox(QMessageBox.Information, '提示', fr'D:\keep\公用-储存安装包\{date}_moon' + ' 创建成功')
            msg_box.exec_()
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}')
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}\{prid}')
            want_file = fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}\{prid}\{chan}' + '.txt'
            file = open(want_file, 'w')
            file.write('投放渠道：' + str(de_channl) + '\n出包需求：' + str(want) + '\n打包参数：' + str(packageinfo))  # 写入出包需求
            mmm_box = QMessageBox(QMessageBox.Information, '提示', fr'项目id：{prid}  产品名称{project_name}  产品需求：{want} 创建成功')
            mmm_box.exec_()
        else:
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}')
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}\{prid}')
            want_file = fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}\{prid}\{chan}'+ '.txt'
            file = open(want_file, 'w')
            file.write('投放渠道：' + str(de_channl) + '\n出包需求：' + str(want) + '\n打包参数：' + str(packageinfo))  # 写入出包需求
            mmm_box = QMessageBox(QMessageBox.Information, '提示', fr'项目id：{prid}  产品名称{project_name}  产品需求：{want} 创建成功')
            mmm_box.exec_()

    def clear_dir_text(self):
        self.mkdir_txt.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())