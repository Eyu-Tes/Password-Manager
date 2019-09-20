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

        self.ui.labelAdd = QtWidgets.QLabel(self.ui.frameAdd)
        self.ui.labelAdd.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelAdd.setFont(font)
        self.ui.labelAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelAdd.setObjectName("labelAdd")

        self.ui.lineEditAdd = QtWidgets.QLineEdit(self.ui.frameAdd)
        self.ui.lineEditAdd.setGeometry(QtCore.QRect(10, 60, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.ui.lineEditAdd.setFont(font)
        self.ui.lineEditAdd.setStyleSheet("background: #fff;\npadding: 1px 3px")
        self.ui.lineEditAdd.setObjectName("lineEditAdd")

        self.ui.labelAddError = QtWidgets.QLabel(self.ui.frameAdd)
        self.ui.labelAddError.setGeometry(QtCore.QRect(10, 80, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ui.labelAddError.setFont(font)
        self.ui.labelAddError.setStyleSheet("color: #ffe01b;")
        self.ui.labelAddError.setObjectName("labelAddError")

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

        self.ui.labelAdd.setText("Enter account name")
        self.ui.pushButtonAddOk.setText("OK")
        self.ui.pushButtonAddCancel.setText("Cancel")
        self.ui.labelAddError.setText('')

        self.ui.frameAdd.hide()

    def display_add_frame(self):
        self.ui.lineEditAdd.clear()
        self.ui.labelAddError.setText("")
        self.ui.lineEditAdd.setFocus()
        self.ui.frameAdd.show()
        self.displayed = True

    def hide_add_frame(self):
        self.ui.frameAdd.hide()
        self.displayed = False
