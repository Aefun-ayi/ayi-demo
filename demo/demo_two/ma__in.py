import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
import os
import untitled
class QEventHandler(QtCore.QObject):
    def eventFilter(self, obj, event):
        """
        目前已经实现将拖到控件上文件的路径设置为控件的显示文本；
        """
        if event.type() == QtCore.QEvent.DragEnter:
            event.accept()
        if event.type() == QtCore.QEvent.Drop:
            md = event.mimeData()
            if md.hasUrls():
            	# 此处md.urls()的返回值为拖入文件的file路径列表，支持多文件同时拖入；默认读取第一个文件的路径进行处理
                url = md.urls()[0]
                obj.setText(url.toLocalFile())
                # print(str(url.toLocalFile()))
                # print(type(url))
                return True
        return super().eventFilter(obj, event)

def online_select_click():
    a = ui.line_apkdir_path.text()

    ui.suc_cfg.append(a)
    # print(a)
    # print(type(a))


if __name__ == '__main__':
    # 初始化数据
    # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    line_apk_path = ui.line_apkdir_path.installEventFilter(QEventHandler(ui.line_apkdir_path))
    ui.select_online.clicked.connect(online_select_click)

    sys.exit(app.exec_())