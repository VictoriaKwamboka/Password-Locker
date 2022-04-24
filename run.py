'''
Due to some Mac issues, this shebang line could not work. 
i keep getting .....exec format error. 
Not even stack overflow could help.

# !/usr/bin/python3

'''
from platform import platform
from user import LogIn, User

def add_new_user(username, password):
    '''
    creates a new user with username and password attributes
    '''
    new_user = User(username,password)
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
    login_user = LogIn.valid_user(username,password)
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
    rand_password=LogIn.generate_password()
    return rand_password
def copy_password(platform):
    """
    copies the password using pyperclip module
    """
    return LogIn.copy_password(platform)




