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
            print("\n======= CREW LIST =======")
            i = 0
            for friend in self.current_user['friends']:
                print(f'{i}. {friend}\n')
                i += 1

    def search_crewmate(self, name_of_crewmate):
        with open (self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == name_of_crewmate:
                return user['name']
            
        return None
            
    def add_crew(self, name_of_crewmate):
        with open(self.file, "r")as f:
            file = json.load(f)

        current = None
        other = None

        for user in file:
            if user['name'] == self.current_user['name']:
                current = user
            elif user['name'] == name_of_crewmate:
                other = user

        if other is None:
            print("Crewmate not found\n")
        
        elif current['name'] in other['blocked'] or other['name'] in current['blocked']:
            print("Could not perform action, check blocked lists.\n")

        elif current['name'] in other['sent friend requests']:
            other['friends'].append(current['name'])
            current['friends'].append(other['name'])

            other['sent friend requests'].remove(current['name'])
            current['received friend requests'].remove(other['name'])


        elif current['name'] not in other['sent friend requests']:
            current['sent friend requests'].append(other['name'])
            other['received friend requests'].append(current['name'])

            
        self.current_user = current

        with open (self.file, "w") as f:
            json.dump(file, f, indent=4)


    def get_received_friend_requests(self):
        if self.current_user['received friend requests'] == []:
            print("\nCrew list is empty.")
        else:
            print("\n======= RECEIVED FRIEND REQUESTS =======")
            i = 0
            for crew in self.current_user['received friend requests']:
                print(f'{i}. {crew}\n')
                i+=1

    def get_sent_friend_requests(self):
        if self.current_user['sent friend requests'] == []:
            print("\nCrew list is empty.")
        else:
            print("\n======= SENT FRIEND REQUESTS =======")
            i = 0
            for crew in self.current_user['sent friend requests']:
                print(f'{i}. {crew}\n')
                i+=1
        
    def unadd_crew(self, name_of_crewmate):
        with open(self.file, "r")as f:
            file = json.load(f)

        current = None
        other = None

        for user in file:
            if user['name'] == self.current_user['name']:
                current = user
            if user['name'] == name_of_crewmate:
                other = user
        
        if other == None:
            print("Crewmate not found.\n")
        elif other['name'] not in current['friends'] or current['name'] not in other['friends']:
            print("Unable to perform action: crewmate not located in friends list.\n")
        elif other['name'] in current['friends'] and current['name'] in other['friends']:
            other['friends'].remove(current['name'])
            current['friends'].remove(other['friends'])

            self.current_user = user
        
        with open(self.file, "w")as f:
            json.dump(file, f, indent=4)

    def block(self, name_of_crewmate):
        crew = self.search_crewmate(name_of_crewmate)
        print(crew)
        if crew == False:
            print("Crewmate doesn't exist.\n")
        else:
            with open(self.file, "r") as f:
                file = json.load(f)
            
            for user in file:
                if user['name'] == self.current_user['name'] and crew in user['friends']:
                    del crew
                    user['blocked'] = []
                    user['blocked'].append(crew['name'])
                    self.current_user = user
                    print(f"Removed {crew} from crewmates list.\n ")
                    break
                elif user['name'] == self.current_user['name'] and crew not in user['friends']:
                    user['blocked'] = []
                    user['blocked'].append(crew)
                    self.current_user = user
                    break
                else:
                    print("Error, crewmate could not be located.")

            with open (self.file, "w") as f:
                json.dump(file, f, indent=4)

    def unblock(self, crewmate):
        if self.current_user['blocked'] == []:
            print("You have no one blocked.\n")

        with open(self.file, "r") as f:
            file = json.dump(f)

        for user in file:
            if user['name'] == self.current_user['name'] and crewmate in user['blocked']:
                user['blocked'].remove(crewmate)
                self.current_user = user

        with open(self.file, "w")as f:
            json.dump(file, f, indent=4)

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

    def print_other_acc_info(self, other):
        with open(self.file, "r") as f:
            file = json.load(f)

        other = None

        for user in file:
            if user['name'] == other['name']:
                other = user

        print(f"\n==== CREWMATE INFORMATION ====\nUsername: {other['username']}\nFavorite Color: {other['favorite color']}\nFavorite Role: {other['favorite role']}\n")



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

