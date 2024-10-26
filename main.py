import os
import json
from tabulate import tabulate

# Use this to create exe
# python -m PyInstaller --onefile main.py

# CRUD
def account_create(username, password, riot_id, region, banned):
    global accounts
    account = [username, password, riot_id, region, banned]
    accounts.append(account)
    save_db()

def accounts_read():
    global accounts

    if len(accounts) == 0:
        print("No accounts to show")
    else:
        print("index\tusername\tpassword\triot id\t\t\tregion\tbanned")
        for index, account in enumerate(accounts):
            print(f"{index}\t{account[0]}\t{account[1]}\t{account[2]}\t{account[3]}\t{account[4]}")

def account_get(account_id):
    global accounts
    account = accounts[account_id]
    paste_to_clipboard(f"{account[0]}, {account[1]}")

def account_update(account_id, username="", password="", riot_id="", region="", banned=False):
    global accounts
    account_edit = accounts[account_id]

    if username != "":
        account_edit[0] = username
    if password != "":
        account_edit[1] = password
    if riot_id != "":
        account_edit[2] = riot_id
    if region != "":
        account_edit[3] = region
    if banned != account_edit[4]:
        account_edit[4] = banned

    accounts[account_id] = account_edit
    save_db()

def account_delete(account_id):
    global accounts
    del accounts[account_id]
    save_db()

# Database actions
def save_db():
    global accounts
    dump = json.dumps(accounts, indent=4)
    f = open(FILE, "w")
    f.write(dump)
    f.close

def load_db():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            undump = json.load(f)
            global accounts
            accounts = undump
    else:
        save_db()

# Constants and useful functions
FILE = "db.json"

def paste_to_clipboard(account):
    command = "echo | set /p null=" + account.strip() + "| clip"
    os.system(command)

def clear():
    os.system('cls')

# Account list structure: username, password, riotID, banned status
accounts = []

# Startup actions
load_db()

# GUI/CLI
while True:
    clear()
    print("1. create account\n2. read all accounts\n3. get account\n4. update account\n5. delete account\nuse 0 to exit")
    option = input()
    if option == "0":
        save_db()
        break

    elif option == "1":
        clear()
        username = input("insert username: ")
        password = input("insert password: ")
        riot_id = input("insert riot id: ")
        region = input("insert region: ")
        banned = input("is it banned? (y/n): ")
        if banned == "y":
            banned = True
        else:
            banned = False
        account_create(username, password, riot_id, region, banned)
        input("account created, press enter to return...")

    elif option == "2":
        clear()
        accounts_read()
        input("press enter to return...")

    elif option == "3":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert account id: "))
            account_get(account_id)
            input("account copied, press enter to return...")
        except (ValueError, IndexError):
            input("wrong input, press enter to return...")

    elif option == "4":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert id:"))
            username = input("insert new username (enter to skip) ")
            password = input("insert new password (enter to skip) ")
            riot_id = input("insert new riot id (enter to skip) ")
            region = input("insert new region (enter to skip) ")
            banned = input("banned? (y/n) (enter to skip) ")
            if banned == "y":
                banned = True
            else:
                banned = False
            account_update(account_id, username, password, riot_id, region, banned)
            input("account updated, press enter to return...")
        except (ValueError, IndexError):
            input("wrong input, press enter to return...")

    elif option == "5":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert account id: "))
            account_delete(account_id)
            input("account deleted, press enter to return...")
        except (ValueError, IndexError):
            input("wrong input, press enter to return...")

    else:
        print("not in range")