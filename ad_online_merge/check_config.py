import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import *
# from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import check_cfg_frame
from event_handler import QEventHandler
import path_list
from apk_object import apk
from Pattern_Test import Pattern_API
import re
import base64
import json
import requests
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QProgressDialog
import rule_ad_name
import datetime
import uiautomator2 as u2


class Main():

    def online_select_click():
        path = ui.line_apkdir_path.text()
        os_p = path_list.system()
        for i in list(os_p.get_dirs_ptha(fr"{path}")):
            a = apk(i)
            a.set_AppInof(i)
            t = Pattern_API(a)
            update_lose = str(t.testms()[0])
            # print(update_lose)
            update_pass = str(t.testms()[1])
            # print(update_pass)
            remove_douhao_lose = re.sub(r',', '\n', update_lose[1:-1])
            remove_danyinhao_lose = remove_douhao_lose.replace("'", '')
            keep_otc_lose = remove_danyinhao_lose.replace('"', '')
            remove_douhao_pass = re.sub(r',', '\n', update_pass[1:-1])
            remove_danyinhao_pass = remove_douhao_pass.replace("'", '')
            keep_otc_pass = remove_danyinhao_pass.replace('"', '')
            ui.suc_cfg.append(f'项目id：{a.pid} \n渠道：{a.cha} \n{keep_otc_pass}\n----------------------------------\n')
            ui.fail_cfg.append(f'项目id：{a.pid} \n渠道：{a.cha} \n{keep_otc_lose}\n----------------------------------\n')
            option = QTextOption()
            option.setAlignment(Qt.AlignCenter)
            ui.suc_cfg.document().setDefaultTextOption(option)
            ui.fail_cfg.document().setDefaultTextOption(option)

    def online_clean_click():
        ui.suc_cfg.clear()
        ui.fail_cfg.clear()

    def ad_select_click():
        try:
            pid = ui.prid.text()

            chan = ui.app_chan.text()
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
                sids = ['all', '1066A_A', '1066B_B', '1066C_C']  # 把目前在用的4个分组放在列表

                for i in sids:  # 对列表进行循环，列表内每一个分组的值进行输出
                    txt = '{"buy_id":"default",' \
                          '"imei":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                          f'"pid":"{pid}",' \
                          f'"sid":"{i}",' \
                          '"lsn":"85202900",' \
                          f'"appid":"{appid}",' \
                          '"isNewUser":"1",' \
                          '"brand":"HUAWEI",' \
                          '"os_version":"ele-al00 10.1.0.162(c00e160r2p11)",' \
                          '"debug":"1",' \
                          '"oaid":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                          f'"cha_id":"{chan}",' \
                          '"buy_act":"default",' \
                          '"os":"EmotionUI_12.0.0"}'
                    s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义

                    code = base64.b64encode(s).decode("utf-8")

                    url = f'https://cfg.vigame.cn/v14/extend?value={code}'

                    http_get = requests.get(url)

                    connect = http_get.json()

                    jdict = json.dumps(connect)

                    stra_name = r'"strategy": ".+?"'
                    gecheng = r'"autoOpt": .+'
                    fenzu = r'"sid": ".+?"'

                    gm = re.findall(gecheng, jdict)
                    fm = re.findall(fenzu, str(gm))

                    m = re.findall(stra_name, jdict)

                    a_group = []
                    b_group = []
                    c_group = []
                    all_group = []

                    # 加上分组判断 按照分组输出对应的分组内的策略信息
                    if "1066C_C" in str(fm):
                        for ii in range(len(m)):
                            c_group.append(m[ii][13:-1])
                            str_c_group = str(c_group)
                            remove_douhao = re.sub(r',', '\n', str_c_group[1:-1])
                            remove_danyinhao = remove_douhao.replace("'", '')
                            keep_otc_c_group = remove_danyinhao.replace('"', '')
                            ui.C_text.setPlainText(keep_otc_c_group)
                            option = QTextOption()
                            option.setAlignment(Qt.AlignCenter)
                            ui.C_text.document().setDefaultTextOption(option)

                    if "1066B_B" in str(fm):
                        for ii in range(len(m)):
                            b_group.append(m[ii][13:-1])
                            str_b_group = str(b_group)
                            remove_douhao = re.sub(r',', '\n', str_b_group[1:-1])
                            remove_danyinhao = remove_douhao.replace("'", '')
                            keep_otc_b_group = remove_danyinhao.replace('"', '')
                            ui.B_text.setPlainText(keep_otc_b_group)
                            option = QTextOption()
                            option.setAlignment(Qt.AlignCenter)
                            ui.B_text.document().setDefaultTextOption(option)

                    if "1066A_A" in str(fm):
                        for ii in range(len(m)):
                            a_group.append(m[ii][13:-1])
                            str_a_group = str(a_group)
                            remove_douhao = re.sub(r',', '\n', str_a_group[1:-1])
                            remove_danyinhao = remove_douhao.replace("'", '')
                            keep_otc_a_group = remove_danyinhao.replace('"', '')
                            ui.A_text.setPlainText(keep_otc_a_group)
                            option = QTextOption()
                            option.setAlignment(Qt.AlignCenter)
                            ui.A_text.document().setDefaultTextOption(option)

                    if "all" in str(fm):
                        for ii in range(len(m)):
                            all_group.append(m[ii][13:-1])
                            str_all_group = str(all_group)
                            remove_douhao = re.sub(r',', '\n', str_all_group[1:-1])
                            remove_danyinhao = remove_douhao.replace("'", '')
                            keep_otc_all_group = remove_danyinhao.replace('"', '')
                            ui.all_text.setPlainText(keep_otc_all_group)
                            option = QTextOption()
                            option.setAlignment(Qt.AlignCenter)
                            ui.all_text.document().setDefaultTextOption(option)

                    list_strate = connect["strategys"]  # 获取分组内的策略信息
                    ad_name = connect["adPositions"]  # 获取分组内策略里面的广告位信息
                    msg_config = []
                    video_config = []
                    plaque_config = []
                    splash_config = []

                    # 利用分组内的策略名和广告位所配置的策略名对比 一致后输出正确有效的广告位
                    for iii in range(len(list_strate)):
                        for index in range(len(ad_name)):
                            if list_strate[iii]['name'] in ad_name[index]['strategys']:
                                if 'msg' in ad_name[index]['strategys']:
                                    msg_config.append(ad_name[index]['name'])
                                    remove_douhao_msg = re.sub(r',', '\n',str(msg_config)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                    remove_danyinhao_msg = remove_douhao_msg.replace("'", '')
                                    keep_otc_msg = remove_danyinhao_msg.replace(' ', '')
                                    ui.msg_cfg_text.setPlainText(keep_otc_msg)
                                    option = QTextOption()
                                    option.setAlignment(Qt.AlignCenter)
                                    ui.msg_cfg_text.document().setDefaultTextOption(option)

                                if 'video' in ad_name[index]['strategys']:
                                    video_config.append(ad_name[index]['name'])
                                    remove_douhao_video = re.sub(r',', '\n',str(video_config)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                    remove_danyinhao_video = remove_douhao_video.replace("'", '')
                                    keep_otc_video = remove_danyinhao_video.replace(' ', '')
                                    ui.video_cfg_text.setPlainText(keep_otc_video)
                                    option = QTextOption()
                                    option.setAlignment(Qt.AlignCenter)
                                    ui.video_cfg_text.document().setDefaultTextOption(option)

                                if 'plaque' in ad_name[index]['strategys']:
                                    plaque_config.append(ad_name[index]['name'])
                                    remove_douhao_plaque = re.sub(r',', '\n',str(plaque_config)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                    remove_danyinhao_plaque = remove_douhao_plaque.replace("'", '')
                                    keep_otc_plaque = remove_danyinhao_plaque.replace(' ', '')
                                    ui.plaque_cfg_text.setPlainText(keep_otc_plaque)
                                    option = QTextOption()
                                    option.setAlignment(Qt.AlignCenter)
                                    ui.plaque_cfg_text.document().setDefaultTextOption(option)

                                if 'splash' in ad_name[index]['strategys']:
                                    splash_config.append(ad_name[index]['name'])
                                    remove_douhao_splash = re.sub(r',', '\n',str(splash_config)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                    remove_danyinhao_splash = remove_douhao_splash.replace("'", '')
                                    keep_otc_splash = remove_danyinhao_splash.replace(' ', '')
                                    ui.splash_cfg_text.setPlainText(keep_otc_splash)
                                    option = QTextOption()
                                    option.setAlignment(Qt.AlignCenter)
                                    ui.splash_cfg_text.document().setDefaultTextOption(option)

                    msg_sid = []
                    video_sid = []
                    plaque_sid = []
                    splash_sid = []

                    for i in range(len(list_strate)):
                        all_source = list_strate[i]
                        for ii in range(len(all_source['sids'])):
                            if '_msg' in all_source['sids'][ii]:
                                msg_source = all_source['sids'][ii]
                                msg_sid.append(msg_source)
                                remove_msg_douhao = re.sub(r',', '\n', str(msg_sid)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                remove_msg_danyinhao = remove_msg_douhao.replace("'", '')
                                msg_sources = remove_msg_danyinhao.replace(' ', '')
                                ui.msg_source_text.setPlainText(msg_sources)
                                option = QTextOption()
                                option.setAlignment(Qt.AlignCenter)
                                ui.msg_source_text.document().setDefaultTextOption(option)

                            if '_video' in all_source['sids'][ii]:
                                video_source = all_source['sids'][ii]
                                video_sid.append(video_source)
                                remove_video_douhao = re.sub(r',', '\n',str(video_sid)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                remove_video_danyinhao = remove_video_douhao.replace("'", '')
                                video_sources = remove_video_danyinhao.replace(' ', '')
                                ui.video_source_text.setPlainText(video_sources)
                                option = QTextOption()
                                option.setAlignment(Qt.AlignCenter)
                                ui.video_source_text.document().setDefaultTextOption(option)

                            if '_plaque' in all_source['sids'][ii]:
                                plaque_source = all_source['sids'][ii]
                                plaque_sid.append(plaque_source)
                                remove_plaque_douhao = re.sub(r',', '\n',str(plaque_sid)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                remove_plaque_danyinhao = remove_plaque_douhao.replace("'", '')
                                plaque_sources = remove_plaque_danyinhao.replace(' ', '')
                                ui.plaque_source_text.setPlainText(plaque_sources)
                                option = QTextOption()
                                option.setAlignment(Qt.AlignCenter)
                                ui.plaque_source_text.document().setDefaultTextOption(option)

                            if '_splash' in all_source['sids'][ii]:
                                splash_source = all_source['sids'][ii]
                                splash_sid.append(splash_source)
                                remove_splash_douhao = re.sub(r',', '\n',str(splash_sid)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                                remove_splash_danyinhao = remove_splash_douhao.replace("'", '')
                                splash_sources = remove_splash_danyinhao.replace(' ', '')
                                ui.splash_source_text.setPlainText(splash_sources)
                                option = QTextOption()
                                option.setAlignment(Qt.AlignCenter)
                                ui.splash_source_text.document().setDefaultTextOption(option)


        except:
            tips = QMessageBox(QMessageBox.Critical, '错误', '程序错误')

    def ad_clean_click():
        ui.all_text.clear()
        ui.A_text.clear()
        ui.B_text.clear()
        ui.C_text.clear()
        ui.splash_cfg_text.clear()
        ui.msg_cfg_text.clear()
        ui.video_cfg_text.clear()
        ui.plaque_cfg_text.clear()
        ui.splash_source_text.clear()
        ui.msg_source_text.clear()
        ui.video_source_text.clear()
        ui.plaque_source_text.clear()

    def ad_name_than(self):
        try:
            pid = ui.prid_2.text()
            chan = ui.app_chan_2.text()
            pro = ui.package_info.text()
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
                sids = ['all', '1066A_A', '1066B_B', '1066C_C']  # 把目前在用的4个分组放在列表
                res = requests.get('http://192.168.7.30:8008/ad')
                if pro not in res.json():
                    pro_msg_box = QMessageBox(QMessageBox.Critical, '错误', '输入的key有误')
                    pro_msg_box.exec_()
                all_ad_name = res.json()[f'{pro}']
                for i in sids:  # 对列表进行循环，列表内每一个分组的值进行输出
                    txt = '{"buy_id":"default",' \
                          '"imei":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                          f'"pid":"{pid}",' \
                          f'"sid":"{i}",' \
                          '"lsn":"85202900",' \
                          f'"appid":"{appid}",' \
                          '"isNewUser":"1",' \
                          '"brand":"HUAWEI",' \
                          '"os_version":"ele-al00 10.1.0.162(c00e160r2p11)",' \
                          '"debug":"1",' \
                          '"oaid":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                          f'"cha_id":"{chan}",' \
                          '"buy_act":"default",' \
                          '"os":"EmotionUI_12.0.0"}'
                    s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
                    code = base64.b64encode(s).decode("utf-8")
                    url = f'https://cfg.vigame.cn/v14/extend?value={code}'
                    http_get = requests.get(url)
                    connect = http_get.json()
                    ad_strategys = connect['strategys']
                    ad_name = connect['adPositions']
                    actual_adname = []  # 空列表 用于接收实际配置的广告位
                    short_ad_name = []  # 空列表 用于接收缺少的广告位
                    match_ad_name = []  # 空列表 用于接收匹配的广告位
                    tmr_ad_name = []  # 空列表 用于接收冗余的广告位
                    for i in range(len(ad_name)):
                        actual_adname.append(ad_name[i]['name'])
                    for ii in range(len(all_ad_name)):
                        if all_ad_name[ii] in actual_adname:
                            match_ad_name.append(all_ad_name[ii])
                        if all_ad_name[ii] not in actual_adname:
                            short_ad_name.append(all_ad_name[ii])
                    for iii in range(len(actual_adname)):
                        if actual_adname[iii] not in all_ad_name:
                            tmr_ad_name.append(actual_adname[iii])

                remove_match_douhao = re.sub(r',', '\n', str(match_ad_name)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                remove_match_danyinhao = remove_match_douhao.replace("'", '')
                match = remove_match_danyinhao.replace(' ', '')
                ui.match_text.setPlainText(f"-----匹配的广告位-----\n{match}")
                option = QTextOption()
                option.setAlignment(Qt.AlignCenter)
                ui.match_text.document().setDefaultTextOption(option)
                if len(short_ad_name) == 0:
                    ui.lack_text.setPlainText('无缺少的广告位')
                    option = QTextOption()
                    option.setAlignment(Qt.AlignCenter)
                    ui.lack_text.document().setDefaultTextOption(option)
                else:
                    remove_lack_douhao = re.sub(r',', '\n', str(short_ad_name)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                    remove_lack_danyinhao = remove_lack_douhao.replace("'", '')
                    short = remove_lack_danyinhao.replace(' ', '')
                    ui.lack_text.setPlainText(f"-----含有缺少的广告位-----\n{short}")
                    option = QTextOption()
                    option.setAlignment(Qt.AlignCenter)
                    ui.lack_text.document().setDefaultTextOption(option)

                if len(tmr_ad_name) == 0:
                    ui.tmr_text.setPlainText('无冗余的广告位')
                    option = QTextOption()
                    option.setAlignment(Qt.AlignCenter)
                    ui.tmr_text.document().setDefaultTextOption(option)
                else:
                    remove_tmr_douhao = re.sub(r',', '\n', str(tmr_ad_name)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
                    remove_tmr_danyinhao = remove_tmr_douhao.replace("'", '')
                    tmr = remove_tmr_danyinhao.replace(' ', '')
                    ui.tmr_text.setPlainText(f"-----含有冗余的广告位-----\n{tmr}")
                    option = QTextOption()
                    option.setAlignment(Qt.AlignCenter)
                    ui.tmr_text.document().setDefaultTextOption(option)

        except:
            tips = QMessageBox(QMessageBox.Critical, '错误', '程序错误')
    def ad_name_clean(self):
        ui.match_text.clear()
        ui.tmr_text.clear()
        ui.lack_text.clear()

    def linetxt(self):
        dir_name = ui.dir_name_2.text()
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
        dir_name = ui.dir_name_2.text()
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
                showImage = QPixmap(path).scaled(ui.img6.width(), ui.img6.height())
                # 展示图片，达到预览效果
                ui.img6.setPixmap(showImage)
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
        dir_name = ui.dir_name_2.text()
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
                showImage = QPixmap(path).scaled(ui.img2_2.width(), ui.img2_2.height())
                # 展示图片，达到预览效果
                ui.img2_2.setPixmap(showImage)
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
        dir_name = ui.dir_name_2.text()
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
                showImage = QPixmap(path).scaled(ui.img3_2.width(), ui.img3_2.height())
                # 展示图片，达到预览效果
                ui.img3_2.setPixmap(showImage)
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
        dir_name = ui.dir_name_2.text()
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
                showImage = QPixmap(path).scaled(ui.img4_2.width(), ui.img4_2.height())
                # 展示图片，达到预览效果
                ui.img4_2.setPixmap(showImage)
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
        dir_name = ui.dir_name_2.text()
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
                showImage = QPixmap(path).scaled(ui.img5_2.width(), ui.img5_2.height())
                # 展示图片，达到预览效果
                ui.img5_2.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()


    def mkdir_name(self):
        a = ui.mkdir_txt.toPlainText()
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
        ui.mkdir_txt.clear()

if __name__ == '__main__':
    # 初始化数据
    # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = check_cfg_frame.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    line_apk_path = ui.line_apkdir_path.installEventFilter(QEventHandler(ui.line_apkdir_path))
    ui.select_online.clicked.connect(Main.online_select_click)
    ui.clean_online_text.clicked.connect(Main.online_clean_click)
    ui.select_ad.clicked.connect(Main.ad_select_click)
    ui.clean_ad_text.clicked.connect(Main.ad_clean_click)
    ui.select_ad_2.clicked.connect(Main.ad_name_than)
    ui.clean_ad_text_2.clicked.connect(Main.ad_name_clean)
    ui.mkdir_dir_2.clicked.connect(Main.linetxt)
    ui.scr1_2.clicked.connect(Main.scra)
    ui.scr2_2.clicked.connect(Main.scrb)
    ui.scr3_2.clicked.connect(Main.scrc)
    ui.scr4_2.clicked.connect(Main.scrd)
    ui.scr5_2.clicked.connect(Main.scre)
    ui.mkdir_name.clicked.connect(Main.mkdir_name)
    ui.clear_dirtxt.clicked.connect(Main.clear_dir_text)
    int_num = QIntValidator()
    int_num.setRange(1, 99999999)
    ui.prid.setValidator(int_num)
    ui.app_chan.setValidator(QRegExpValidator(QRegExp("[a-z]{12}")))
    sys.exit(app.exec_())
