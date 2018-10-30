import unittest
import json
import os
from app import create_app


class AuthTestCase(unittest.TestCase):
	# method will run before each test case method
	def setUp(self):
		self.client= create_app('testing').test_client()
		self.user = {'name':'joan','email':'ngugi.joan2@gmail.com', 'roles':'admin', 'password':'@254'}

	def register_user(self,email="", password="",name="",roles=""):
		"helper method for test for user registration"
		user_data = self.user
		return self.client.post('/api/v2/auth/register', data=user_data)


	def login_user(self, name="",email="", password="",roles=""):
		"helper method for test for user login"
		user_data =self.user
		return self.client.post('/api/v2/auth/login', data=user_data)


	def test_register_user(self):
            self.register_user()
            result = self.login_user()
            access_token = json.loads(result.data.decode())['token']

            response = self.client.post('/api/v2/auth/register',data=self.user,
                headers=dict(Authorization="Bearer " + access_token))

            self.assertEqual(response.status_code, 201)


if __name__=="__main__":
	unittest.main()
