from functions import account
account = account()

def block_scene():
    while True:
        try:
            option = int(input("==== BLOCK STATION ====\n1. Block Crew\n2. Unblock Crew\n3. View blocked\n4. Return\nInput: "))
            if option < 1 or option > 4:
                raise ValueError("Error: enter a number from 1-4.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                account.get_crew_list()
                crew = input("\nEnter crew you want to block (you can also block crews not from the list): ")
                account.block(crew)
                
            elif option == 2:
                account.get_blocked_list()
                crew =input("\nEnter the crew you would like to unblock: ")
                account.unblock(crew)
                
            elif option == 3:
                account.get_blocked_list()
            elif option == 4:
                break

# ========== MANAGING FRIENDS/ VIEWING ACCOUNTS
def viewing_other_accounts():
    while True:
        searched = input("=== LOOK UP ===\nEnter name of crewmate to search: ")
       
        while account.search_crewmate(searched) == False:
            option = input("The crewmate you entered doesn't exist. Please enter the following:\n1. Keep Searching\n2. Exit Lookup Station\nInput: ")
            if option == 1:
                viewing_other_accounts()
            elif option == 2:
                break

# ===== Editing account info functions ====
def color_scene():
    colors = {
        1: "Red",
        2: "Blue",
        3: "Green",
        4: "Pink",
        5: "Orange",
        6: "Yellow",
        7: "Black",
        8: "White",
        9: "Purple",
        10: "Brown",
        11: "Cyan",
        12: "Lime",
        13: "Maroon",
        14: "Rose",
        15: "Banana",
        16: "Gray",
        17: "Tan",
        18: "Coral"
    }
    while True:
        print("==== AMONGUS COLORS ====\n")
        for key, value in colors.items():
            print(f"{key}. {value}")
        try:
            choice = int(input("Enter your favorite color: "))
            if choice not in colors:
                raise ValueError("Error: enter a valid number 1-18")
        except Exception as e:
            print(e)
        else:
            chosen_color = colors[choice]
            print(f"Favorite color added: {chosen_color}")
            account.set_favorite_color(chosen_color)
            break
def role_scene():
    roles = {
        1: "Crewmate",
        2: "Scientist",
        3: "Engineer",
        4: "Guardian Angel",
        5: "Noisemaker",
        6: "Tracker",
        7: "Detective",
        8: "Imposter",
        9: "Shapeshifter",
        10: "Phantom",
        11: "Viper",
        12: "Ghost",
    }
    while True:
        print("==== AMONGUS ROLES ====\n")
        for key,value in roles.items():
            print(f"{key}, {value}")
        try:
            choice = int(input("Enter your favorite role: "))
            if choice not in roles:
                raise ValueError("Error: enter a valid number 1-12")
        except Exception as e:
            print(e)
        else:
            chosen_role = roles[choice]
            print(f"Favorite role added: {chosen_role}")
            account.set_favorite_role(chosen_role)
            break

# ========== SETTING FUNCTIONS ==========

def edit_username_scene():
    while True:
        try:
            new_username = input("\nEnter your new username: ")
            check = account.change_user(new_username)
            if check == False:
                raise Exception("Someone already has this username.")
        except Exception as e:
            print(e)
        else:
            if check == True:
                print("Username change successful!\n")
                break
        

def change_password_scene():
    new_pass = input("\nEnter your new password: ")
    account.change_password(new_pass)

def edit_account_info_scene():
    print("====== GENERAL ACCOUNT INFO ======\n")
    account.print_account_information()
    while True:
        try:
            option = int(input("Would you like to edit:\n1. Favorite Color\n2. Favorite Role\n3. Exit\nInput: "))
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number between 1-3.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                color_scene()
            if option == 2:
                role_scene()
            if option == 3:
                break

# ========== LOGIN FUNCTIONS ==========

def ship_message_scene():
    crew = input("=== COMMUNICATIONS ===\nEnter crewmate: ")
    msg = input("\nEnter the message: ")
    account.send_message(crew, msg)
    while True:
        try:
            option = int(input("=== COMMUNICATIONS ===\n1. Send another message\n2. Return to Inbox\nInput: "))
            if option < 1 or option > 2:
                raise ValueError("Error: enter a valid number between 1-2.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                break
            elif option == 2:
                inbox_scene()
                break

def inbox_scene():

    while True:
        try:
            option= int(input("===== INBOX =====\n1. Ship a Message\n2. View Messages\n3. Return\nInput:"))
            if option < 1 or option >3:
                raise ValueError("Error: enter a valid number between 1-3.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                ship_message_scene()
                break
            elif option == 2:
                account.view_messages()
            elif option == 3:
                break

def manage_crew():
   
    while True:
        try:
            option = int(input("====== YOUR CREWMATES ======\n1. View Crew-list\n2. Search or Manage A Crewmate\n3. Return\nInput: "))
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                account.get_crew_list()
                account.get_received_friend_requests()
                account.get_sent_friend_requests()
            elif option == 2:
                search_scene()
            elif option == 3:
                break
def search_scene():
    while True:
        try:
            option = int(input("====== CREWMATE SEARCH-N-MANAGE ======\n1. View Crewmate Account\n2. Add Crewmate\n3. Unadd Crewmate\n4. Manage Block\n5. Return\nInput: "))
            if option < 1 or option > 5:
                raise ValueError("Error: enter a valid number (1-5).")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                crew = input("\nEnter crew you want to view: ")
                account.print_other_acc_info(crew)
             
            elif option == 2:
                crew = input("\nEnter crew you want to add: ")
                account.add_crew(crew)
                
            elif option == 3:
                account.get_crew_list()
                crew = input("\nEnter crew you want to unadd: ")
                account.unadd_crew(crew)
                
            elif option == 4:
                block_scene()
        
            elif option == 5:
                break   

def post_tip_scene():
    while True:
        try:
            category = input("What category is this tip in?\nexamples: Imposter, Viper, Detective, etc.\nInput: ")
            tip = input("\nInput your tip: ")
        except Exception:
            print("There was an error uplaoding your tip.")
        else:
            account.upload_tip(category, tip)
            break
def board_scene():
    while True:
        try:
            option = int(input("==== TIP BOARD ====\n1. Post a Tip\n2. Delete a Tip\n3. View Tips\n4. Return\nInput: "))
            if option < 1 or option > 4:
                raise ValueError("Enter a valid number between 1-4.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                post_tip_scene()
            elif option == 2:
                account.delete_tip()
            elif option == 3:
                account.view_tips()
            elif option == 4:
                break

def settings():
    while True:
        try:
            option = int(input("======= SPACE SETTINGS =======\n1. Edit Username\n2. Change Password\n3. Account Info\n4. Sign Out\n5. Return to Space Hub\n\n6. DELETE ACCOUNT\nInput: "))
            if option < 1 or option > 6:
                raise ValueError("Error: enter a valid number between 1-6.\n")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                edit_username_scene()
            elif option == 2:
                change_password_scene()
            elif option == 3:
                edit_account_info_scene()
            elif option == 4:
                # dont add another main_menu redirection since its already called
                account.logout()
                break
            elif option == 5:
                break
            elif option == 6:
                try:
                    choice = int(input("Are you sure you want to delete your account?\n1. Yes\n2. No\nInput: "))
                    if choice < 1 or choice > 2:
                        raise ValueError("Error: enter a valid number 1-2.")
                except Exception as e:
                    print(e)
                else:
                    if choice == 1:
                        check_deleted = account.delete_account()
                        if check_deleted == True:
                            break
                        elif check_deleted == False:
                            print("Account deletion failed")
                    elif choice == 2:
                        break

def faq():
    pass

# ========== MAIN MENU FUNCTIONS ==========
def space_hub():
    while True:
        try:
            option = int(input(f"======= SPACE HUB =======\nWelcome {account.current_user['name']}!\n1. Ship message\n2. Inbox\n3. Manage Crews\n4. Tip board\n5. FAQ\n6. Settings\nInput: "))
            if option < 1 or option > 7:
                raise ValueError("Error: enter a valid number between 1-7.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                ship_message_scene()
            elif option == 2:
                inbox_scene()
            elif option == 3:
                manage_crew()
                
            elif option == 4:
                board_scene()
            elif option == 5:
                faq()
            elif option == 6:
                settings()

def login_scene():
    user = input("\nUsername: ")
    passw = input("Password: ")
    logged_in = account.login(user, passw)
    if logged_in == True:
       space_hub()
    else:  
        try:
            option = int(input(("======= Login Unsuccessful =======\n1. Try again\n2. Return to previous page\nInput: ")))
            if option < 1 or option >2:
                raise ValueError("Error: enter 1 or 2\n")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                login_scene()
            elif option == 2:
                main_menu()
            
            
def create_account_scene():
    userEntersName = input("\nPlease enter a username: ")
    userEntersPassword = input("\nPlease enter a password: ")
    newAcc = account.create_account(userEntersName, userEntersPassword)
    if newAcc:
        print("Account creation success!\n Redirecting you to login page..\n")
    else:
        print("ERROR: Account creation failed.. Redirecting you to login page..\n")
    login_scene()

# MAIN MENU ==========
def main_menu():

    while True:
        try:
            option = int(input("======= SPACE HUB =======\n1. Crewmate Login\n2. Create Crewmate Account\n3. Quit\nInput: "))
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number between 1-3.\n")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                login_scene()
            elif option == 2:
                create_account_scene()
            elif option == 3:
                break

if __name__ == "__main__":
    main_menu()
        