from platform import platform

from argon2 import PasswordHasher


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
        
    