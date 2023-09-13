import os
from PyQt5.QtWidgets import QMessageBox

def ImgDriName(dirname):
    dir_name = dirname
    if '\n' in dir_name:
        dir_remove_line = dir_name.replace("\n", '')
        dir_path = dir_remove_line.replace('	', '_')
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