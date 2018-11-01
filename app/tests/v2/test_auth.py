import unittest
import json
import os
from app import create_app


class AuthTestCase(unittest.TestCase):
	# method will run before each test case method
	def setUp(self):
		self.client= create_app('testing').test_client()
		self.user = {'name':'joan','email':'joan@gmail.com', 'roles':'admin', 'password':'jojo'}
		self.user_empty = {'name':'joan','email':'joan@gmail.com', 'roles':'admin', 'password':''}

	def register_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/register', data=user_data)

	def login_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/login', data=user_data)



	def test_user_login(self):
		response = self.client.post('/api/v2/auth/login',data=json.dumps(self.user),
		content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_empty_password(self):
		response = self.client.post('/api/v2/auth/login',data=json.dumps(self.user_empty),
		content_type='application/json')
		self.assertEqual(response.status_code, 200)

	# def test_Register_user(self):
    #     response = self.client.post('/api/v2/users/login',
    #      data = json.dumps(self.user),
    #      content_type = 'application/json')
    #     response_data = json.loads(response.data.decode())
	#
    #     token = json.loads(response.data.decode())['access_token']
	#
    #     response = self.client.post('/api/v2/auth/user',
    #     data = json.dumps(self.register_valid_email),
    #     headers=dict(Authorization="Bearer " + token),
    #     content_type = 'application/json')
    #     response_data = json.loads(response.data)
    #     self.assertEqual(response_data["message"],"Enter correct email format")
    #     self.assertEqual(response.status_code, 200)
#
	# def test_registration(self):
	# 	"""Test user registration works correcty."""
	# 	res = self.client.post('/auth/v2/register', data=self.user_data)
	# 	# get the results returned in json format
	# 	result = json.loads(res.data.decode())
	# 	# assert that the request contains a success message and a 201 status code
	# 	self.assertEqual(result['message'], "You registered successfully.")
	# 	self.assertEqual(res.status_code, 201)
	#
	# def test_register_user(self):
    #         self.register_user()
    #         result = self.login_user()
    #         access_token = json.loads(result.data.decode())['token']
	#
    #         response = self.client.post('/api/v2/auth/register',data=self.user,
    #             headers=dict(Authorization="Bearer " + access_token))
	#
    #         self.assertEqual(response.status_code, 201)





	# def test_non_registered_user_login(self):
	# 	"""Test non registered users cannot login."""
	# 	# define a dictionary to represent an unregistered user
	# 	not_a_user = {
	# 		'email': 'not_a_user@example.com',
	# 		'password': 'nope'
	# 	}
	# 	# send a POST request to /auth/login with the data above
	# 	res = self.client.post('/api/v2/auth/login', data=not_a_user)
	# 	# get the result in json
	# 	result = json.loads(res.data.decode())
	#
	# 	# assert that this response must contain an error message
	# 	# and an error status code 401(Unauthorized)
	# 	self.assertEqual(res.status_code, 401)
	# 	self.assertEqual(
	# 		result['message'], "Invalid email or password, Please try again")


if __name__=="__main__":
	unittest.main()
