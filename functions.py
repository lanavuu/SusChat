import json

class account():
    def __init__(self, filename="account_management.json"):
        self.file = filename
        self.__account_database = []

    def create_account(self, username, password):
        account = {"name": username, "password": password, "friends": [], "favorite color": "n/a", "favorite role": "n/a"}
        self.__account_database.append(account)

        with open(self.file, "w") as f:
            json.dump(self.__account_database, f)

    def login(self, username, password):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        logged_in = False
        print(file)
        if file["username"] != username or file["password"] != password:
               print("Error: Username or password incorrect\n")
               logged_in = False
        else:
            logged_in = True
        return logged_in
        
        
    def crew_list(self):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        friends = list(file.values())
        print(f"List of friends: {friends}")
