# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 400)
        Form.setMinimumSize(QSize(300, 400))
        Form.setMaximumSize(QSize(300, 400))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 131, 121))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setPixmap(QPixmap(u"../images/user_profile.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.login_name = QLineEdit(Form)
        self.login_name.setObjectName(u"login_name")
        self.login_name.setGeometry(QRect(40, 180, 221, 31))
        font = QFont()
        font.setFamily(u"Candara Light")
        font.setPointSize(10)
        self.login_name.setFont(font)
        self.login_name.setStyleSheet(u"border-color: rgb(81, 244, 244);\n"
"border: 2px solid #55ffff;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.login_name.setEchoMode(QLineEdit.Normal)
        self.login_name.setCursorPosition(0)
        self.login_name.setDragEnabled(True)
        self.login_name.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.login_name.setClearButtonEnabled(True)
        self.login_password = QLineEdit(Form)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setGeometry(QRect(40, 230, 221, 31))
        self.login_password.setFont(font)
        self.login_password.setStyleSheet(u"border-color: rgb(81, 244, 244);\n"
"border: 2px solid #55ffff;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.login_password.setEchoMode(QLineEdit.Password)
        self.login_password.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.login_password.setClearButtonEnabled(True)
        self.login_in = QPushButton(Form)
        self.login_in.setObjectName(u"login_in")
        self.login_in.setGeometry(QRect(40, 290, 221, 31))
        self.login_in.setFont(font)
        self.login_in.setStyleSheet(u"background-color: #55ffff;\n"
"border: 1px solid #55ffff;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.login_register = QPushButton(Form)
        self.login_register.setObjectName(u"login_register")
        self.login_register.setGeometry(QRect(40, 340, 221, 31))
        self.login_register.setFont(font)
        self.login_register.setStyleSheet(u"background-color: #55ffff;\n"
"border: 1px solid #55ffff;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.login_name.setText("")
        self.login_name.setPlaceholderText(QCoreApplication.translate("Form", u" input your name", None))
        self.login_password.setText("")
        self.login_password.setPlaceholderText(QCoreApplication.translate("Form", u" input password", None))
        self.login_in.setText(QCoreApplication.translate("Form", u"Login", None))
        self.login_register.setText(QCoreApplication.translate("Form", u"Register", None))
    # retranslateUi

