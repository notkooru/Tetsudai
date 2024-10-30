import os
import json
import tkinter

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

# GUI
root = tkinter.Tk()

# Window settings
window_height = 500
window_width = 650

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = int((screen_height/2) - (window_height/2))
y = int((screen_width/2) - (window_width/2))

root.geometry(f"{window_width}x{window_height}+{y}+{x}")

# Widget setup

# Widget packaging

root.mainloop()