import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
import qtawesome as qta

class QWindow(QWidget):
    def __init__(self, parent=None, flags= Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 300
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.x = int((self.SCREEN_WIDTH - self.WINDOW_WIDTH) / 2)
        self.y = int((self.SCREEN_HEIGHT - self.WINDOW_HEIGHT) / 2)
        self.window_grid_layout = QGridLayout()
        self.window_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.init_layout()
        self.set_layout()
        self.finish_layout()

    def init_layout(self):
        self.btn = QPushButton(qta.icon('fa5s.cannabis', color='olive'), '测试')
        pass

    def set_layout(self):
        self.window_grid_layout.addWidget(self.btn, 0, 0, 1, 1)
        pass

    def finish_layout(self):
        self.setLayout(self.window_grid_layout)
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWindow()
    window.resize(window.WINDOW_WIDTH, window.WINDOW_HEIGHT)
    window.move(window.x, window.y)
    window.setWindowTitle('阿一测试使用')
    window.show()
    sys.exit(app.exec_())
    pass
