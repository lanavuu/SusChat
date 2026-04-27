import json

class account():
    def __init__(self, filename="account_management.json"):
        self.file = filename
        self.__account_database = []
        self.current_user = None


        with open (filename, "r") as f:
            self.__account_database = json.load(f)

    def create_account(self, username, password):
        account = {"name": username, "password": password, "friends": [], "favorite color": "n/a", "favorite role": "n/a"}
        self.__account_database.append(account)

        with open(self.file, "w") as f:
            json.dump(self.__account_database, f, indent=4)

    def login(self, username, password):
        with open("account_management.json", "r") as f:
            file = json.load(f)

        for user in file:
            if user["name"] == username and user["password"] == password:
                self.current_user = user
                print("Login Successful!")
                return True
        print("Invalid Username or Password.")
        return False
    
    def change_user(self, newName):
       if self.current_user != None:
           self.current_user['name'] = newName
           self.__account_database.append(self.current_user['name'])
           with open(self.file, "w") as f:
            json.dump(self.__account_database, f, indent=4)

           

    def change_password(self, newPass):
        self.current_user["password"] = newPass
    def logout(self):
        self.current_user = None

    def get_crew_list(self):
        print(self.current_user["friends"])

    def set_favorite_color(self, color):
        self.current_user["favorite color"] = color

    