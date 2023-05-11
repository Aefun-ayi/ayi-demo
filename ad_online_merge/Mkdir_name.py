import datetime
import os
from PyQt5.QtWidgets import QMessageBox


def mk_dir_name(mkdirtxt):
    a = mkdirtxt
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
        want_file = fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{project_name}\{prid}\{chan}' + '.txt'
        file = open(want_file, 'w')
        file.write('投放渠道：' + str(de_channl) + '\n出包需求：' + str(want) + '\n打包参数：' + str(packageinfo))  # 写入出包需求
        mmm_box = QMessageBox(QMessageBox.Information, '提示', fr'项目id：{prid}  产品名称{project_name}  产品需求：{want} 创建成功')
        mmm_box.exec_()