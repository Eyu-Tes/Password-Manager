import sys
import pyperclip
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import welcome_win
import main_win
import passman_model
from add_frame import AddFrame
from change_frame import ChangeFrame
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
        self.password = passman_model.get_master_password()
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
                passman_model.insert_master_password(self.password)
                self.go_to_main_window()
        else:
            if password != self.password:
                self.ui.labelPError.setText('Wrong password!')
            else:
                self.go_to_main_window()

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
        self.change = ChangeFrame(self.ui)
        self.rename = RenameFrame(self.ui)
        self.remove = RemoveFrame(self.ui)
        self.remove_all = RemoveAllFrame(self.ui)

        self.current_item = None
        self.ui.labelNoItem.hide()
        self.populate_list()

        self.ui.pushButtonCopy.clicked.connect(self.copy_password)
        self.ui.pushButtonAdd.clicked.connect(self.show_add_frame)
        self.ui.pushButtonChange.clicked.connect(self.show_change_frame)
        self.ui.pushButtonRename.clicked.connect(self.show_rename_frame)
        self.ui.pushButtonRemove.clicked.connect(self.show_remove_frame)
        self.ui.pushButtonRemoveAll.clicked.connect(self.show_remove_all_frame)

        self.ui.listWidgetAccounts.itemClicked.connect(self.item_clicked)

    def populate_list(self):
        items = passman_model.get_accounts()
        for item in items:
            self.ui.listWidgetAccounts.addItem(item[0])

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

# ----------------------------- Copy Password ---------------------------------
    def copy_password(self):
        item = self.get_selected_item()
        if item:
            self.current_item = item
            name = self.current_item.text()
            self.ui.listWidgetAccounts.setCurrentRow(-1)
            pwd = passman_model.get_account_password(name)
            pyperclip.copy(pwd)
            self.ui.labelStatus.setText(f'{name} password copied to clip board!')
        else:
            self.ui.labelNoItem.show()
# -----------------------------------------------------------------------------

# ----------------------------- Add Frame -------------------------------------
    def show_add_frame(self):
        if not self.add.displayed:
            self.ui.labelStatus.setText('')
            self.ui.labelNoItem.hide()
            self.add.display_add_frame()
            self.add.ui.pushButtonAddOk.clicked.connect(self.add_item_commit)
            self.add.ui.pushButtonAddCancel.clicked.connect(self.add_item_cancel)

    def add_item_commit(self):
        name = self.add.ui.lineEditAddAccount.text()
        pwd = self.add.ui.lineEditAddPassword.text()
        if name and pwd:
            # if account is already found in list, don't add it
            if name.lower() in self.get_items():
                self.add.ui.labelAddError.setText('Account Already exists!')
            else:
                self.add.ui.labelAddError.setText('')
                self.ui.listWidgetAccounts.addItem(name)
                passman_model.add_account(name, pwd)
                self.add.hide_add_frame()
                self.ui.labelStatus.setText(f'{name} added to account store!')

            self.add.ui.lineEditAddAccount.clear()
            self.add.ui.lineEditAddPassword.clear()
            self.add.ui.lineEditAddAccount.setFocus()
        elif not name:
            self.add.ui.lineEditAddAccount.setFocus()
        elif not pwd:
            self.add.ui.lineEditAddPassword.setFocus()

    def add_item_cancel(self):
        self.add.hide_add_frame()
# -----------------------------------------------------------------------------

# -------------------------- Change Frame -------------------------------------
    def show_change_frame(self):
        item = self.get_selected_item()
        if item:
            self.current_item = item
            if not self.change.displayed:
                self.ui.labelStatus.setText('')
                self.ui.labelNoItem.hide()
                self.change.ui.labelChange.setText(
                    f'Change {self.current_item.text()} password to - ')
                self.change.display_change_frame()
                self.change.ui.pushButtonChangeOk.clicked.connect(self.change_item_commit)
                self.change.ui.pushButtonChangeCancel.clicked.connect(self.change_item_cancel)
        else:
            self.ui.labelNoItem.show()

    def change_item_commit(self):
        cur_row = self.ui.listWidgetAccounts.row(self.current_item)
        item_name = self.current_item.text()
        new_password = self.change.ui.lineEditChange.text()
        if new_password:
            # Make sure next item isn't selected by default, after change.
            self.ui.listWidgetAccounts.setCurrentRow(-1)
            passman_model.change_account_password(item_name, new_password)
            self.change.hide_change_frame()
            self.ui.labelStatus.setText(f'{item_name} password changed!')
            self.change.ui.lineEditChange.clear()
            self.change.ui.lineEditChange.setFocus()

    def change_item_cancel(self):
        self.change.hide_change_frame()
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
                passman_model.rename_account(item_name, new_name)
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
        passman_model.remove_account(item_name)
        self.remove.hide_remove_frame()
        self.ui.labelStatus.setText(f'{item_name} removed from account store!')

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
        passman_model.remove_all_accounts()
        self.remove_all.hide_remove_all_frame()
        self.ui.labelStatus.setText('Account store is empty!')

    def remove_all_items_cancel(self):
        self.remove_all.hide_remove_all_frame()
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WelcomeWindow()
    sys.exit(app.exec_())
