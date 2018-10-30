import unittest
import json

from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"name":"Americanah", "category":"African", "description":"Written by Chimamanda","price":"1500","quantity":"20"}
			self.user = {'name':'njerr','email':'njer@gmail.com', 'password':'dsaf','roles':'admin'}
			self.header = {"Content-Type": "application/json"}
		def register_user(self,name='',email='',roles='',password=''):
			user_data = self.user
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self,name='',email='',roles='',password=''):
			user_data = self.user
			return self.client.post('/api/v2/auth/login', data=user_data)



		#test to check if admin or store attendant can get product list
		def test_product_list(self):
			"""send HTTP GET request to the application on specified path"""
			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)

		def test_create_new_product(self):
		        '''test admin can create a new product'''
		        data = self.product_data
		        response = self.client.post('/api/v2/products',
		            data=json.dumps(data), headers=self.header)

		        result = json.loads(response.data.decode())

		        self.assertEqual(response.status_code, 201)
		        

		# def test_create_product(self):
		# 	self.register_user()
		# 	result = self.login_user()
		# 	access_token = json.loads(result.data.decode())['access_token']
		# 	response = self.client.post('/api/v2/products',data=self.product_data,
		# 		headers=dict(Authorization="Bearer " + access_token))
		#
		# 	self.assertEqual(response.status_code, 201)


		# def test_get_one_product(self):
		# 	response=self.client.get("api/v2/products/1",content_type="application/json")
		# 	self.assertEqual(response.status_code,200)



if __name__=="__main__":
	unittest.main()
