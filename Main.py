from PyQt4 import QtGui, QtCore
import os
import stat
import Main_GUI
import sys
import Info
import Decipher_GUI
import Decipher
import Cipher
import Cipher_GUI
import message
import set_password
import PyPDF2
import textract


def getText(filename):
    pdf_file = open(filename, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    num_pages = read_pdf.numPages
    count = 0
    text = ""
    # The while loop will read each page
    while count < num_pages:
        pageObj = read_pdf.getPage(count)
        count += 1
        text += pageObj.extractText()
    return text


def message_alert(mess, alert):
    msg = QtGui.QMessageBox()
    msg.setWindowIcon(QtGui.QIcon(":/newPrefix/Graphics/Logo/PyPher.png"))
    msg.setWindowTitle('PyPher')
    msg.setText(mess)
    if alert == 'close':
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.addButton(QtGui.QMessageBox.Cancel)
    elif alert == 'delete':
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.addButton(QtGui.QMessageBox.Cancel)
    elif alert == 'info':
        msg.setIcon(QtGui.QMessageBox.Information)
    msg.addButton(QtGui.QMessageBox.Ok)
    msg.setDefaultButton(QtGui.QMessageBox.Ok)
    result = msg.exec_()
    if result == msg.Ok:
        return 1
    else:
        return 0


class PyPherAbout(QtGui.QDialog, Info.Ui_Dialog):
    def __init__(self):
        super(PyPherAbout, self).__init__()
        self.setupUi(self)


class PyPherPass(QtGui.QDialog, set_password.Ui_Dialog):
    def __init__(self):
        super(PyPherPass, self).__init__()
        self.setupUi(self)
        self.set_pass.setEchoMode(QtGui.QLineEdit.Password)


class PyPherMess(QtGui.QDialog, message.Ui_message):
    def __init__(self, file=''):
        super(PyPherMess, self).__init__()
        self.setupUi(self)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.label_6.hide()
        self.data = ''
        self.file = file
        self.dec = PyPherDecipher(self.file)
        self.decipher = Decipher.Decipher()
        self.password_send.clicked.connect(self.auth)

    def auth(self):
        password = self.password.text()
        self.password.setText('')
        self.decipher = Decipher.Decipher(self.data, password)
        return_result = self.decipher.decipher_password()
        if not return_result[0]:
            self.former_disp(True)
        else:
            file_data = self.decipher.decipher_message(return_result[1])
            form.hide()
            self.hide()
            self.former_disp(False)
            self.dec = PyPherDecipher(self.file, password)
            self.dec.setWindowModality(QtCore.Qt.ApplicationModal)
            self.dec.show()
            self.dec.textEdit.setText(file_data)

    def former_disp(self, val):
        if val:
            self.label_5.move(40, 50)
            self.password.move(190, 60)
            self.password_send.move(380, 60)
            self.label_6.show()
        else:
            self.label_5.move(40, 60)
            self.password.move(190, 70)
            self.password_send.move(380, 70)
            self.label_6.hide()

    def closeEvent(self, event):
        self.former_disp(False)
        self.password.setText('')


class PyPherDecipher(QtGui.QWidget, Decipher_GUI.Ui_decipher):
    def __init__(self, file_open='', password=''):
        super(PyPherDecipher, self).__init__()
        self.setupUi(self)
        self.cipher = Cipher.Cipher()
        self.file = file_open
        self.passw = password
        self.go_back.clicked.connect(self.back)
        self.save.clicked.connect(self.check)
        self.password.clicked.connect(self.set_new)
        self.delete_file.clicked.connect(self.delete)

    def back(self):
        result = message_alert('Any unsaved data will be lost\nDo you want to go back?', 'close')
        if result:
            self.hide()
            form.show()

    def check(self):
        if self.passw == '':
            self.pass_update = PyPherPass()
            self.pass_update.setWindowModality(QtCore.Qt.ApplicationModal)
            self.pass_update.show()
            self.pass_update.send_pass.clicked.connect(self.update)
        else:
            self.cipher_data()
            message_alert('Password Protected File Saved', 'info')

    def update(self):
        new_pass = self.pass_update.set_pass.text()
        if new_pass != '':
            self.pass_update.close()
            self.passw = new_pass
            self.cipher_data()
            message_alert('Password Changed', 'info')

    def cipher_data(self):
        self.cipher = Cipher.Cipher(self.textEdit.toPlainText(), self.passw)
        ciphered = self.cipher.cipher()
        if not os.stat(self.file)[0] & stat.S_IWRITE:
            # File is read-only, so make it writeable
            os.chmod(self.file, stat.S_IWRITE)
            f = open(self.file, 'w+')
            f.writelines('ciphered\n' + ciphered)
            f.close()
        else:
            f = open(self.file, 'w+')
            f.writelines('ciphered\n' + ciphered)
            f.close()
        # File is writeable, so make it read-only
        os.chmod(self.file, stat.S_IREAD)

    def set_new(self):
        self.pass_update = PyPherPass()
        self.pass_update.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pass_update.show()
        self.pass_update.send_pass.clicked.connect(self.update)

    def delete(self):
        result = message_alert('Do you really want\nto delete this File?', 'delete')
        if result:
            if not os.stat(self.file)[0] & stat.S_IWRITE:
                # File is read-only, so make it writeable
                os.chmod(self.file, stat.S_IWRITE)
            os.remove(str(self.file))
            self.hide()
            form.show()

    def closeEvent(self, event):
        result = message_alert('Do you want to Exit?', 'close')
        if result:
            event.accept()
        else:
            event.ignore()


class PyPherCipher(QtGui.QWidget, Cipher_GUI.Ui_cipher):
    def __init__(self):
        super(PyPherCipher, self).__init__()
        self.setupUi(self)
        self.path = os.getcwd()
        self.passw = ''
        self.file = ''
        self.go_back.clicked.connect(self.back)
        self.save.clicked.connect(self.save_file)
        self.choose.clicked.connect(self.choose_file)

    def back(self):
        result = message_alert('Any unsaved data will be lost\nDo you want to go back?', 'close')
        if result:
            self.hide()
            form.show()

    def save_file(self):
        if self.textEdit.toPlainText() != '' and self.textEdit.toPlainText() != 'Write Here...   ':
            self.pass_update = PyPherPass()
            self.pass_update.setWindowModality(QtCore.Qt.ApplicationModal)
            self.pass_update.show()
            self.pass_update.send_pass.clicked.connect(self.set)

    def set(self):
        if not self.pass_update.set_pass.text() == '':
            self.pass_update.close()
            if not os.path.exists(self.path + r'/PyPher-Vault/'):
                os.makedirs(os.path.join(self.path + r'/PyPher-Vault/'))
            self.dir = QtGui.QFileDialog(self, 'Save File')
            self.dir.setDirectory(self.path + r'/PyPher-Vault/')
            self.dir.setFilter('*.txt')
            self.dir.setAcceptMode(QtGui.QFileDialog.AcceptSave)
            self.dir.directoryEntered.connect(self.entered)
            if self.dir.exec_():
                selected = self.dir.selectedFiles()
                checker = os.path.splitext(str(selected[0]))
                if checker[1] != '.txt' and not os.path.exists(selected[0]):
                    self.file = selected[0] + '.txt'
                else:
                    self.file = selected[0]
            new_pass = self.pass_update.set_pass.text()
            if new_pass != '':
                self.pass_update.close()
                self.passw = new_pass
                self.cipher_data()
                message_alert('Password Protected File Saved', 'info')

    def entered(self, directory):
        if directory is not (self.path + r'/PyPher-Vault/'):
            self.dir.setDirectory(self.path + r'/PyPher-Vault/')

    def cipher_data(self):
        self.cipher = Cipher.Cipher(self.textEdit.toPlainText(), self.passw)
        ciphered = self.cipher.cipher()
        if not os.path.exists(self.file):
            f = open(self.file, 'w+')
            f.write('ciphered\n' + ciphered)
            f.close()
        else:
            if not os.stat(self.file)[0] & stat.S_IWRITE:
                # File is read-only, so make it writeable
                os.chmod(self.file, stat.S_IWRITE)
                f = open(self.file, 'w+')
                f.write('ciphered\n' + ciphered)
                f.close()
            else:
                f = open(self.file, 'w+')
                f.write('ciphered\n' + ciphered)
                f.close()
        # File is writeable, so make it read-only
        os.chmod(self.file, stat.S_IREAD)

    def choose_file(self):
        filter = 'Text File (*.txt);;PDF File (*.pdf);;Doc File (*.docx);;Any Other (*)'
        selected = QtGui.QFileDialog.getOpenFileName(self, 'Choose File', '.', filter)
        self.file = str(selected)
        filte_type = os.path.splitext(self.file)[1]
        if self.file != '':
            try:
                if filte_type == '.txt':
                    with open(self.file) as f:
                        self.textEdit.setText(f.read())
                elif filte_type == '.pdf':
                    self.textEdit.setText(getText(self.file))
                elif filte_type == '.docx':
                    self.textEdit.setText(textract.process(self.file))
                else:
                    with open(self.file) as f:
                        self.textEdit.setText(f.read())
            except:
                message_alert('This format is not supported', 'delete')

    def closeEvent(self, event):
        result = message_alert('Do you want to Exit?', 'close')
        if result:
            event.accept()
        else:
            event.ignore()


class PyPherMain(QtGui.QWidget, Main_GUI.Ui_PyPher):
    def __init__(self):
        super(PyPherMain, self).__init__()
        self.setupUi(self)
        self.path = os.getcwd()
        self.info = PyPherAbout()
        self.mess = PyPherMess()
        self.new = PyPherCipher()
        self.choose_file.clicked.connect(self.open_dir)
        self.about.clicked.connect(self.show_info)
        self.create_new.clicked.connect(self.new_file)

    def new_file(self):
        self.new.textEdit.setPlainText('Write Here...   ')
        form.hide()
        self.new.setWindowModality(QtCore.Qt.ApplicationModal)
        self.new.show()

    def show_info(self):
        self.info.setWindowModality(QtCore.Qt.ApplicationModal)
        self.info.show()

    def open_dir(self):
        if not os.path.exists(self.path + r'/PyPher-Vault/'):
            os.makedirs(os.path.join(self.path + r'/PyPher-Vault/'))
        self.file = QtGui.QFileDialog(self, 'Choose Files')
        self.file.setDirectory(self.path + r'/PyPher-Vault/')
        self.file.setFilter("Text files (*.txt)")
        self.file.directoryEntered.connect(self.entered)
        if self.file.exec_():
            selected_add = self.file.selectedFiles()
            self.file_open = selected_add[0]
            f = open(self.file_open, 'r')
            selected = f.read()
            if selected.split('\n', 1)[0] == 'ciphered':
                self.mess = PyPherMess(self.file_open)
                self.mess.data = selected.split('\n', 1)[1]
                self.mess.setWindowModality(QtCore.Qt.ApplicationModal)
                self.mess.show()
            else:
                self.dec = PyPherDecipher(self.file_open)
                self.hide()
                self.dec.show()
                self.dec.textEdit.setText(selected)

    def entered(self, directory):
        if not os.path.exists(self.path + r'/PyPher-Vault/'):
            os.makedirs(os.path.join(self.path + r'/PyPher-Vault/'))
        if directory is not (self.path + r'/PyPher-Vault/'):
            self.file.setDirectory(self.path + r'/PyPher-Vault/')

    def closeEvent(self, event):
        result = message_alert('Do you want to Exit?', 'close')
        if result:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    global form
    form = PyPherMain()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
