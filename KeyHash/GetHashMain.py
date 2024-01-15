import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from qt_material import apply_stylesheet
from untitled import Ui_Form
from GetHashApi import upload_jks_file
from EventHandler import QEventHandler




class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.HashSelect.clicked.connect(self.SelectHash)
        self.KeyFile.installEventFilter(QEventHandler(self.KeyFile))
        self.KeyFile.setPlaceholderText("拖入签名文件生成路径")


    def SelectHash(self):
        key_name = self.KeyName.text()
        key_password = self.KeyPassword.text()
        key_path = self.KeyFile.text()
        get_hash = upload_jks_file(upload_url='http://192.168.7.188:8111/upload', key_name=key_name, key_password=key_password, file_path=key_path)
        self.KeyHashInfo.setText(get_hash)
        print(get_hash)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())