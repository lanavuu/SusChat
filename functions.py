import json
from datetime import datetime
from pathlib import Path

class account():
    def __init__(self, filename="account_management.json"):
        self.file = Path(__file__).parent / filename
        self.message_log = Path(__file__).parent / "message_log.txt"
        self.__account_database = []
        self.current_user = None

        with open(self.file, "r", encoding="utf-8") as f:
            self.__account_database = json.load(f)


    def create_account(self, username, password):
        """Create an account that doesn't exist.
        
        User will create account then stored into `account_management` file.

        Args:
            username: can be a mixture of int or string
            password: can be a mixture of int or string

        FIX - make sure it doesn't match any other names in the file
        """
        account = {"name": username, "password": password, "friends": [], "favorite color": "n/a", "favorite role": "n/a", "received friend requests": [], "sent friend requests" : [], "blocked": []}
        self.__account_database.append(account)

        with open(self.file, "w") as f:
            json.dump(self.__account_database, f, indent=4)

    def login(self, username, password):
        """Log into an existing account.

        Logs into an account if the provided ``username`` and ``password`` matches any accounts in the file.
        If either ``username`` or ``password`` is incorrect, output a failed attempt message.

        Args:
            username: provided username from user
            password: provided password from user

        Return:
            ``True`` if found a match in the file, ``False`` if could not find a match in the file.
        """
        with open(self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user["name"] == username and user["password"] == password:
                self.current_user = user
                print("Login Successful!")
                return True
        print("Invalid Username or Password.")
        return False
    
    def change_user(self, newName):
        """Change the username of the current account.

        Allows user to change their username. Function will find the name that matches the current user's name in the file then store the
        new name into the value for the key that matched the current user's name.

        Args:
            newName: the name that the user wants to change to.
        
        FIX - make sure it doesn't match any other names in the file
        
        """
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
        """Change the password of the current account

        Allows user to change their password.

        Args:
            newPass: the new password that user provided and wants to change to.
        """
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
        """Log out of the current account

        When ran, set current user to ``None`` to log out of the account.
        """
        self.current_user = None

    def get_crew_list(self):
        """Get a list of friends added.

        Get the list of friends in user's account.
        First check if the list is empty, if not print the data in ``friends`` with index order formatting.

        """

        # dict.get(key, default val), if friends doesn't have a value give an empty list
        friends = self.current_user.get("friends", [])
        if friends == []:
            print("\nCrew list is empty.")
            return
        print("\n======= CREW LIST =======")
        i = 1
        for friend in self.current_user['friends']:
            print(f'{i}. {friend}\n')
            i += 1

    def search_crewmate(self, name_of_crewmate):
        """Search for a user.

        Look up a crewmate to see if they exist. Currently useless.

        Args:
            name_of_crewmate: name of the person user wants to lookup.
        Return:
            None
        """
        with open (self.file, "r") as f:
            file = json.load(f)

        for user in file:
            if user['name'] == name_of_crewmate:
                return user['name']
            
        return None
            
    def add_crew(self, name_of_crewmate):
        """Add a friend.

        Allows user to send a friend request to another account.
        Find and set the accounts to each other, ``current`` holds the current account the user is in. ``other`` holds name_of_crewmate's name value.
        Users must not be blocked by one another. Users can only add each other if they are in each other's ``sent friend requests`` list.

        Args:
            name_of_crewmate: name of the other user that the current user wants to add/send a friend request to.
        
        """
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
            return
        
        elif current['name'] in other['blocked'] or other['name'] in current['blocked']:
            print("Could not perform action, check blocked lists.\n")
            return

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
        """Get a list of people who sent a friend request to current user.

        Allows user to view whom is in their ``received friend requests`` list. The purpose is to allow them to know who wants to add them.
        Letting the user know who wants to add them can make adding friends easier.
        This function will print the data in ``received friend requests`` in index format.
        
        """
        if self.current_user['received friend requests'] == []:
            print("\nCrew list is empty.")
            return
        
        print("\n======= RECEIVED FRIEND REQUESTS =======")
        i = 0
        for crew in self.current_user['received friend requests']:
            print(f'{i}. {crew}\n')
            i+=1

    def get_sent_friend_requests(self):
        """Get a list of the people you sent a friend request to.

        Allows user to view whom is in their ``sent friend requests`` list. 
        The purpose is to allow them to know who they sent a friend request to.
        This function will print the data in ``sent friend requests`` in index format.
   
        """
        if self.current_user['sent friend requests'] == []:
            print("\nCrew list is empty.")
        else:
            print("\n======= SENT FRIEND REQUESTS =======")
            i = 0
            for crew in self.current_user['sent friend requests']:
                print(f'{i}. {crew}\n')
                i+=1
        
    def unadd_crew(self, name_of_crewmate):
        """Unadds a friend.

        User can unadd the other user. ``current`` will be set to the current account logged in.
        ``other`` will store ``name_of_crewmate`` if a key matches to ``name_of_crewmate`` in the files.
        User must already be in eachother's ``friends`` list to unadd eachother.
        If this is true, their names will be removed from eachother's ``friends`` list.
        
        """
        with open(self.file, "r")as f:
            file = json.load(f)

        current = None
        other = None

        for user in file:
            if user['name'] == self.current_user['name']:
                current = user
            if user['name'] == name_of_crewmate:
                other = user
        
        if other is None:
            print("Crewmate not found.\n")
            return
        elif other['name'] not in current['friends'] or current['name'] not in other['friends']:
            print("Unable to perform action: crewmate not located in friends list.\n")
            return
        elif other['name'] in current['friends'] and current['name'] in other['friends']:
            other['friends'].remove(current['name'])
            current['friends'].remove(other['name'])

            self.current_user = current
        
        with open(self.file, "w")as f:
            json.dump(file, f, indent=4)

    def block(self, name_of_crewmate):
        """Block the other user

        ``current`` will be set to the current user logged in. ``other`` will be set to ``name_of_crewmate``
        If they are currently friends, they will be removed from eachother's ``friends`` list then ``name_of_crewmate`` will be added to ``block``.
        If they are not currently friends, ``name_of_crewmate`` will be appended to the user's ``block``.

        Args:
            name_of_crewmate: name of other user that the user would like to block.
        """
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
        elif other['name'] in current['friends'] and current['name'] in other['friends']:
            other['friends'].remove(current['name'])
            current['friends'].remove(other['name'])

            current['blocked'].append(other['name'])
        else:
            current['blocked'].append(other['name'])

        self.current_user = current

        with open (self.file, "w") as f:
            json.dump(file, f, indent=4)

    def unblock(self, crewmate):
        """Unblocks a user

        Unblocks ``crewmate`` by checking if crewmate is blocked.

        Args:
            crewmate: name of the player user would like to unblock
        """
        if self.current_user['blocked'] == []:
            print("You have no one blocked.\n")

        with open(self.file, "r") as f:
            file = json.load(f)
        
        current = None
        other = None

        for user in file:
            if user['name'] == self.current_user['name']:
                current = user
            if user['name'] == crewmate:
                other = user
        
        if other == None:
            print("Crewmate not found.\n")

        elif other['name'] in current['blocked']:
            current['blocked'].remove(other['name'])
            print(f"{other['name']} has been successfully unblocked!\n")
        
        self.current_user = current

        with open(self.file, "w")as f:
            json.dump(file, f, indent=4)

    def get_blocked_list(self):
        """Prints the list of people in the current account's ``blocked``.

        Get the data from ``blocked`` and print it's empty if it is empty.
        If not empty will print each name blocked in index format.

        """
        blocked = self.current_user.get("blocked", [])
        if blocked == []:
            print("==== BLOCKED LIST ====\n No one is blocked.\n")
            return
       
        print("\n==== BLOCKED LIST ====")
        i = 1
        for blocked in self.current_user['blocked']:
            print(f"{i}. {blocked}\n")
            i+=1


    def set_favorite_color(self, color):
        """Set current user's favorite color.

        Locate the current user's `name` in order to change `favorite color` in the file.
        
        Args:
            color: the color the player wants to set as their favorite color.
        """
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
        """Set current user's favorite role.

        Locate the current user's `name` in order to change `favorite role` in the file.
        
        Args:
            role: the role the player wants to set as their favorite role.
        """
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
        """Prints basic information about the current user's account
        
        Will print `name`, `favorite color`, and `favorite role`.
        """
        user = self.current_user
        print(f"Name: {user['name']}\nFavorite Color: {user['favorite color']}\nFavorite Role: {user['favorite role']}\n")

    def print_other_acc_info(self, other_acc):
        """Prints basic information about another user's account
            
        Find the name of ``other_acc`` in the file then save the key into ``other``. Check if empty.
        If not empty, prints ``other_acc`` 'name', 'favorite color' and 'favorite role'.
        """
        with open(self.file, "r") as f:
            file = json.load(f)

        other = None

        for user in file:
            if user['name'] == other_acc:
                other = user
                break
        if other is None:
            print("Crewmate not found")
            return

        print(f"\n==== CREWMATE INFORMATION ====\nUsername: {other['name']}\nFavorite Color: {other['favorite color']}\nFavorite Role: {other['favorite role']}\n")

    def send_message(self, receiver, message):
        """Send a message to another user
        
        Verify if both accounts are logged in or exists and store into ``current`` and ``other``.
        If both accounts are valid, prints a formatted date of when message is executed, followed by the name of the sender, the name of the receiver and the message.
       
        Args:
            reciever: name of the person to send the message to.
            message: the message the user would like to send.
        """
        if self.current_user == None:
            print("Error: you are not logged in.")
            return
        with open (self.file, "r") as f:
            file = json.load(f)
        
        current = None
        other = None

        for user in file:
            if user['name'] == self.current_user['name']:
                current = user
            if user['name'] == receiver:
                other = user
        if other == None:
            print("Crewmate not found.\n")
            return None
        elif other != None and current != None:
            msg = f"{datetime.now().strftime('%Y-%m-%d %I:%M %p')} | from: {current['name']} | to: {other['name']} | message: {message}"

            with open(self.message_log, "a", encoding="utf-8") as f:
                f.write(msg)
            print(f"Message to {other['name']} sent!\n")

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

