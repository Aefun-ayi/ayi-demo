from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt5.QtCore import QSize
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个QLabel并设置大小
        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)

        # 加载图片并将其缩放到QLabel的大小
        self.pixmap = QPixmap(r'D:\ayi-demo\icon_dir\sscom.ico')
        self.update_image_size()
        self.label.setPixmap(self.pixmap)

        self.setCentralWidget(self.label)

    def resizeEvent(self, event):
        # QLabel大小变化时重新设置图片大小
        self.update_image_size()
        self.label.setPixmap(self.pixmap)

    def update_image_size(self):
        # 将图片缩放到QLabel大小
        size = self.label.size()
        self.pixmap = self.pixmap.scaled(QSize(size.width(), size.height()), aspectRatioMode=QtCore.Qt.KeepAspectRatio)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()