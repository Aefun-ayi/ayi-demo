import sys
from PyQt5.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
import untitled
import aes_main



class MainWindow(QWidget, untitled.Ui_Form):

    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.decode.clicked.connect(self.decrypt_aes)
        self.encryp.clicked.connect(self.encrypt_aes)

    def encrypt_aes(self):
        text = self.text.toPlainText()
        key = b'1234561234561234'
        iv = b'1234561234561234'
        encrypted_data = aes_main.aes_encrypt(text, key, iv)
        self.encryp_text.setText(encrypted_data.decode('utf-8'))

    def decrypt_aes(self):
        text = self.encryp_text.toPlainText()
        key = b'1234561234561234'
        iv = b'1234561234561234'
        decrypt_data = aes_main.aes_decrypt(text, key, iv)
        self.text.setText(decrypt_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
