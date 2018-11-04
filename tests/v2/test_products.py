import unittest
import json
import os
from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"product_id":90, "name":"American-00","category":"African", "description": "Written by joan","price":20,"quantity":1500}
			self.missing_data = {"product_id":"", "name":"","category":"Africanah", "description": "Written by Chimamanda","price":20,"quantity":1500}
			self.register_user_admin= {'email': 'john@gmail.com', 'name': 'joan', 'password': 'jojo','roles':'admin'}
			self.register_user_attendant= {'email': 'jagi@gmail.com', 'name': 'joan', 'password': 'jojo','roles':'attendant'}
			self.login_user_admin={'email': 'john@gmail.com','password': 'joj0o'}
			self.login_user_attendant={'email': 'jagi@gmail.com','password': 'jojo'}

		def register_user(self,email="", password="",roles="",name=""):
			user_data = self.register_user
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self, email="", password=""):
			user_data =self.user
			return self.client.post('/api/v2/auth/login', data=user_data)

		


		def test_product_empty(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps({}),
			content_type = 'application/json')

			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)
		def test_invalid_product_id(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login_user_admin),
			content_type = 'application/json')

			response=self.client.get("api/v1/sale/99999",content_type="application/json")
			self.assertEqual(response.status_code,404)

		def test_product_list(self):
			response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login_user_admin),
			content_type = 'application/json')

			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()
