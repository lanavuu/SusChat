import functions
def loginScene():
    pass

def createAccountScene():
    userEntersName = input("\nPlease enter a username: ")
    userEntersPassword = input("\nPlease enter a password: ")
    newAcc = functions.createAccount(userEntersName, userEntersPassword)
    print("Account creation success!\n Redirecting you to login page..\n")
    loginScene()


def mainMenu():
    while True:
        option = int(input("\n======= SPACE HUB =======\n1. Crewmate Login\n2. Create Crewmate Account\n3. Quit\n"))
        try:
            if option < 1 or option > 3:
                raise ValueError("Error: enter a valid number between 1-3.\n")
        except Exception as e:
            print(e)
        else:
            if option == 1:
                loginScene()
            elif option == 2:
                createAccountScene()
            elif option == 3:
                break

        
