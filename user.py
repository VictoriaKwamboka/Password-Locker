import pyperclip
import string
import random


class User:
    '''
    This class generates new instances of a user
    '''
    list_of_users = []

    def __init__(self, username, password):
        '''
        a user will have a username and a password
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        saves the user
        '''
        User.list_of_users.append(self)
    @classmethod
    def display_users(cls):
        '''
        Displays the list of users in the class
        '''
        return cls.list_of_users
    def delete_user(self):
        '''
        Deletes a user from the class list
        '''
        User.list_of_users.remove(self)
class LogIn():
    '''
    provides a blueprint for creating new instances of a login
    '''
    logins = []

    @classmethod
    def valid_user(cls, username, password):
        '''
        validates if the user is in the list of users and returns their username
        '''
        val_user = ''
        for user in User.list_of_users:
            if(user.username == username and user.password == password):
                val_user = user.username
        return val_user
    def __init__(self, platform, username, password):

        '''
        initializes the details to be stored
        '''
        self.platform = platform
        self.username = username
        self.password = password
    def save_login(self):
        '''
        method to save log in details of a user
        '''
        LogIn.logins.append(self)
    def delete_login(self):
        '''
        method to delete a log in from the list of log ins
        '''
        LogIn.logins.remove(self)

    @classmethod
    def find_login(cls, platform):
        '''
        this method takes in the platform name and returns the log in details associated with that platform
        '''
        for login in cls.logins:
            if login.platform == platform:
                return login

    @classmethod
    def copy_password(cls, platform):
        '''
        this paperclip function copies the password for a specific login usinf pyperclip
        '''
        found_login = LogIn.find_login(platform)
        pyperclip.copy(found_login.password)

    @classmethod
    def truthy_login(cls, platform):
        ''''
        truthy method that returns true if the log in exists otherwise returns false
        '''
        for login in cls.logins:
            if login.platform == platform:
                return True
        return False
    @classmethod
    def display_logins(cls):
        '''
        This method returns the list of log in details when called
        '''
        return cls.logins

    def generate_password(stringLength=8):
        '''
        Using random and string modules to generate a random password that's 8 characters long
        The password contains strings, special characters and numbers
        '''
        password = "~!@#$%^&*" + string.ascii_lowercase +string.ascii_uppercase
        return ''.join(random.choice(password) for i in range(stringLength))


    
  
    