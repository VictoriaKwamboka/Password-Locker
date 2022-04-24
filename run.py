'''
Due to some Mac issues, this shebang line could not work. 
i keep getting .....exec format error. 
Not even stack overflow could help.

# !/usr/bin/python3

'''
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
