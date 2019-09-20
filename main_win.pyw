# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 511)
        MainWindow.setMinimumSize(QtCore.QSize(562, 511))
        MainWindow.setMaximumSize(QtCore.QSize(562, 511))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: #cfcfcfcf;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameTitle = QtWidgets.QFrame(self.centralwidget)
        self.frameTitle.setGeometry(QtCore.QRect(0, 0, 571, 80))
        self.frameTitle.setStyleSheet("background-color: #ffe01b;")
        self.frameTitle.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTitle.setObjectName("frameTitle")
        self.labelTitle = QtWidgets.QLabel(self.frameTitle)
        self.labelTitle.setGeometry(QtCore.QRect(110, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background: #181818;\n"
"color: #cfcfcf;")
        self.labelTitle.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitle.setWordWrap(False)
        self.labelTitle.setObjectName("labelTitle")
        self.listWidgetAccounts = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetAccounts.setGeometry(QtCore.QRect(10, 90, 256, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidgetAccounts.setFont(font)
        self.listWidgetAccounts.setStyleSheet("background: #181818;\n"
"color: #fff;\n"
"padding: 3px;")
        self.listWidgetAccounts.setFrameShape(QtWidgets.QFrame.Panel)
        self.listWidgetAccounts.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidgetAccounts.setObjectName("listWidgetAccounts")
        self.labelNoItem = QtWidgets.QLabel(self.centralwidget)
        self.labelNoItem.setGeometry(QtCore.QRect(300, 170, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(16)
        self.labelNoItem.setFont(font)
        self.labelNoItem.setStyleSheet("color: #f44336;\n"
"background-color: #cfcfcf;\n"
"padding: 3px;")
        self.labelNoItem.setObjectName("labelNoItem")
        self.pushButtonCopy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCopy.setGeometry(QtCore.QRect(280, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCopy.setFont(font)
        self.pushButtonCopy.setStyleSheet("background:  #008cba;\n"
"color: #fff;")
        self.pushButtonCopy.setObjectName("pushButtonCopy")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(430, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("background:  #008cba;\n"
"color: #fff;")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonRename = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRename.setGeometry(QtCore.QRect(430, 340, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRename.setFont(font)
        self.pushButtonRename.setStyleSheet("background: #008cba;\n"
"color: #fff;")
        self.pushButtonRename.setObjectName("pushButtonRename")
        self.pushButtonRemove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemove.setGeometry(QtCore.QRect(280, 410, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRemove.setFont(font)
        self.pushButtonRemove.setStyleSheet("background: #008cba;\n"
"color: #fff;")
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.pushButtonRemoveAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveAll.setGeometry(QtCore.QRect(430, 410, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRemoveAll.setFont(font)
        self.pushButtonRemoveAll.setStyleSheet("background: #008cba;\n"
"color: #fff;")
        self.pushButtonRemoveAll.setObjectName("pushButtonRemoveAll")
        self.pushButtonChange = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonChange.setGeometry(QtCore.QRect(280, 340, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonChange.setFont(font)
        self.pushButtonChange.setStyleSheet("background:  #008cba;\n"
"color: #fff;")
        self.pushButtonChange.setObjectName("pushButtonChange")
        self.labelStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(0, 480, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet("background: #ffe01b;\n"
"color: #181818;\n"
"padding: 3px 5px;")
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassMan"))
        self.labelTitle.setText(_translate("MainWindow", "         PassMan"))
        self.labelNoItem.setText(_translate("MainWindow", "No account selected!"))
        self.pushButtonCopy.setText(_translate("MainWindow", "Copy \n"
"Password"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Add \n"
"Account"))
        self.pushButtonRename.setText(_translate("MainWindow", "Rename \n"
"Account"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove \n"
"Account"))
        self.pushButtonRemoveAll.setText(_translate("MainWindow", "Remove All \n"
"Accounts"))
        self.pushButtonChange.setText(_translate("MainWindow", "Change \n"
"Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
