from main_win import *


class RenameFrame:
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.displayed = False
        self.create_rename_frame()

    def create_rename_frame(self):
        self.ui.frameRename = QtWidgets.QFrame(self.ui.centralwidget)
        self.ui.frameRename.setGeometry(QtCore.QRect(280, 90, 271, 161))
        self.ui.frameRename.setStyleSheet("background: #0079bf;")
        self.ui.frameRename.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.frameRename.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.frameRename.setObjectName("frameRename")

        self.ui.labelRename = QtWidgets.QLabel(self.ui.frameRename)
        self.ui.labelRename.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelRename.setFont(font)
        self.ui.labelRename.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelRename.setObjectName("labelRename")

        self.ui.lineEditRename = QtWidgets.QLineEdit(self.ui.frameRename)
        self.ui.lineEditRename.setGeometry(QtCore.QRect(10, 60, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.ui.lineEditRename.setFont(font)
        self.ui.lineEditRename.setStyleSheet("background: #fff;\npadding: 1px 3px")
        self.ui.lineEditRename.setObjectName("lineEditRename")

        self.ui.labelRenameError = QtWidgets.QLabel(self.ui.frameRename)
        self.ui.labelRenameError.setGeometry(QtCore.QRect(10, 80, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ui.labelRenameError.setFont(font)
        self.ui.labelRenameError.setStyleSheet("color: #ffe01b;")
        self.ui.labelRenameError.setObjectName("labelRenameError")

        self.ui.pushButtonRenameOk = QtWidgets.QPushButton(self.ui.frameRename)
        self.ui.pushButtonRenameOk.setGeometry(QtCore.QRect(47, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRenameOk.setFont(font)
        self.ui.pushButtonRenameOk.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRenameOk.setObjectName("pushButtonRenameOk")

        self.ui.pushButtonRenameCancel = QtWidgets.QPushButton(self.ui.frameRename)
        self.ui.pushButtonRenameCancel.setGeometry(QtCore.QRect(150, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRenameCancel.setFont(font)
        self.ui.pushButtonRenameCancel.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRenameCancel.setObjectName("pushButtonRenameCancel")

        self.ui.pushButtonRenameOk.setText("OK")
        self.ui.pushButtonRenameCancel.setText("Cancel")
        self.ui.labelRenameError.setText('')

        self.ui.frameRename.hide()

    def display_rename_frame(self):
        self.ui.lineEditRename.clear()
        self.ui.labelRenameError.setText("")
        self.ui.lineEditRename.setFocus()
        self.ui.frameRename.show()
        self.displayed = True

    def hide_rename_frame(self):
        self.ui.frameRename.hide()
        self.displayed = False
