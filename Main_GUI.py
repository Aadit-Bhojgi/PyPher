# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_GUI.ui'
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


class Ui_PyPher(object):
    def setupUi(self, PyPher):
        PyPher.setObjectName(_fromUtf8("PyPher"))
        PyPher.resize(650, 708)
        PyPher.setMinimumSize(QtCore.QSize(650, 708))
        PyPher.setMaximumSize(QtCore.QSize(650, 708))
        font = QtGui.QFont()
        font.setPointSize(12)
        PyPher.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Logo/PyPher.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PyPher.setWindowIcon(icon)
        PyPher.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(PyPher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 0, 481, 461))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 590, 491, 101))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.choose_file = QtGui.QCommandLinkButton(self.horizontalLayoutWidget)
        self.choose_file.setEnabled(True)
        self.choose_file.setMinimumSize(QtCore.QSize(211, 71))
        self.choose_file.setMaximumSize(QtCore.QSize(211, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.choose_file.setFont(font)
        self.choose_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_file.setStyleSheet(_fromUtf8("color: #626065;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/document.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.choose_file.setIcon(icon1)
        self.choose_file.setIconSize(QtCore.QSize(50, 50))
        self.choose_file.setDefault(False)
        self.choose_file.setObjectName(_fromUtf8("choose_file"))
        self.horizontalLayout.addWidget(self.choose_file)
        self.create_new = QtGui.QCommandLinkButton(self.horizontalLayoutWidget)
        self.create_new.setEnabled(True)
        self.create_new.setMinimumSize(QtCore.QSize(211, 71))
        self.create_new.setMaximumSize(QtCore.QSize(211, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.create_new.setFont(font)
        self.create_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new.setStyleSheet(_fromUtf8("color: #626065;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/new-file.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.create_new.setIcon(icon2)
        self.create_new.setIconSize(QtCore.QSize(50, 50))
        self.create_new.setDefault(False)
        self.create_new.setObjectName(_fromUtf8("create_new"))
        self.horizontalLayout.addWidget(self.create_new)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 450, 231, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.about = QtGui.QCommandLinkButton(self.centralwidget)
        self.about.setEnabled(True)
        self.about.setGeometry(QtCore.QRect(290, 540, 81, 41))
        self.about.setMinimumSize(QtCore.QSize(81, 41))
        self.about.setMaximumSize(QtCore.QSize(81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.about.setFont(font)
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about.setStyleSheet(_fromUtf8("color: #626065;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Graphics/Buttons/info.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.about.setIcon(icon3)
        self.about.setIconSize(QtCore.QSize(22, 22))
        self.about.setDefault(False)
        self.about.setObjectName(_fromUtf8("about"))
        self.actionAbout = QtGui.QAction(PyPher)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.retranslateUi(PyPher)
        QtCore.QMetaObject.connectSlotsByName(PyPher)

    def retranslateUi(self, PyPher):
        PyPher.setWindowTitle(_translate("PyPher", "PyPher", None))
        self.label.setText(_translate("PyPher",
                                      "<html><head/><body><p><img src=\":/newPrefix/Graphics/Buttons/description.png\"/></p></body></html>",
                                      None))
        self.choose_file.setText(_translate("PyPher", "Choose File", None))
        self.create_new.setText(_translate("PyPher", "Create New", None))
        self.label_4.setText(_translate("PyPher",
                                        "<html><head/><body><p><span style=\" font-size:45pt; color:#626065;\">PyPher</span></p></body></html>",
                                        None))
        self.about.setText(_translate("PyPher", "Info", None))
        self.actionAbout.setText(_translate("PyPher", "About", None))


import resources

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    PyPher = QtGui.QMainWindow()
    ui = Ui_PyPher()
    ui.setupUi(PyPher)
    PyPher.show()
    sys.exit(app.exec_())
