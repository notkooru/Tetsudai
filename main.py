import os

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

# CRUD
def account_create():
    pass

def account_read():
    pass

def account_update():
    pass

def account_delete():
    pass