import unittest
from user import User

class Testclass(unittest.TestCase):
    '''
    This test class defines test cases for the User class(In the user.py module)
    '''
    # def tearDown(self):
    #     '''
    #     clears up after each test runs
    #     '''
    #     User.list_of_users = []

    def setUp(self):
        '''
        Runs before each individual test case to set up
        '''
        self.new_user = User('Victoria', '09808hj!')
    

    
    def test_init(self):
        '''
        This method ensure proper initialization
        '''
        
        self.assertEqual(self.new_user.username, 'Victoria')
        self.assertEqual(self.new_user.password, '09808hj!')
    
    def test_save_user(self):
        '''
        Tests if new user has been added to our list of users
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.list_of_users), 1)






if __name__ == "__main__":
    unittest.main()