import os
import json
import tkinter

# CRUD
def account_create(username, password, riotID, region, banned=False):
    account = [username, password, riotID, region, banned]
    accounts.append(account)
    save_db()

def accounts_read():
    global accounts
    print("index\tusername\tpassword\triot id\tregion\t\t\tbanned")
    for index, account in enumerate(accounts):
        print(f"{index}\t{account[0]}\t{account[1]}\t{account[2]}\t{account[3]}\t{account[4]}")

def account_get(account_id):
    global accounts
    account = accounts[account_id]
    paste_to_clipboard(f"{account[0]}, {account[1]}")

def account_update(account_id, username="", password="", riotid="", region="", banned=False):
    global accounts
    account_edit = accounts[account_id]
    
    if username != "":
        account_edit[0] = username
    if password != "":
        account_edit[1] = password
    if riotid != "":
        account_edit[2] = riotid
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

# DB actions
def save_db():
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
        accounts = []
        save_db()
        
# Misc
FILE = "db.json"

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

#account list structure: username, password, riotID, banned status
accounts = []

#GUI
root = tkinter.Tk()

#window settings
window_height = 800
window_width = 800

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = int((screen_height/2) - (window_height/2))
y = int((screen_width/2) - (window_width/2))

root.geometry(f"{window_width}x{window_height}+{y}+{x}")

#widget setup

#widget packaging

root.mainloop()