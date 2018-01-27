# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_password.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(442, 150)
        Dialog.setMinimumSize(QtCore.QSize(442, 150))
        Dialog.setMaximumSize(QtCore.QSize(442, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Logo/PyPher.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.send_pass = QtGui.QCommandLinkButton(Dialog)
        self.send_pass.setGeometry(QtCore.QRect(380, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(6)
        self.send_pass.setFont(font)
        self.send_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_pass.setFocusPolicy(QtCore.Qt.TabFocus)
        self.send_pass.setAcceptDrops(False)
        self.send_pass.setStyleSheet(_fromUtf8("border: white;\n"
                                               ""))
        self.send_pass.setText(_fromUtf8(""))
        self.send_pass.setIconSize(QtCore.QSize(15, 15))
        self.send_pass.setObjectName(_fromUtf8("send_pass"))
        self.set_pass = QtGui.QLineEdit(Dialog)
        self.set_pass.setGeometry(QtCore.QRect(190, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.set_pass.setFont(font)
        self.set_pass.setMouseTracking(True)
        self.set_pass.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.set_pass.setStyleSheet(_fromUtf8("font: 75 9pt \"Yu Gothic UI Semibold\";"))
        self.set_pass.setObjectName(_fromUtf8("set_pass"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.set_pass, self.send_pass)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PyPher - Password", None))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:15pt; color:#626065;\">Set password for your file</span></p></body></html>",
                                        None))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#626065;\">Enter Password :</span></p></body></html>",
                                        None))


import resources

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
