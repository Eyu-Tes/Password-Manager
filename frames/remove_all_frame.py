from main_win import *


class RemoveAllFrame:
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.displayed = False
        self.create_remove_all_frame()

    def create_remove_all_frame(self):
        self.ui.frameRemoveAll = QtWidgets.QFrame(self.ui.centralwidget)
        self.ui.frameRemoveAll.setGeometry(QtCore.QRect(280, 90, 271, 161))
        self.ui.frameRemoveAll.setStyleSheet("background: #0079bf;")
        self.ui.frameRemoveAll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ui.frameRemoveAll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.frameRemoveAll.setObjectName("frameRemoveAll")

        self.ui.labelRemoveAll = QtWidgets.QLabel(self.ui.frameRemoveAll)
        self.ui.labelRemoveAll.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ui.labelRemoveAll.setFont(font)
        self.ui.labelRemoveAll.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.labelRemoveAll.setObjectName("labelRemoveAll")

        self.ui.pushButtonRemoveAllOk = QtWidgets.QPushButton(self.ui.frameRemoveAll)
        self.ui.pushButtonRemoveAllOk.setGeometry(QtCore.QRect(47, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRemoveAllOk.setFont(font)
        self.ui.pushButtonRemoveAllOk.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRemoveAllOk.setObjectName("pushButtonRemoveAllOk")

        self.ui.pushButtonRemoveAllCancel = QtWidgets.QPushButton(self.ui.frameRemoveAll)
        self.ui.pushButtonRemoveAllCancel.setGeometry(QtCore.QRect(150, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(True)
        font.setWeight(75)
        self.ui.pushButtonRemoveAllCancel.setFont(font)
        self.ui.pushButtonRemoveAllCancel.setStyleSheet("background: #ffe01b;")
        self.ui.pushButtonRemoveAllCancel.setObjectName("pushButtonRemoveAllCancel")

        self.ui.labelRemoveAll.setText("Sure u want to delete all accounts ?")
        self.ui.pushButtonRemoveAllOk.setText("OK")
        self.ui.pushButtonRemoveAllCancel.setText("Cancel")

        self.ui.frameRemoveAll.hide()

    def display_remove_all_frame(self):
        self.ui.frameRemoveAll.show()
        self.displayed = True

    def hide_remove_all_frame(self):
        self.ui.frameRemoveAll.hide()
        self.displayed = False
