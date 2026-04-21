import functions

# ========== SETTING FUNCTIONS ==========

def edit_username_scene():
    pass
def change_password_scene():
    pass
def edit_account_info_scene():
    pass

# ========== LOGIN FUNCTIONS ==========

def ship_message_scene():
    pass
def inbox_scene():
    pass
def list_scene():
    pass
def search_scene():
    pass
def board_scene():
    pass
def clip_scene():
    pass
def settings():
    while True:
        option = int(input("======= SPACE SETTINGS =======\n1. Edit Username\n2. Change Password\n3. Account Info\n4. Sign Out\n"))
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
                edit_acc_info_scene()
            elif option == 4:
                # dont add another main_menu redirection since its already called
                break
def faq():
    pass

# ========== MAIN MENU FUNCTIONS ==========

def login_scene():
    username = input("\nUsername: ")
    password = input("\nPassword: ")
    logged_in = functions.login(username, password)
    if logged_in == True:
        while True:
            option = int(input("======= SPACE HUB =======\n1. Ship message\n2. Inbox\n3. Crew List\n4. Crew Search\n5. Tip board\n6. Clip share\n7. Settings\n8. FAQ"))
            try:
                if option < 1 or option > 8:
                    raise ValueError("Error: enter a valid number between 1-7.")
            except Exception as e:
                print(e)
            else:
                if option == 1:
                    ship_message_scene()
                elif option == 2:
                    inbox_scene()
                elif option == 3:
                    list_scene()
                elif option == 4:
                    search_scene()
                elif option == 5:
                    board_scene()
                elif option == 6:
                    clip_scene()
                elif option == 7:
                    settings()
                    break
                elif option == 8:
                    faq()
    else:
        option = int(input(("======= Login Unsuccessful =======\n1. Try again\n2. Return to previous page\n")))
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
            
            
def createAccountScene():
    userEntersName = input("\nPlease enter a username: ")
    userEntersPassword = input("\nPlease enter a password: ")
    newAcc = functions.createAccount(userEntersName, userEntersPassword)
    print("Account creation success!\n Redirecting you to login page..\n")
    login_scene()

# MAIN MENU ==========
def main_menu():
    while True:
        option = int(input("\n======= SPACE HUB =======\n1. Crewmate Login\n2. Create Crewmate Account\n3. Quit\n"))
        try:
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number between 1-3.\n")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                login_scene()
            elif option == 2:
                createAccountScene()
            elif option == 3:
                break

main_menu()
        
