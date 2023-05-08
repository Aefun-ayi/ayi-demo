# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1058, 608)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dir_name = QtWidgets.QLineEdit(Form)
        self.dir_name.setMinimumSize(QtCore.QSize(0, 50))
        self.dir_name.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.dir_name.setObjectName("dir_name")
        self.horizontalLayout.addWidget(self.dir_name)
        self.mkdir_dir = QtWidgets.QPushButton(Form)
        self.mkdir_dir.setMinimumSize(QtCore.QSize(0, 50))
        self.mkdir_dir.setObjectName("mkdir_dir")
        self.horizontalLayout.addWidget(self.mkdir_dir)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.img1 = QtWidgets.QLabel(Form)
        self.img1.setTextFormat(QtCore.Qt.AutoText)
        self.img1.setAlignment(QtCore.Qt.AlignCenter)
        self.img1.setObjectName("img1")
        self.verticalLayout.addWidget(self.img1)
        self.scr1 = QtWidgets.QPushButton(Form)
        self.scr1.setObjectName("scr1")
        self.verticalLayout.addWidget(self.scr1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img2 = QtWidgets.QLabel(Form)
        self.img2.setAlignment(QtCore.Qt.AlignCenter)
        self.img2.setObjectName("img2")
        self.verticalLayout_2.addWidget(self.img2)
        self.scr2 = QtWidgets.QPushButton(Form)
        self.scr2.setObjectName("scr2")
        self.verticalLayout_2.addWidget(self.scr2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img3 = QtWidgets.QLabel(Form)
        self.img3.setAlignment(QtCore.Qt.AlignCenter)
        self.img3.setObjectName("img3")
        self.verticalLayout_3.addWidget(self.img3)
        self.scr3 = QtWidgets.QPushButton(Form)
        self.scr3.setObjectName("scr3")
        self.verticalLayout_3.addWidget(self.scr3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img4 = QtWidgets.QLabel(Form)
        self.img4.setAlignment(QtCore.Qt.AlignCenter)
        self.img4.setObjectName("img4")
        self.verticalLayout_4.addWidget(self.img4)
        self.scr4 = QtWidgets.QPushButton(Form)
        self.scr4.setObjectName("scr4")
        self.verticalLayout_4.addWidget(self.scr4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.img5 = QtWidgets.QLabel(Form)
        self.img5.setAlignment(QtCore.Qt.AlignCenter)
        self.img5.setObjectName("img5")
        self.verticalLayout_5.addWidget(self.img5)
        self.scr5 = QtWidgets.QPushButton(Form)
        self.scr5.setObjectName("scr5")
        self.verticalLayout_5.addWidget(self.scr5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "截五图工具"))
        self.label.setText(_translate("Form", "创建五图文件夹"))
        self.mkdir_dir.setText(_translate("Form", "创建目录"))
        self.img1.setText(_translate("Form", "图片预览区"))
        self.scr1.setText(_translate("Form", "截图（1）"))
        self.img2.setText(_translate("Form", "图片预览区"))
        self.scr2.setText(_translate("Form", "截图（2）"))
        self.img3.setText(_translate("Form", "图片预览区"))
        self.scr3.setText(_translate("Form", "截图（3）"))
        self.img4.setText(_translate("Form", "图片预览区"))
        self.scr4.setText(_translate("Form", "截图（4）"))
        self.img5.setText(_translate("Form", "图片预览区"))
        self.scr5.setText(_translate("Form", "截图（5）"))