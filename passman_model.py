import sqlite3


def create_master_table():
    query = 'CREATE TABLE IF NOT EXISTS master (password VARCHAR(8))'
    cur.execute(query)


def create_accounts_table():
    query = """CREATE TABLE IF NOT EXISTS account_manager (
                account VARCHAR(255), 
                password VARCHAR(8)
            )"""
    cur.execute(query)


def insert_master_password(password):
    query = f"""INSERT INTO master (password) VALUES ('{password}')"""
    cur.execute(query)
    db.commit()


def get_master_password():
    query = 'SELECT password FROM master'
    cur.execute(query)
    password = cur.fetchone()
    return password[0] if password else ''


def get_accounts():
    query = 'SELECT account FROM account_manager'
    cur.execute(query)
    accounts = cur.fetchall()
    return accounts


def get_account_password(account):
    query = f"""SELECT password FROM account_manager
                WHERE account = '{account}'"""
    cur.execute(query)
    passwords = cur.fetchone()
    return passwords[0] if passwords else ''


def add_account(account, password='happypg'):
    query = f"""INSERT INTO account_manager (account, password) 
                VALUES ('{account}', '{password}')"""
    cur.execute(query)
    db.commit()


def rename_account(old_name, new_name):
    query = f"""UPDATE account_manager
                SET account = '{new_name}' WHERE account = '{old_name}'"""
    cur.execute(query)
    db.commit()


def remove_account(account):
    query = f"""DELETE FROM account_manager
                WHERE account = '{account}'"""
    cur.execute(query)
    db.commit()


def remove_all_accounts():
    query = f"""DELETE FROM account_manager"""
    cur.execute(query)
    db.commit()


db = sqlite3.connect('password manager.db')
cur = db.cursor()
create_master_table()
create_accounts_table()
