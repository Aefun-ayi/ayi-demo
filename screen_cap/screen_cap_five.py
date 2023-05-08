# d = u2.connect()
# d.app_start('net.cafewfwednfq.tssfefonar.ixk','com.cc.run.view.activity.SplashActivity')
#
# d.screenshot(f"D:/Test_ToolS/images/测试使用.jpg")
import uiautomator2 as u2
import untitled
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import os
import datetime

class Main_window():
    def linetxt(self):
        dir_name = ui.dir_name.text()
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
        dir_name = ui.dir_name.text()
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
                showImage = QPixmap(path).scaled(ui.img1.width(), ui.img1.height())
                # 展示图片，达到预览效果
                ui.img1.setPixmap(showImage)
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
        dir_name = ui.dir_name.text()
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
                showImage = QPixmap(path).scaled(ui.img2.width(), ui.img2.height())
                # 展示图片，达到预览效果
                ui.img2.setPixmap(showImage)
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
        dir_name = ui.dir_name.text()
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
                showImage = QPixmap(path).scaled(ui.img3.width(), ui.img3.height())
                # 展示图片，达到预览效果
                ui.img3.setPixmap(showImage)
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
        dir_name = ui.dir_name.text()
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
                showImage = QPixmap(path).scaled(ui.img4.width(), ui.img4.height())
                # 展示图片，达到预览效果
                ui.img4.setPixmap(showImage)
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
        dir_name = ui.dir_name.text()
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
                showImage = QPixmap(path).scaled(ui.img5.width(), ui.img5.height())
                # 展示图片，达到预览效果
                ui.img5.setPixmap(showImage)
            else:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
                msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.mkdir_dir.clicked.connect(Main_window.linetxt)
    ui.scr1.clicked.connect(Main_window.scra)
    ui.scr2.clicked.connect(Main_window.scrb)
    ui.scr3.clicked.connect(Main_window.scrc)
    ui.scr4.clicked.connect(Main_window.scrd)
    ui.scr5.clicked.connect(Main_window.scre)
    sys.exit(app.exec_())