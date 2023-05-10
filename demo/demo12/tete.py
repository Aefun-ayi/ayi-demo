import sys
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from queue import Queue


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        self.button = QPushButton("Start")
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.queue = queue

        self.button.clicked.connect(self.start_thread)

    def start_thread(self):
        text = self.lineEdit.text()
        self.queue.put(text)


class MyThread(QThread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        text = self.queue.get()
        # 处理lineedit的文本内容
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = MyWidget()
    queue = Queue()
    thread = MyThread(queue)
    thread.start()
    widget.show()

    sys.exit(app.exec_())