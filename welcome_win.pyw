# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 459)
        MainWindow.setMinimumSize(QtCore.QSize(470, 459))
        MainWindow.setMaximumSize(QtCore.QSize(470, 459))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: #008cba;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 160, 271, 241))
        self.frame_2.setStyleSheet("background: #cfcfcf;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelPassword = QtWidgets.QLabel(self.frame_2)
        self.labelPassword.setGeometry(QtCore.QRect(20, 40, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setText("")
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditPassword = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditPassword.setGeometry(QtCore.QRect(20, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background: #fff;\n"
"padding: 3px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonPOK = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonPOK.setGeometry(QtCore.QRect(90, 180, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        self.pushButtonPOK.setFont(font)
        self.pushButtonPOK.setStyleSheet("background-color: #ffe01b;\n"
"")
        self.pushButtonPOK.setObjectName("pushButtonPOK")
        self.labelPError = QtWidgets.QLabel(self.frame_2)
        self.labelPError.setGeometry(QtCore.QRect(20, 116, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(9)
        self.labelPError.setFont(font)
        self.labelPError.setStyleSheet("color: #f44336;")
        self.labelPError.setText("")
        self.labelPError.setObjectName("labelPError")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 471, 80))
        self.frame.setStyleSheet("background-color: #ffe01b;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelTitle_2 = QtWidgets.QLabel(self.frame)
        self.labelTitle_2.setGeometry(QtCore.QRect(50, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setStyleSheet("background: #181818;\n"
"color: #cfcfcf;")
        self.labelTitle_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitle_2.setWordWrap(False)
        self.labelTitle_2.setObjectName("labelTitle_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassMan"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Password - 4 to 8 characters long"))
        self.pushButtonPOK.setText(_translate("MainWindow", "OK"))
        self.pushButtonPOK.setShortcut(_translate("MainWindow", "Return"))
        self.labelTitle_2.setText(_translate("MainWindow", "         PassMan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

