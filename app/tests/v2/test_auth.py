import unittest
import json
import os
from app import create_app


class AuthTestCase(unittest.TestCase):
	# method will run before each test case method
	def setUp(self):
		self.client= create_app('testing').test_client()
		self.user = {'name':'njerr','email':'njer@gmail.com', 'roles':'admin', 'password':'dsaf'}
		# self.new_user = {'email': 'alias@gmail.com', 'name':'alias', 'password': '1881','roles'='admin'}

	def register_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/register', data=user_data)

	def login_user(self,name='',email='',roles='',password=''):
		user_data = self.user
		return self.client.post('/api/v2/auth/login', data=user_data)

	def test_registration(self):
		self.register_user()
		result = self.login_user()
		response = self.client.post('/api/v2/auth/register',
				data=json.dumps(self.user),
				content_type='application/json')

		self.assertEqual(response.status_code, 201)


	def test_user_login(self):
		res = self.client.post('/api/v2/auth/register', data=self.user)
		self.assertEqual(res.status_code, 201)
		login_res = self.client().post('/auth/login', data=self.user_data)

		# get the results in json format
		result = json.loads(login_res.data.decode())
		# Assert that the status code is equal to 200
		self.assertEqual(login_res.status_code, 200)
		self.assert()
		self.assertTrue(result['access_token'])


	# def test_user_login(self):
	# 	user_data = self.user
	# 	res = self.client.post('/api/v2/auth/register', data=user_data)
	# 	self.assertEqual(res.status_code, 201)
	# 	login_res = self.client.post('/api/v2/auth/login', data=self.user_data)
	#
	# 	# get the results in json format
	# 	result = json.loads(login_res.data.decode())
	# 	# Test that the response contains success message
	# 	# Assert that the status code is equal to 200
	# 	self.assertEqual(login_res.status_code, 200)
	# 	self.assertTrue(result['access_token'])
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
