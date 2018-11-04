
import unittest
import json
import os
from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"product_id":5, "name":"Purple Hibiscus","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.register_user = {'email': 'joo@gmail.com', 'name': 'joan', 'password': 'jj','roles':'admin'}
			self.login_user={'email': 'joo@gmail.com','password': 'jj'}

		def register_user(self,email="", password="",roles="",name=""):
			user_data = self.register_user
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self, email="", password=""):
			user_data =self.user
			return self.client.post('/api/v2/auth/login', data=user_data)
