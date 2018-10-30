import unittest
import json
import os
from app import create_app


class AuthTestCase(unittest.TestCase):
	# method will run before each test case method
	def setUp(self):
		self.client= create_app('testing').test_client()
		self.user = {'name':'njerr','email':'njer@gmail.com', 'roles':'admin', 'password':'dsaf'}

	def register_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/register', data=user_data)

	def login_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/login', data=user_data)


	def test_register_user(self):
            self.register_user()
            result = self.login_user()
            access_token = json.loads(result.data.decode())['access_token']

            response = self.client.post('/api/v2/auth/register',data=self.user,
                headers=dict(Authorization="Bearer " + access_token))

            self.assertEqual(response.status_code, 201)


if __name__=="__main__":
	unittest.main()
