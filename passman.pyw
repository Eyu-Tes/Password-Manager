import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import welcome_win
import main_win
from add_frame import AddFrame
from rename_frame import RenameFrame
from remove_frame import RemoveFrame
from remove_all_frame import RemoveAllFrame


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

        self.add = AddFrame(self.ui)
        self.rename = RenameFrame(self.ui)
        self.remove = RemoveFrame(self.ui)
        self.remove_all = RemoveAllFrame(self.ui)

        self.current_item = None
        self.ui.labelNoItem.hide()
        self.populate_list()

        self.ui.pushButtonAdd.clicked.connect(self.show_add_frame)
        self.ui.pushButtonRename.clicked.connect(self.show_rename_frame)
        self.ui.pushButtonRemove.clicked.connect(self.show_remove_frame)
        self.ui.pushButtonRemoveAll.clicked.connect(self.show_remove_all_frame)

        self.ui.listWidgetAccounts.itemClicked.connect(self.item_clicked)

    def populate_list(self):
        items = MainWindow.read_from_db()
        for item in items:
            self.ui.listWidgetAccounts.addItem(item.strip())

    def get_items(self):
        # Uses generator to return the item texts in the list widgets
        for i in range(self.ui.listWidgetAccounts.count()):
            item_name = self.ui.listWidgetAccounts.item(i).text().lower()
            yield item_name

    def get_selected_item(self):
        list_items = self.ui.listWidgetAccounts.selectedItems()
        if not list_items:
            return
        return list_items[0]

    def item_clicked(self):
        if self.ui.labelNoItem.isVisible():
            self.ui.labelNoItem.hide()

# ----------------------------- Add Frame -------------------------------------
    def show_add_frame(self):
        if not self.add.displayed:
            self.ui.labelStatus.setText('')
            self.ui.labelNoItem.hide()
            self.add.display_add_frame()
            self.add.ui.pushButtonAddOk.clicked.connect(self.add_item_commit)
            self.add.ui.pushButtonAddCancel.clicked.connect(self.add_item_cancel)

    def add_item_commit(self):
        name = self.add.ui.lineEditAdd.text()
        if name:
            # if account is already found in list, don't add it
            if name.lower() in self.get_items():
                self.add.ui.labelAddError.setText('Account Already exists!')
            else:
                self.add.ui.labelAddError.setText('')
                self.ui.listWidgetAccounts.addItem(name)
                MainWindow.add_to_db(name)
                self.add.hide_add_frame()
                self.ui.labelStatus.setText(f'{name} added to food store!')
        self.add.ui.lineEditAdd.clear()
        self.add.ui.lineEditAdd.setFocus()

    def add_item_cancel(self):
        self.add.hide_add_frame()
# -----------------------------------------------------------------------------

# -------------------------- Rename Frame -------------------------------------
    def show_rename_frame(self):
        item = self.get_selected_item()
        if item:
            self.current_item = item
            if not self.rename.displayed:
                self.ui.labelStatus.setText('')
                self.ui.labelNoItem.hide()
                self.rename.ui.labelRename.setText(
                    f'Rename {self.current_item.text()} to - ')
                self.rename.display_rename_frame()
                self.rename.ui.pushButtonRenameOk.clicked.connect(
                    self.rename_item_commit)
                self.rename.ui.pushButtonRenameCancel.clicked.connect(
                    self.rename_item_cancel)
            else:
                print('Already Rename')
        else:
            self.ui.labelNoItem.show()

    def rename_item_commit(self):
        cur_row = self.ui.listWidgetAccounts.row(self.current_item)
        item_name = self.current_item.text()
        new_name = self.rename.ui.lineEditRename.text()
        if new_name:
            # if account is already found in list, don't add it
            if new_name.lower() in self.get_items():
                self.rename.ui.labelRenameError.setText('Account Already exists!')
            else:
                self.rename.ui.labelRenameError.setText('')
                self.ui.listWidgetAccounts.takeItem(cur_row)
                self.ui.listWidgetAccounts.insertItem(cur_row, QListWidgetItem(new_name))
                # Make sure next item isn't selected by default, after rename.
                self.ui.listWidgetAccounts.setCurrentRow(-1)
                MainWindow.rename_in_db(item_name, new_name)
                self.rename.hide_rename_frame()
                self.ui.labelStatus.setText(f'{item_name} renamed to {new_name}!')
        self.rename.ui.lineEditRename.clear()
        self.rename.ui.lineEditRename.setFocus()

    def rename_item_cancel(self):
        self.rename.hide_rename_frame()
