import sys
import ayiceshi
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = ayiceshi.Ui_Form()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
