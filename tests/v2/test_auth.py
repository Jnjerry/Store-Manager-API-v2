
import unittest
import json
import os
from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"product_id":5, "name":"Purple Hibiscus","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.register_user = {'email': 'jojo-1@gmail.com', 'name': 'joan', 'password': 'jj','roles':'admin'}
			self.register_new_user = {'email': 'njeri-10@gmail.com', 'name': 'ngugijo', 'password': 'm@ngun@1','roles':'admin'}
			self.login_user={'email': 'njeri-10@gmail.com','password': 'm@ngun@1'}
			self.new_user={'email': 'njerijoan@gmail.com','password': 'm@ngun@1'}

		def register_user(self,email="", password="",roles="",name=""):
			user_data = self.register_user
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self, email="", password=""):
			user_data =self.user
			return self.client.post('/api/v2/auth/login', data=user_data)

		def test_signup_new_user(self):
			response = self.client.post('/api/v2/auth/register',
			data=json.dumps(self.register_user), content_type = 'application/json')

			result = json.loads(response.data.decode())

			self.assertEqual(response.status_code, 201)
			self.assertEqual(result['message'], 'user created successfully')

		def test_login_user(self):
			response = self.client.post('/api/v2/auth/register',
			data=json.dumps(self.register_new_user), content_type = 'application/json')
			result = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			response = self.client.post('/api/v2/auth/login',
			data=json.dumps(self.login_user), content_type = 'application/json')
			result = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)

		def test_login_unexisting_user(self):
			response = self.client.post('/api/v2/auth/login',
				data=json.dumps(self.new_user),content_type = 'application/json')

			result = json.loads(response.data.decode())
			self.assertEqual(result['message'],
				"email does not exist")
			self.assertEqual(response.status_code, 400)