# -----------------------------------------------------------------------------

# -------------------------- Remove Frame -------------------------------------
    def show_remove_frame(self):
        item = self.get_selected_item()
        if item:
            self.current_item = item
            if not self.remove.displayed:
                self.ui.labelStatus.setText('')
                self.ui.labelNoItem.hide()
                self.remove.ui.labelRemove.setText(
                    f'Sure u want to remove {self.current_item.text()} ?')
                self.remove.display_remove_frame()
                self.remove.ui.pushButtonRemoveOk.clicked.connect(
                    self.remove_item_commit)
                self.remove.ui.pushButtonRemoveCancel.clicked.connect(
                    self.remove_item_cancel)
        else:
            self.ui.labelNoItem.show()

    def remove_item_commit(self):
        item_name = self.current_item.text()
        self.ui.listWidgetAccounts.takeItem(self.ui.listWidgetAccounts.row(self.current_item))
        # Make sure the next item is not selected by default, after deletion.
        self.ui.listWidgetAccounts.setCurrentRow(-1)
        MainWindow.remove_from_db(item_name)
        self.remove.hide_remove_frame()
        self.ui.labelStatus.setText(f'{item_name} removed food store!')

    def remove_item_cancel(self):
        self.remove.hide_remove_frame()
# -----------------------------------------------------------------------------

# ------------------------ Remove All Frame ---------------------------------
    def show_remove_all_frame(self):
        if self.ui.listWidgetAccounts.count() > 0:
            if not self.remove_all.displayed:
                self.ui.labelStatus.setText('')
                self.ui.labelNoItem.hide()
                self.remove_all.display_remove_all_frame()
                self.remove_all.ui.pushButtonRemoveAllOk.clicked.connect(
                    self.remove_all_items_commit)
                self.remove_all.ui.pushButtonRemoveAllCancel.clicked.connect(
                    self.remove_all_items_cancel)
        else:
            self.ui.labelNoItem.show()

    def remove_all_items_commit(self):
        self.ui.listWidgetAccounts.clear()
        MainWindow.remove_all_from_db()
        self.remove_all.hide_remove_all_frame()
        self.ui.labelStatus.setText('Account store is empty!')

    def remove_all_items_cancel(self):
        self.remove_all.hide_remove_all_frame()
# -----------------------------------------------------------------------------

    @staticmethod
    def read_from_db():
        with open('acc_passwords.txt', 'r') as f:
            content = f.readlines()
        return content

    @staticmethod
    def add_to_db(content):
        with open('acc_passwords.txt', 'a') as f:
            f.write(f'{content}\n')

    @staticmethod
    def rename_in_db(old_content, new_content):
        with open('acc_passwords.txt') as of, open('new.txt', 'w') as nf:
            for old_line in of.readlines():
                if not (old_line.strip().lower() == old_content.lower()):
                    nf.write(old_line)
                else:
                    nf.write(f'{new_content}\n')
        os.remove('acc_passwords.txt')
        os.rename('new.txt', 'acc_passwords.txt')

    @staticmethod
    def remove_from_db(content):
        with open('acc_passwords.txt') as of, open('new.txt', 'w') as nf:
            for old_line in of.readlines():
                if not (old_line.strip().lower() == content.lower()):
                    nf.write(old_line)
        os.remove('acc_passwords.txt')
        os.rename('new.txt', 'acc_passwords.txt')

    @staticmethod
    def remove_all_from_db():
        # with open('food_items.txt', 'w') as f:
        #         f.write()
        # erase all the contents of the text file
        open('acc_passwords.txt', 'w').close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WelcomeWindow()
    sys.exit(app.exec_())
