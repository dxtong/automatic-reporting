# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\My Drive\Programming\python\swire_autoreport_v0.1\swire_autoreport.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_swire_autoreport(object):
    def setupUi(self, swire_autoreport):
        swire_autoreport.setObjectName("swire_autoreport")
        swire_autoreport.resize(310, 124)
        swire_autoreport.setMinimumSize(QtCore.QSize(310, 0))
        swire_autoreport.setMaximumSize(QtCore.QSize(310, 124))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/columbia.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        swire_autoreport.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(swire_autoreport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(swire_autoreport)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(swire_autoreport)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(swire_autoreport)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(swire_autoreport)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(swire_autoreport)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(swire_autoreport)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(swire_autoreport)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(swire_autoreport)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(swire_autoreport)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setTime(QtCore.QTime(19, 1, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(swire_autoreport)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(swire_autoreport)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(swire_autoreport)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(swire_autoreport)
        QtCore.QMetaObject.connectSlotsByName(swire_autoreport)
        swire_autoreport.setTabOrder(self.lineEdit, self.lineEdit_2)
        swire_autoreport.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        swire_autoreport.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        swire_autoreport.setTabOrder(self.lineEdit_4, self.timeEdit)
        swire_autoreport.setTabOrder(self.timeEdit, self.pushButton)
        swire_autoreport.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, swire_autoreport):
        _translate = QtCore.QCoreApplication.translate
        swire_autoreport.setWindowTitle(_translate("swire_autoreport", "Swire & NBA 自動報表"))
        self.label_4.setText(_translate("swire_autoreport", "Email密碼:"))
        self.label_2.setText(_translate("swire_autoreport", "WMS密碼:"))
        self.label.setText(_translate("swire_autoreport", "WMS帳戶:"))
        self.label_3.setText(_translate("swire_autoreport", "Email帳戶:"))
        self.timeEdit.setDisplayFormat(_translate("swire_autoreport", "hh:mm"))
        self.pushButton.setText(_translate("swire_autoreport", "執行"))
        self.pushButton_2.setText(_translate("swire_autoreport", "停止"))
import image_rc
