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
        with open(self.file, "r") as f:
           file = json.load(f)

        for user in file:
           if user['name'] == self.current_user['name']:
               user['name'] = newName
               # point to the new username
               self.current_user = user
               break
           
        with open(self.file, "w") as f:
            json.dump(file, f, indent=4)
               
    def change_password(self, newPass):
        with open(self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == self.current_user['name'] and user['password'] == self.current_user['password']:
                user['password'] = newPass
                self.current_user = user
                break

        with open(self.file, "w") as f:
            json.dump(file, f, indent=4)

    def logout(self):
        self.current_user = None

    def get_crew_list(self):
        print(self.current_user["friends"])

    def set_favorite_color(self, color):
        with open(self.file, "r") as f:
            file = json.load(f)

        verification = self.verify_account
        if verification == True:
            for user in file:
                user['favorite color'] = color
                self.current_user = user
                break
        

    def verify_account(self):
        # helper function to identify account
        with open(self.file, "r") as f:
            file = json.load(f)
        if self.current_user == None:
            return False
        
        for user in file:
            if user['name'] == self.current_user['name']:
                return user
        return False

    