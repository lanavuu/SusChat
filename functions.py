import json

class account():
    def __init__(self, filename="account_management.json"):
        self.file = filename
        self.__account_list = []

    def create_account(self, username, password):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        file["username"] = username
        file["password"] = password

        with open("account_managemen.json", "w") as f:
            json.dump(file, f)

    def login(self, username, password):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        tries = 3
        logged_in = False
        while tries != 0:
            if file["username"] != username or file["password"] != password:
                tries -= 1
                print(f"Username or password is incorrect, please try again. You have {tries} left")
            else:
                logged_in = True
                break
        return logged_in
        
        
    def crew_list(self):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        friends = list(file.values())
        print(f"List of friends: {friends}")
