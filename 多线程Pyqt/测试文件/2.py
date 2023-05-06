import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QMessageBox
from PyQt5.QtCore import QFileSystemWatcher


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.watcher = QFileSystemWatcher(self)
        self.watcher.fileChanged.connect(self.display_path)

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('File Watcher')

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 200, 30)
        self.textbox.setDragEnabled(True)

        self.show()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        path = event.mimeData().urls()[0].toLocalFile()
        self.watcher.addPath(path)

    def display_path(self, path):
        self.textbox.setText(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())