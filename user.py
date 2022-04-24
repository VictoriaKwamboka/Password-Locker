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