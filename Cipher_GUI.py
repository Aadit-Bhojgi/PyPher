# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cipher_GUI.ui'
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


class Ui_cipher(object):
    def setupUi(self, cipher):
        cipher.setObjectName(_fromUtf8("cipher"))
        cipher.resize(650, 505)
        cipher.setMinimumSize(QtCore.QSize(650, 505))
        cipher.setMaximumSize(QtCore.QSize(650, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Logo/PyPher.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        cipher.setWindowIcon(icon)
        self.label_6 = QtGui.QLabel(cipher)
        self.label_6.setGeometry(QtCore.QRect(180, 440, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.go_back = QtGui.QCommandLinkButton(cipher)
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
        self.choose = QtGui.QCommandLinkButton(cipher)
        self.choose.setEnabled(True)
        self.choose.setGeometry(QtCore.QRect(400, 440, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.choose.setFont(font)
        self.choose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose.setStyleSheet(_fromUtf8("color: #626065;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/document.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.choose.setIcon(icon2)
        self.choose.setIconSize(QtCore.QSize(30, 30))
        self.choose.setDefault(False)
        self.choose.setObjectName(_fromUtf8("choose"))
        self.save = QtGui.QCommandLinkButton(cipher)
        self.save.setEnabled(True)
        self.save.setGeometry(QtCore.QRect(540, 440, 101, 51))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/download.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.save.setIcon(icon3)
        self.save.setIconSize(QtCore.QSize(30, 30))
        self.save.setDefault(False)
        self.save.setObjectName(_fromUtf8("save"))
        self.line = QtGui.QFrame(cipher)
        self.line.setGeometry(QtCore.QRect(140, 450, 20, 31))
        self.line.setStyleSheet(_fromUtf8(""))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.textEdit = QtGui.QTextEdit(cipher)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 631, 411))
        self.textEdit.setMinimumSize(QtCore.QSize(631, 411))
        self.textEdit.setMaximumSize(QtCore.QSize(631, 411))
        self.textEdit.setStyleSheet(_fromUtf8("font: 75 11pt \"Yu Gothic UI Semibold\";"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(cipher)
        QtCore.QMetaObject.connectSlotsByName(cipher)

    def retranslateUi(self, cipher):
        cipher.setWindowTitle(_translate("cipher", "PyPher", None))
        self.label_6.setText(_translate("cipher",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#626065;\">Choose file from system :</span></p></body></html>",
                                        None))
        self.go_back.setText(_translate("cipher", "Go Back", None))
        self.choose.setText(_translate("cipher", "Choose", None))
        self.save.setText(_translate("cipher", " Save", None))
        self.textEdit.setHtml(_translate("cipher",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Yu Gothic UI Semibold\'; font-size:11pt; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                         None))


import resources

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    cipher = QtGui.QWidget()
    ui = Ui_cipher()
    ui.setupUi(cipher)
    cipher.show()
    sys.exit(app.exec_())
