# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_message(object):
    def setupUi(self, message):
        message.setObjectName(_fromUtf8("message"))
        message.resize(442, 150)
        message.setMinimumSize(QtCore.QSize(442, 150))
        message.setMaximumSize(QtCore.QSize(442, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Logo/PyPher.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        message.setWindowIcon(icon)
        message.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_4 = QtGui.QLabel(message)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(message)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.password = QtGui.QLineEdit(message)
        self.password.setGeometry(QtCore.QRect(190, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.password.setFont(font)
        self.password.setStyleSheet(_fromUtf8("font: 75 9pt \"Yu Gothic UI Semibold\";"))
        self.password.setObjectName(_fromUtf8("password"))
        self.password_send = QtGui.QCommandLinkButton(message)
        self.password_send.setGeometry(QtCore.QRect(380, 70, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(6)
        self.password_send.setFont(font)
        self.password_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_send.setFocusPolicy(QtCore.Qt.TabFocus)
        self.password_send.setAcceptDrops(False)
        self.password_send.setStyleSheet(_fromUtf8("border: white;\n"
                                                   ""))
        self.password_send.setText(_fromUtf8(""))
        self.password_send.setIconSize(QtCore.QSize(15, 15))
        self.password_send.setObjectName(_fromUtf8("password_send"))
        self.label_6 = QtGui.QLabel(message)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(60, 110, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(message)
        QtCore.QMetaObject.connectSlotsByName(message)
        message.setTabOrder(self.password, self.password_send)

    def retranslateUi(self, message):
        message.setWindowTitle(_translate("message", "PyPher - Password", None))
        self.label_4.setText(_translate("message",
                                        "<html><head/><body><p><span style=\" font-size:15pt; color:#626065;\">File is password protected</span></p></body></html>",
                                        None))
        self.label_5.setText(_translate("message",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#626065;\">Enter Password :</span></p></body></html>",
                                        None))
        self.label_6.setText(_translate("message",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:red\">Authentication failed. Please try again</span></p></body></html>",
                                        None))


import resources

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    message = QtGui.QDialog()
    ui = Ui_message()
    ui.setupUi(message)
    message.show()
    sys.exit(app.exec_())
