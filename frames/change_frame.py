from main_win import *


class ChangeFrame:
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.displayed = False
        self.create_change_frame()

    def create_change_frame(self):
        self.ui.frameChange = QtWidgets.QFrame(self.ui.centralwidget)
        self.ui.frameChange.setGeometry(QtCore.QRect(280, 90, 271, 161))
        self.ui.frameChange.setStyleSheet("background: #0079bf;")
        self.ui.frameChange.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.frameChange.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.frameChange.setObjectName("frameChange")

        self.ui.labelChange = QtWidgets.QLabel(self.ui.frameChange)
        self.ui.labelChange.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelChange.setFont(font)
        self.ui.labelChange.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelChange.setObjectName("labelChange")

        self.ui.lineEditChange = QtWidgets.QLineEdit(self.ui.frameChange)
        self.ui.lineEditChange.setGeometry(QtCore.QRect(10, 60, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.ui.lineEditChange.setFont(font)
        self.ui.lineEditChange.setStyleSheet(
            "background: #fff;\npadding: 1px 3px")
        self.ui.lineEditChange.setObjectName("lineEditChange")

        self.ui.pushButtonChangeOk = QtWidgets.QPushButton(self.ui.frameChange)
        self.ui.pushButtonChangeOk.setGeometry(QtCore.QRect(47, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonChangeOk.setFont(font)
        self.ui.pushButtonChangeOk.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonChangeOk.setObjectName("pushButtonChangeOk")

        self.ui.pushButtonChangeCancel = QtWidgets.QPushButton(self.ui.frameChange)
        self.ui.pushButtonChangeCancel.setGeometry(QtCore.QRect(150, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonChangeCancel.setFont(font)
        self.ui.pushButtonChangeCancel.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonChangeCancel.setObjectName("pushButtonChangeCancel")

        self.ui.pushButtonChangeOk.setText("OK")
        self.ui.pushButtonChangeCancel.setText("Cancel")

        self.ui.frameChange.hide()

    def display_change_frame(self):
        self.ui.frameChange.show()
        self.displayed = True

    def hide_change_frame(self):
        self.ui.frameChange.hide()
        self.displayed = False
