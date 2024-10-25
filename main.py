import os
import json

# CRUD
def account_create(username, password, riotID, banned=0):
    account = [username, password, riotID, banned]
    accounts.append(account)

def account_read():
    pass

def account_update():
    pass

def account_delete():
    pass

# DB actions
def save_db():
    dump = json.dumps(accounts, indent=4)
    f = open(FILE, "w")
    f.write(dump)
    f.close

def load_db():
    f = open(FILE, "r")
    undump = json.load(f)
    global accounts
    accounts = undump

# Misc
FILE = "db.json"

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

#account list structure: username, password, riotID, banned status
accounts = []