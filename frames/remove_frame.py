from main_win import *


class RemoveFrame:
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.displayed = False
        self.create_remove_frame()

    def create_remove_frame(self):
        self.ui.frameRemove = QtWidgets.QFrame(self.ui.centralwidget)
        self.ui.frameRemove.setGeometry(QtCore.QRect(280, 90, 271, 161))
        self.ui.frameRemove.setStyleSheet("background: #0079bf;")
        self.ui.frameRemove.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.frameRemove.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.frameRemove.setObjectName("frameRemove")

        self.ui.labelRemove = QtWidgets.QLabel(self.ui.frameRemove)
        self.ui.labelRemove.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelRemove.setFont(font)
        self.ui.labelRemove.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelRemove.setObjectName("labelRemove")

        self.ui.pushButtonRemoveOk = QtWidgets.QPushButton(self.ui.frameRemove)
        self.ui.pushButtonRemoveOk.setGeometry(QtCore.QRect(47, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRemoveOk.setFont(font)
        self.ui.pushButtonRemoveOk.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRemoveOk.setObjectName("pushButtonRemoveOk")

        self.ui.pushButtonRemoveCancel = QtWidgets.QPushButton(self.ui.frameRemove)
        self.ui.pushButtonRemoveCancel.setGeometry(QtCore.QRect(150, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRemoveCancel.setFont(font)
        self.ui.pushButtonRemoveCancel.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRemoveCancel.setObjectName("pushButtonRemoveCancel")

        self.ui.pushButtonRemoveOk.setText("OK")
        self.ui.pushButtonRemoveCancel.setText("Cancel")

        self.ui.frameRemove.hide()

    def display_remove_frame(self):
        self.ui.frameRemove.show()
        self.displayed = True

    def hide_remove_frame(self):
        self.ui.frameRemove.hide()
        self.displayed = False
