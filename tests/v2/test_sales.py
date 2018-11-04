import unittest
import json
import os
from app import create_app


class SaleTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"product_id":5, "name":"Purple Hibiscus","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.register_user = {'email': 'jojo-1@gmail.com', 'name': 'joan', 'password': 'jj','roles':'admin'}
			self.register_new_user = {'email': 'njeri-10@gmail.com', 'name': 'ngugijo', 'password': 'm@ngun@1','roles':'attendant'}
			self.login_user={'email': 'njeri-10@gmail.com','password': 'm@ngun@1'}
			self.new_user={'email': 'njerijoan@gmail.com','password': 'm@ngun@1'}
			self.new_data = {"product_id":1000, "name":"Purple Hibiscus-00","category":"Africanah", "description": "Written by Chimamanda","price":1500,"quantity":20}
			self.sale_data={'quantity':2,'product_id':2}


		def test_cannot_sell_non_existent_product(self):
			response = self.client.post('/api/v2/auth/login',
			data = json.dumps(self.login_user),content_type = 'application/json')
			token = json.loads(response.data.decode())['access_token']

			response = self.client.get('/api/v2/products/2000',
			headers=dict(Authorization="Bearer " + token),data = json.dumps(self.new_data),
			content_type = 'application/json')

			response_data = json.loads(response.data)
			self.assertEqual(response.status_code, 404)

		def test_make_sale(self):
			response = self.client.post('/api/v2/auth/login',
			data = json.dumps(self.login_user),content_type = 'application/json')

			token = json.loads(response.data.decode())['access_token']

			response = self.client.post('/api/v2/sales',data = json.dumps(self.sale_data),
			headers=dict(Authorization="Bearer " + token),
			content_type = 'application/json')
			response_data = json.loads(response.data)
			self.assertEqual(response.status_code, 201)
