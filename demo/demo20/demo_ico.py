import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QApplication
from qt_material import apply_stylesheet
import untitled
import qtawesome as qta


class MainWindow(QWidget, untitled.Ui_Form):
    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        icon_spin = qta.icon('ri.refresh-line', color='white', color_disabled='red',animation=qta.Spin(self.pushButton, interval=1, step=1))
        self.pushButton.setIcon(icon_spin)
        self.pushButton.setStyleSheet("font: 30pt \"华文细黑\";""color: rgb(170, 255, 127);""border-radius: 20px;")
        self.pushButton.setIconSize(QSize(50, 50))
        fa5_icon = qta.icon('mdi.delete-forever-outline', color='white')
        self.pushButton_2.setIcon(fa5_icon)
        self.pushButton_2.setStyleSheet("font: 30pt \"华文细黑\";""color: rgb(170, 255, 127);""border-radius: 20px;")
        self.pushButton_2.setIconSize(QSize(50, 50))
        self.label.setMinimumSize(0, 50)
        movie = QMovie('584_20220713102555471.gif')
        self.label.setMovie(movie)
        movie.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())