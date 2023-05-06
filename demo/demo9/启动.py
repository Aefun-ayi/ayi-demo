import  sys
import zhuchuangkou as u1
import zichuangkouyi as u2
import zichuangkouer as u3
from PyQt5.QtWidgets import  *

class thirdWindow(QMainWindow):
    def __init__(self, parent =None):
        super(thirdWindow, self).__init__(parent)
        self.ui3 = u3.Ui_Form()
        self.ui3.setupUi(self)

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.ui2 = u2.Ui_Form()
        self.ui2.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = u1.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui2 = u2.Ui_Form()
        # self.ui2.setupUi(self)
        # self.ui3 = u3.Ui_Form()
        # self.ui3.setupUi(self)
        self.ui.pushButton.clicked.connect(self.slot1)
        # self.ui.pushButton_2.clicked.connect(self.slot2)

    def slot1(self):

        u2.Ui_Form

    # def slot2(self):
    #     win3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    # win2 = SecondWindow()
    # win3 = thirdWindow()

    sys.exit(app.exec_())
