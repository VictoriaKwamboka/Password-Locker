'''
Due to some Mac issues, this shebang line could not work. 
i keep getting .....exec format error. 
Not even stack overflow could help.

# !/usr/bin/python3

'''
# from platform import platform
from platform import platform
from user import LogIn, User


def add_new_user(username, password):
    '''
    creates a new user with username and password attributes
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    saves the user
    '''
    user.save_user()


def display_user():
    '''
    display existing users
    '''
    return User.display_users()


def valid_user(username, password):
    '''
    allows an existing user to log in
    '''
    login_user = LogIn.valid_user(username, password)
    return login_user


def add_new_login(platform, username, password):
    '''
    adds log in details for a new user
    '''
    new_login = LogIn(platform, username, password)
    return new_login


def save_new_login(login):
    '''
    saves a new log in to the list of log ins
    '''
    login.save_login()


def display_login_details():
    """
    returns all saved login details
    """
    return LogIn.display_logins()


def delete_login(login):
    """
    deletes an entry from the login list

    """
    login.delete_login()


def find_login(platform):
    """
    find login details using platform name
    """
    return LogIn.find_login(platform)


def check_truthy_login(platform):
    """
   returns true if an account exists with that platform name and false otherwise

    """
    return LogIn.truthy_login(platform)


def gen_password():
    '''
    generates a random password for the user.
    '''
    rand_password = LogIn.generate_password()
    return rand_password


def copy_password(platform):
    """
    copies the password using pyperclip module
    """
    return LogIn.copy_password(platform)


def Password_Locker():
    '''
    Define a function to run the Pasword locker

    '''

    print("Hello Welcome to your Password Locker...\n Please enter one of the following to proceed.\n NEW ---  To Create A New Account  \n OLD ---  Already Have An Existing Account  \n")
    short_code = input("").lower().strip()

    if short_code == 'new':
        print('Sign up for a new account:')
        print('_' * 65)

        username = input("What's your preferred username?" )
        while True:
            print(" TYPE - To type your preferred pasword:\n GEN - To generate a random password")
            password_Choice = input().lower().strip()
            if password_Choice == 'type':
                password = input("Enter preferred password\n")
                break
            elif password_Choice == 'gen':
                password = gen_password()
                break
            else:
                print("Invalid short code. Please try again!")
        save_user(add_new_user(username,password))
        print("_" * 65)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("_" * 65)
    elif short_code == "old":
        print("_" * 65)
        print("Enter your username and password to log in:")
        print('_' * 65)
        username = input("What's your preferred username? ")
        password = input("Enter password: ")
        login = valid_user(username,password)
        if valid_user == login:
            print(f"Hello {username}. Welcome To The Password_Locker!")  
            print('\n')
    while True:
        print("Use these short codes:\n CREATE - Create a new login details \n DISPLAY - Display log in details \n FIND - Find a log in detail for a platform \n GEN - Generate A random password \n DELETE- Delete log in details \n EXIT - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "create":
            print("Create New Log Ins")
            print("_"*65)
            print("Platform Name? ")
            platform = input().lower()
            print("Your platform username: ")
            username = input()
            while True:
                print(" TYPE - To type your own password if you already have an account:\n GEN - To generate random password")
                password_Choice = input().lower().strip()
                if password_Choice == 'type':
                    password = input("Enter your preferred password\n")
                    break
                elif password_Choice == 'gen':
                    password = gen_password()
                    break
                else:
                    print("Invalid short code, please use 'type' or 'gen'")
            save_new_login(add_new_login(platform,username,password))
            print('\n')
            print(f"Login Details for: {platform} are:  -Username: {username} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "display":
            if display_login_details():
                print("Here's your list of saved platform log in details: ")
                 
                print('*' * 40)
                print('_'* 30)
                for platform in display_login_details():
                    print(f" Account:{platform.platform} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any login details saved yet..........")
        elif short_code == "find":
            print("Enter the platform name you want to search: ")
            search_name = input().lower()
            if find_login(search_name):
                search_login= find_login(search_name)
                print(f"Account Name : {search_login.platform}")
                print('-' * 65)
                print(f"User Name: {search_login.username} Password :{search_login.password}")
                print('-' * 65)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "delete":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_login(search_name):
                search_login = find_login(search_name)
                print("_"*65)
                search_login.delete_login()
                print('\n')
                print(f"Your stored credentials for : {search_login.platform} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
        elif short_code == 'gen':

            password = gen_password()
            print(f" {password} has been generated succesfull. You can proceed to use it to your platform!")
        elif short_code == 'exit':
            print("Thanks for using Password_Locker....Please pop by next time to use it again!")
            break
        else:
            print("Wrong entry... Check your short code and let it match those in the menu! ")
    else:
        print("Please enter a valid input to continue")
        
            
    

if __name__ == '__main__':
    Password_Locker()
