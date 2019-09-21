from main_win import *


class AddFrame:
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.displayed = False
        self.create_add_frame()

    def create_add_frame(self):
        self.ui.frameAdd = QtWidgets.QFrame(self.ui.centralwidget)
        self.ui.frameAdd.setGeometry(QtCore.QRect(280, 90, 271, 161))
        self.ui.frameAdd.setStyleSheet("background: #0079bf;")
        self.ui.frameAdd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.frameAdd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.frameAdd.setObjectName("frameAdd")

        self.ui.labelAddAccount = QtWidgets.QLabel(self.ui.frameAdd)
        self.ui.labelAddAccount.setGeometry(QtCore.QRect(10, 5, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelAddAccount.setFont(font)
        self.ui.labelAddAccount.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelAddAccount.setObjectName("labelAddAccount")

        self.ui.lineEditAddAccount = QtWidgets.QLineEdit(self.ui.frameAdd)
        self.ui.lineEditAddAccount.setGeometry(QtCore.QRect(10, 30, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.ui.lineEditAddAccount.setFont(font)
        self.ui.lineEditAddAccount.setStyleSheet(
            "background: #fff;\npadding: 1px 3px")
        self.ui.lineEditAddAccount.setObjectName("lineEditAddAccount")

        self.ui.labelAddError = QtWidgets.QLabel(self.ui.frameAdd)
        self.ui.labelAddError.setGeometry(QtCore.QRect(10, 50, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ui.labelAddError.setFont(font)
        self.ui.labelAddError.setStyleSheet("color: #ffe01b;")
        self.ui.labelAddError.setObjectName("labelAddError")

        self.ui.labelAddPassword = QtWidgets.QLabel(self.ui.frameAdd)
        self.ui.labelAddPassword.setGeometry(QtCore.QRect(10, 65, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelAddPassword.setFont(font)
        self.ui.labelAddPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelAddPassword.setObjectName("labelAddPassword")

        self.ui.lineEditAddPassword = QtWidgets.QLineEdit(self.ui.frameAdd)
        self.ui.lineEditAddPassword.setGeometry(QtCore.QRect(10, 90, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.ui.lineEditAddPassword.setFont(font)
        self.ui.lineEditAddPassword.setStyleSheet(
            "background: #fff;\npadding: 1px 3px")
        self.ui.lineEditAddPassword.setObjectName("lineEditAddPassword")

        self.ui.pushButtonAddOk = QtWidgets.QPushButton(self.ui.frameAdd)
        self.ui.pushButtonAddOk.setGeometry(QtCore.QRect(47, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonAddOk.setFont(font)
        self.ui.pushButtonAddOk.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonAddOk.setObjectName("pushButtonAddOk")

        self.ui.pushButtonAddCancel = QtWidgets.QPushButton(self.ui.frameAdd)
        self.ui.pushButtonAddCancel.setGeometry(QtCore.QRect(150, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonAddCancel.setFont(font)
        self.ui.pushButtonAddCancel.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonAddCancel.setObjectName("pushButtonAddCancel")

        self.ui.labelAddAccount.setText("Enter account name")
        self.ui.labelAddPassword.setText("Enter account password")
        self.ui.pushButtonAddOk.setText("OK")
        self.ui.pushButtonAddCancel.setText("Cancel")
        self.ui.labelAddError.setText('')

        self.ui.frameAdd.hide()

    def display_add_frame(self):
        self.ui.lineEditAddAccount.clear()
        self.ui.lineEditAddPassword.clear()
        self.ui.labelAddError.setText("")
        self.ui.lineEditAddAccount.setFocus()
        self.ui.frameAdd.show()
        self.displayed = True

    def hide_add_frame(self):
        self.ui.frameAdd.hide()
        self.displayed = False
