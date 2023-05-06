import re
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import untitled
import requests

def ceshi():
    a = ui.lineEdit.text()
    url = 'http://192.168.7.30:8008/ad'
    res = requests.get(url)
    ad_name = res.json()
    try:
        adname = ad_name[f'{a}']
        if a == '':
            ui.textBrowser.setText('请输入key')
        else:
            ui.textBrowser.setText(f'{str(adname)}')
    except:
        ui.textBrowser.setText('请输入对应的key')

if __name__ == '__main__':
    # 初始化数据
    # 。。。。。
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(ceshi)

    sys.exit(app.exec_())
