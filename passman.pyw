import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import welcome_win
import main_win


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = welcome_win.Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_window = None
        self.password = ''

        new_user = self.first_time()
        if new_user:
            self.ui.labelPassword.setText('Create Master Password')
        else:
            self.ui.labelPassword.setText('Enter Password')

        self.ui.pushButtonPOK.clicked.connect(self.validate)
        self.show()

    def first_time(self):
        self.retrieve_master_password()
        new_user = False if self.password else True
        return new_user

    def validate(self):
        password = self.ui.lineEditPassword.text()
        if self.first_time():
            if len(password) > 8:
                self.ui.labelPError.setText('Maximum length is 8 characters')
            elif len(password) < 4:
                self.ui.labelPError.setText('Minimum length is 4 characters')
            else:
                self.password = password
                self.insert_master_password()
                self.go_to_main_window()
        else:
            if password != self.password:
                self.ui.labelPError.setText('Wrong password!')
            else:
                self.go_to_main_window()

    def insert_master_password(self):
        with open('master_password.txt', 'w') as f:
            f.write(self.password)

    def retrieve_master_password(self):
        with open('master_password.txt') as f:
            self.password = f.read()

    def go_to_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_win.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WelcomeWindow()
    sys.exit(app.exec_())
