import sys
import qdarkstyle
from PyQt5.QtWidgets import QWidget, QApplication
import untitled
from qt_material import apply_stylesheet

class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.auto_path.setPlaceholderText("请拖入安装包获取路径开始操作")
        self.line_apkdir_path.setPlaceholderText("请拖入安装包获取路径开始操作")
        self.select_online.clicked.connect(self.AAA)

    def AAA(self):
        self.suc_cfg.append('test')
        self.fail_cfg.append('tttt')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())