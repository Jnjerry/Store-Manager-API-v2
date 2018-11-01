import unittest
import json

from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"name":"Americanah", "category":"African", "description":"Written by Chimamanda","price":"1500","quantity":"20"}
			self.user = {'name':'twyyy','email':'twigyyy@gail.com', 'password':'dsaf','roles':'admin'}
			self.less_product_details={"name":"Americanah", "category":"African"}
			self.header = {"Content-Type": "application/json"}

		def register_user(self,name='',email='',roles='',password=''):
			user_data = json.dumps(self.user)
			return self.client.post('/api/v2/auth/register', headers={'content_type':'application/json'}, data=user_data)

		def login_user(self,name='',email='',roles='',password=''):
			user_data = self.user
			return self.client.post('/api/v2/auth/login',headers={'content_type':'application/json'},data=user_data)



		#test to check if admin or store attendant can get product list
		def test_product_list(self):
			"""send HTTP GET request to the application on specified path"""
			# response=self.client.get('api/v2/products',content_type="application/json")
			# self.assertEqual(response.status_code,200)
			user=self.register_user()
			# login=self.login_user()
			print(user,'------------------')
			# print(login,'------------------')

		def test_create_product(self):
			self.register_user()
			result = self.login_user()
			response = self.client.post('/api/v2/products',
				data=json.dumps(self.product_data),
				headers={'content_type':'application/json'}
				)
			self.assertEqual(response.status_code, 201)
		#
		# def test_invalid_product_id(self):
		# 	response=self.client.get("api/v2/products/900",content_type="application/json")
		# 	self.assertEqual(response.status_code,404)
		#
		# def test_empty_space(self):
		# 	self.register_user()
		# 	result = self.login_user()
		# 	response=self.client.post("api/v2/products/{}",content_type="application/json")
		# 	self.assertEqual(response.status_code,404)
		#
		# def test_api_can_get_all(self):
		# 	results = self.register_user()
		# 	result = self.login_user()
		# 	print(results, "token-----------------------")
		# 	access_token = json.loads(result.data.decode())['access_token']
		# 	res = self.client.post(
		# 		'/api/v2/products',
		# 		headers=dict(Authorization="Bearer " + access_token),
		# 		data=self.product_data)
		# 	self.assertEqual(res.status_code, 201)
		# 	res = self.client.get(
		# 	   '/api/v2/products',
		# 		headers=dict(Authorization="Bearer " + access_token),
		# 	)
		# 	self.assertEqual(res.status_code, 200)





if __name__=="__main__":
	unittest.main()
