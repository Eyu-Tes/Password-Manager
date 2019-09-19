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
        MainWindow.resize(562, 486)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: #008cba;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 571, 80))
        self.frame_2.setStyleSheet("background-color: #ffe01b;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelTitle = QtWidgets.QLabel(self.frame_2)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassMan"))
        self.labelTitle.setText(_translate("MainWindow", "         PassMan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
