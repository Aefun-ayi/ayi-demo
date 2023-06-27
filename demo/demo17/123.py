import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
import untitled


class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        showImage = QPixmap(r"D:\keep\五图截图\头-省电小精灵A_viyy\2023年06月13日 18时31分10秒五图-1.png").scaled(self.label.width(), self.label.height())
        # 展示图片，达到预览效果
        self.label.setPixmap(showImage)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())