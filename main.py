import os

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

# CRUD
def account_create(username, password, riotID, banned=0):
    account = [username, password, riotID, banned]
    return account

def account_read():
    pass

def account_update():
    pass

def account_delete():
    pass

#account list structure: username, password, riotID, banned status
accounts = []