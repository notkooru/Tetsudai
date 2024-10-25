import os

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

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
    pass

def load_db():
    pass

#account list structure: username, password, riotID, banned status
accounts = []