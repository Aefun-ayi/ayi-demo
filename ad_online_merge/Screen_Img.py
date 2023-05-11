import uiautomator2 as u2
from PyQt5.QtWidgets import QMessageBox
import os
import datetime



def scr(dirname_text):
    try:
        # 加入try 避免出现连接失败时产生的闪退问题
        d = u2.connect()
    except RuntimeError as run:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', f'报错信息：{run}，手机连接失败，请重新连接手机')
        msg_box.exec_()
    dir_name = dirname_text
    # 判断输入为空处理
    if dir_name == '':
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入创建五图文件夹的目录名')
        msg_box.exec_()
    else:
        # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
        dir_path = dir_name.replace('	', '_')
        isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
        # 进入判断是否存在这个文件夹
        if isExists:
            # 时间戳
            filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日',h='时', f='分', s='秒')
            # 截图路径
            path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-1.png")
            return path

        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
            msg_box.exec_()