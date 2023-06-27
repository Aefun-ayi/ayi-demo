import sys
from PyQt5.QtWidgets import QWidget, QApplication
import untitled
from adb_order import check_adb_devices, get_connected_device_models

class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Refresh)

    def Refresh(self):
        self.comboBox.clear()
        for i in get_connected_device_models():
            self.comboBox.addItem(f'{i}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())