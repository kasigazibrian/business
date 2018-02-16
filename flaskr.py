import os
from app import *
import  unittest
app.config['TESTING']= True
class BusinessTestCase(unittest.TestCase):
    #Test if login page loads correctly
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    #Test if login loads with the required information
    def test_login_loads_with_required_information(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please sign in' in response.data)
        self.assertTrue(b'Username' in response.data)
        self.assertTrue(b'Password' in response.data)

    def test_login_pass(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(Username='kbrian',Password=123456), follow_redirects=True)
        self.assertTrue(b'You have successfully logged in!' in response.data)

    def test_login_fail(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(Username='kbrian',Password='dfgdg'), follow_redirects=True)
        self.assertTrue(b'INVALID USERNAME OR PASSWORD' in response.data)

    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'You have successfully logged out' in response.data)


if __name__=='__main__':
    unittest.main()
