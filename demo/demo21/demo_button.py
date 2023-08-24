import qtawesome as qta
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget

if __name__ == '__main__':
    app = QApplication([])
    button = QPushButton("ok")

    icon_spin = qta.icon('msc.account', color='white',color_disabled='red', animation=qta.Spin(button, interval=1, step=1))

    icon_pulse = qta.icon('msc.account', color='white', color_disabled='red', animation=qta.Pulse(button))

    button.setIcon(icon_spin)

    button.show()
    app.exec_()