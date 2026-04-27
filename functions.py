import json

class account():
    def __init__(self, filename="account_management.json"):
        self.file = filename
        self.__account_database = []
        self.current_user = None


        with open (filename, "r") as f:
            self.__account_database = json.load(f)

    def create_account(self, username, password):
        account = {"name": username, "password": password, "friends": [], "favorite color": "n/a", "favorite role": "n/a", "received friend requests": [], "sent friend requests" : [], "blocked": []}
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
        if self.current_user['friends'] == []:
            print("\nCrew list is empty.")
        else:
            with open (self.file, "r") as f:
                file = json.load(f)
            
            for friends in file:
                print(f"{friends}. {friends['friends']}\n")

    def search_crewmate(self, name_of_crewmate):
        with open (self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == name_of_crewmate:
                return name_of_crewmate
            else:
                return False
            
    def add_crew(self, name_of_crewmate):
        crew = self.search_crewmate(name_of_crewmate)
        if crew == False:
            print("Crewmate doesn't exist.\n")
        else:
            with open(self.file, "r") as f:
                file = json.load(f)
            
            for user in file:
                if user['name'] == self.current_user['name']:
                    user['sent friend request'] = crew
                    self.current_user = user
                    print(f"Sent a friend request to: {crew}\n ")
                    break
            with open (self.file, "w") as f:
                json.dump(file, f, indent=4)

    def unadd_crew(self, name_of_crewmate):
        crew = self.search_crewmate(name_of_crewmate)
        if crew == False:
            print("Crewmate doesn't exist.\n")
        else:
            with open (self.file, "r") as f:
                file = json.load(f)

            for user in file:
                if user['name'] == self.current_user['name'] and crew in user['friends']:

                    del crew
                    self.current_user = user
                    print(f"Removed {crew} from crewmates list.\n ")
                    break
                else:
                    print("Error, crewmate could not be located.")

            with open (self.file, "w") as f:
                json.dump(file, f, indent=4)

    def block(self, name_of_crewmate):
        crew = self.search_crewmate(name_of_crewmate)
        if crew == False:
            print("Crewmate doesn't exist.\n")
        else:
            with open(self.file, "r") as f:
                file = json.load(f)
            
            for user in file:
                if user['name'] == self.current_user['name'] and crew in user['friends']:
                    del crew
                    user['blocked'] = crew
                    self.current_user = user
                    print(f"Removed {crew} from crewmates list.\n ")
                    break
                elif user['name'] == self.current_user['name'] and crew not in user['friends']:
                    user['blocked'] = crew
                    self.current_user = user
                    break
                else:
                    print("Error, crewmate could not be located.")

            with open (self.file, "w") as f:
                json.dump(file, f, indent=4)

    def unblock(self, crewmate):
        with open (self.file, "r") as f:
            file = json.load(f)
        for user in file:
            if user['name'] == self.current_user['name'] and user.get("blocked") != None:
                for block in file:
                    if block['blocked'] == crewmate:
                        del block
    
    def blocked_list(self):
        with open (self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == self.current_user['name'] and user.get("blocked") != None:
                print(f"{user}. {user['blocked']}\n")
            else:
                print("0 crewmates blocked.\n")

    def set_favorite_color(self, color):
        with open(self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == self.current_user['name']:
                user['favorite color'] = color
                self.current_user = user
                break
        
        with open(self.file, "w") as f:
            json.dump(file, f, indent=4)
            
    
    def set_favorite_role(self, role):
        with open(self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == self.current_user['name']:
                user['favorite role'] = role
                self.current_user = user
                break

        with open(self.file, "w") as f:
            json.dump(file, f, indent=4)

    def print_account_information(self):
        user = self.current_user
        print(f"Name: {user['name']}\nFavorite Color: {user['favorite color']}\nFavorite Role: {user['favorite role']}\n")

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

    