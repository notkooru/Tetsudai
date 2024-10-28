import os
import json
from tabulate import tabulate

# Use this to create exe
# python -m PyInstaller --onefile main.py

# CRUD
def account_create(username, password, riot_id, region, banned):
    global accounts
    account = {"username" : username, 
               "password" : password, 
               "riot id" : riot_id,
               "region" : region,
               "banned status" : banned}
    accounts.append(account)
    db_save()

def accounts_read():
    global accounts
    
    accounts_formated = []

    for index, account in enumerate(accounts):
        accounts_formated.append([index, account["username"], account["password"], account["riot id"], account["region"], account["banned status"]])

    headers = ["id", "username", "password", "riot id", "region", "banned status"]

    if len(accounts) == 0:
        print("No accounts to show")
    else:
        print(tabulate(accounts_formated, headers=headers, tablefmt="grid"))

def account_get(account_id):
    global accounts
    account = accounts[account_id]
    paste_to_clipboard(f"{account["username"]}, {account["password"]}")

def account_update(account_id, username="", password="", riot_id="", region="", banned=False):
    global accounts
    account_edit = accounts[account_id]

    if username != "":
        account_edit["username"] = username
    if password != "":
        account_edit["password"] = password
    if riot_id != "":
        account_edit["riot id"] = riot_id
    if region != "":
        account_edit["region"] = region
    if banned != account_edit["banned status"]:
        account_edit["banned status"] = banned

    accounts[account_id] = account_edit
    db_save()

def account_delete(account_id):
    global accounts
    del accounts[account_id]
    db_save()

# Database actions
def db_save():
    global accounts
    dump = json.dumps(accounts, indent=4)
    f = open(FILE, "w")
    f.write(dump)
    f.close

def db_load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            undump = json.load(f)
            global accounts
            accounts = undump
            f.close()
    else:
        db_save()

def db_convert():
    global accounts
    accounts_converted = []
    for account in accounts:
        account_converted = {"username" : account[0],
                             "password" : account[1],
                             "riot id" : account[2],
                             "region" : account[3],
                             "banned status" : account[4]}
        accounts_converted.append(account_converted)
    accounts = accounts_converted
    db_save()

# Constants and useful functions
FILE = "db.json"

def paste_to_clipboard(account):
    command = "echo | set /p null=" + account.strip() + "| clip"
    os.system(command)

def clear():
    os.system('cls')

# Account dict structure: username, password, riot id, region, banned status
accounts = []

# Startup actions
db_load()

# Database converter
if len(accounts) > 0 and type(accounts[0]) == list:
    db_convert()

# GUI/CLI
while True:
    clear()
    print("1. create account\n2. read all accounts\n3. get account\n4. update account\n5. delete account\nuse 0 to exit")
    option = input()
    if option == "0":
        db_save()
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
        input("account created, press enter to return... ")

    elif option == "2":
        clear()
        accounts_read()
        input("press enter to return... ")

    elif option == "3":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert account id: "))
            account_get(account_id)
            input("account copied, press enter to return... ")
        except (ValueError, IndexError):
            input("wrong input, press enter to return... ")

    elif option == "4":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert id: "))
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
            input("account updated, press enter to return... ")
        except (ValueError, IndexError):
            input("wrong input, press enter to return... ")

    elif option == "5":
        clear()
        accounts_read()
        try:
            account_id = int(input("insert account id: "))
            account_delete(account_id)
            input("account deleted, press enter to return... ")
        except (ValueError, IndexError):
            input("wrong input, press enter to return... ")

    else:
        print("not in range")