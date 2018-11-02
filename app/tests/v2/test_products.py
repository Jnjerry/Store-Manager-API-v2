import unittest
import json
import os
from ... import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"product_id":5, "name":"Purple Hibiscus","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.missing_data = {"product_id":"", "name":"","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.register_user = {'email': 'joo@gmail.com', 'name': 'joan', 'password': 'jj','roles':'admin'}
			self.login_user={'email': 'joo@gmail.com','password': 'jj'}

		def register_user(self,email="", password="",roles="",name=""):
			user_data = self.register_user
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self, email="", password=""):
			user_data =self.user
			return self.client.post('/api/v2/auth/login', data=user_data)


		def test_create_product(self):
			response = self.client.post(
			'/api/v2/auth/login',
			data = json.dumps(self.login_user),
			content_type = 'application/json'
			)
			token = json.loads(response.data.decode())['access_token']

			# #test product has been added
			response = self.client.post(
			'/api/v2/products',
			data = json.dumps(self.product_data),
			headers=dict(Authorization="Bearer " + token),
			content_type = 'application/json')
			response_data = json.loads(response.data)
			self.assertEqual(response.status_code, 201)

		def test_modify_product(self):
			response = self.client.post(
			'/api/v2/auth/login',
			data = json.dumps(self.login_user),

			content_type = 'application/json'
			)
			token = json.loads(response.data.decode())['access_token']
			# check if updated item exists
			response = self.client.put(
			'/api/v2/products/8888',
			headers=dict(Authorization="Bearer " + token),
			data = json.dumps(self.product_data),
			content_type = 'application/json')

			response_data = json.loads(response.data)
			self.assertEqual(response.status_code, 201)


		def test_product_list(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login_user),
			content_type = 'application/json')

			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)

		def test_product_id(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login_user),
			content_type = 'application/json')

			response=self.client.get('api/v2/products/34',content_type="application/json")
			self.assertEqual(response.status_code,200)
		def test_product_empty(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps({}),
			content_type = 'application/json')

			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)
		# def test_product_missing(self):
		# 	response = self.client.post('/api/v2/auth/login',data = json.dumps(self.missing_data),
		# 	content_type = 'application/json')
		#
		# 	response=self.client.get('api/v2/products',content_type="application/json")
		# 	self.assertEqual(response.status_code,200)

		def test_invalid_product_id(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login_user),
			content_type = 'application/json')

			response=self.client.get("api/v1/sale/9000",content_type="application/json")
			self.assertEqual(response.status_code,404)
