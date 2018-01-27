# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Decipher_GUI.ui'
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


class Ui_decipher(object):
    def setupUi(self, decipher):
        decipher.setObjectName(_fromUtf8("decipher"))
        decipher.resize(651, 505)
        decipher.setMinimumSize(QtCore.QSize(651, 505))
        decipher.setMaximumSize(QtCore.QSize(651, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Logo/PyPher.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        decipher.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(decipher)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 631, 411))
        self.textEdit.setMinimumSize(QtCore.QSize(631, 411))
        self.textEdit.setMaximumSize(QtCore.QSize(631, 411))
        self.textEdit.setStyleSheet(_fromUtf8("font: 75 11pt \"Yu Gothic UI Semibold\";"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.go_back = QtGui.QCommandLinkButton(decipher)
        self.go_back.setEnabled(True)
        self.go_back.setGeometry(QtCore.QRect(10, 440, 121, 51))
        self.go_back.setMinimumSize(QtCore.QSize(121, 51))
        self.go_back.setMaximumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.go_back.setFont(font)
        self.go_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_back.setStyleSheet(_fromUtf8("color: #626065;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/back.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.go_back.setIcon(icon1)
        self.go_back.setIconSize(QtCore.QSize(30, 30))
        self.go_back.setDefault(False)
        self.go_back.setObjectName(_fromUtf8("go_back"))
        self.save = QtGui.QCommandLinkButton(decipher)
        self.save.setEnabled(True)
        self.save.setGeometry(QtCore.QRect(200, 440, 101, 51))
        self.save.setMinimumSize(QtCore.QSize(101, 51))
        self.save.setMaximumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setStyleSheet(_fromUtf8("color: #626065;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/download.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setIconSize(QtCore.QSize(30, 30))
        self.save.setDefault(False)
        self.save.setObjectName(_fromUtf8("save"))
        self.delete_file = QtGui.QCommandLinkButton(decipher)
        self.delete_file.setEnabled(True)
        self.delete_file.setGeometry(QtCore.QRect(310, 440, 111, 51))
        self.delete_file.setMinimumSize(QtCore.QSize(111, 51))
        self.delete_file.setMaximumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delete_file.setFont(font)
        self.delete_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_file.setStyleSheet(_fromUtf8("color: #626065;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/delete.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.delete_file.setIcon(icon3)
        self.delete_file.setIconSize(QtCore.QSize(30, 30))
        self.delete_file.setDefault(False)
        self.delete_file.setObjectName(_fromUtf8("delete_file"))
        self.password = QtGui.QCommandLinkButton(decipher)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(430, 440, 211, 51))
        self.password.setMinimumSize(QtCore.QSize(211, 51))
        self.password.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password.setStyleSheet(_fromUtf8("color: #626065;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/edit.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.password.setIcon(icon4)
        self.password.setIconSize(QtCore.QSize(30, 30))
        self.password.setDefault(False)
        self.password.setObjectName(_fromUtf8("password"))
        self.line = QtGui.QFrame(decipher)
        self.line.setGeometry(QtCore.QRect(150, 450, 20, 31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(decipher)
        QtCore.QMetaObject.connectSlotsByName(decipher)

    def retranslateUi(self, decipher):
        decipher.setWindowTitle(_translate("decipher", "PyPher", None))
        self.textEdit.setHtml(_translate("decipher",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Yu Gothic UI Semibold\'; font-size:11pt; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                         None))
        self.go_back.setText(_translate("decipher", "Go Back", None))
        self.save.setText(_translate("decipher", " Save", None))
        self.delete_file.setText(_translate("decipher", "Delete", None))
        self.password.setText(_translate("decipher", " Change Password", None))


import resources

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    decipher = QtGui.QWidget()
    ui = Ui_decipher()
    ui.setupUi(decipher)
    decipher.show()
    sys.exit(app.exec_())
