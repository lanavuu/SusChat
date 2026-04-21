import json

def createAccount(username, password):
    with open("account_management", "r") as f:
        file = json.load(f)

    file["username"] = username
    file["password"] = password

    with open("account_management", "w") as f:
        json.dump(file, f)

