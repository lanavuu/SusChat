from functions import account
account = account()
# ========== MANAGING FRIENDS/ VIEWING ACCOUNTS
def viewing_other_accounts():
    pass
# ========== SETTING FUNCTIONS ==========

def edit_username_scene():
    new_username = input("\nEnter your new username: ")
    account.change_user(new_username)

def change_password_scene():
    new_pass = input("\nEnter your new password: ")
    account.change_password(new_pass)

def edit_account_info_scene():
    print("====== GENERAL ACCOUNT INFO ======\n")
    account.print_account_information()
    while True:
        option = int(input("Would you like to edit:\n1. Favorite Color\n2. Favorite Role\n3. Exit\nInput: "))
        try:
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number between 1-3.")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                color = input("Favorite Color: ")
                account.set_favorite_color(color)
                break
            if option == 2:
                role = input("Favorite Role: ")
                account.set_favorite_role(role)
                break
            if option == 3:
                break

# ========== LOGIN FUNCTIONS ==========

def ship_message_scene():
    pass
def inbox_scene():
    pass
def manage_crew():
   
    while True:
        print("\n====== YOUR CREWMATES ======\n")
        option = int(input("1. View Crew-list\n2. Search or Manage A Crewmate\nInput: "))
        try:
            if option < 1 or option > 2:
                raise ValueError("Error: enter a valid number")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                account.get_crew_list()
                break
            if option == 2:
                search_scene()
                break
def search_scene():
    while True:
        option = int(input("====== CREWMATE SEARCH ======\n1. View Crewmate Account\n2. Add Crewmate\n3. Unadd Crewmate\n4. Block Crewmate\n5. Unblock\n6. View blocked\n Input: "))
        try:
            if option < 1 or option > 6:
                raise ValueError("Error: enter a valid number (1-6).")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                viewing_other_accounts()
                break
            elif option == 2:
                crew = input("\nEnter crew you want to add: ")
                account.add_crew(crew)
                break
            elif option == 3:
                account.get_crew_list()
                crew = input("\nEnter crew you want to unadd: ")
                account.unadd_crew(crew)
                break
            elif option == 4:
                account.get_crew_list()
                crew = input("\nEnter crew you want to block (you can also block crews not from the list): ")
                account.block(crew)
                break
            elif option == 5:
                pass
            elif option == 6:
                pass
def board_scene():
    pass
def clip_scene():
    pass
def settings():
    while True:
        option = int(input("======= SPACE SETTINGS =======\n1. Edit Username\n2. Change Password\n3. Account Info\n4. Sign Out\nInput: "))
        try:
            if option < 1 or option > 4:
                raise ValueError("Error: enter a valid number between 1-4.\n")
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
def faq():
    pass

# ========== MAIN MENU FUNCTIONS ==========

def login_scene():
    user = input("\nUsername: ")
    passw = input("\nPassword: ")
    logged_in = account.login(user, passw)
    if logged_in == True:
        while True:
            option = int(input(f"======= SPACE HUB =======\nWelcome {account.current_user['name']}!\n1. Ship message\n2. Inbox\n3. Manage Crews\n4. Tip board\n5. Clip share\n6. Settings\n7. FAQ\nInput: "))
            try:
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
                    break
                elif option == 4:
                    board_scene()
                    break
                elif option == 5:
                    clip_scene()
                elif option == 6:
                    settings()
                    break
                elif option == 7:
                    faq()
    else:
        option = int(input(("======= Login Unsuccessful =======\n1. Try again\n2. Return to previous page\nInput: ")))
        try:
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
    print("Account creation success!\n Redirecting you to login page..\n")
    login_scene()

# MAIN MENU ==========
def main_menu():

    while True:
        option = int(input("\n======= SPACE HUB =======\n1. Crewmate Login\n2. Create Crewmate Account\n3. Quit\nInput: "))
        try:
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
        