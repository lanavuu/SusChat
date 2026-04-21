import json

def createAccount(username, password):
    with open("account_management", "r") as f:
        file = json.load(f)

    file["username"] = username
    file["password"] = password

    with open("account_management", "w") as f:
        json.dump(file, f)

def login(username, password):
    with open("account_management", "r") as f:
        file = json.load(f)
        
    tries = 3
    while tries != 0:
        if file["name"] != username or file["password"] != password:
            tries -= 1
            print(f"Username or password is incorrect, please try again. You have {tries} left")
