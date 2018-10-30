
import unittest
import json

from app import create_app


class ProductsTestCase(unittest.TestCase):
		def setUp(self):
			self.client= create_app('testing').test_client()
			self.product_data = {"name":"purple hibiscus", "category":"african", "description": "biographies","price":"price","quantity":"40"}
			# self.user = {'name':'joan','email':'ngugi.joan2@gmail.com', 'roles':'admin', 'password':'@254'}

		def register_user(self,name='joan',email='ngugi.joan2@gmail.com',roles='admin',password='@254'):
			user_data = {
					'name':name,
					'password':password,
					'email':email,
					'roles':roles


			}
			return self.client.post('/api/v2/auth/register', data=user_data)

		def login_user(self,name='joan',email='ngugi.joan2@gmail.com',roles='admin',password='@254'):
			user_data = {
					'name':name,
					'password':password,
					'email':email,
					'roles':roles


			}
			return self.client.post('/api/v2/auth/login', data=user_data)



		#test to check if admin or store attendant can get product list
		def test_product_list(self):
			"""send HTTP GET request to the application on specified path"""
			response=self.client.get('api/v2/products',content_type="application/json")
			self.assertEqual(response.status_code,200)

		def test_create_product(self):
			self.register_user()
			result = self.login_user()
			access_token = json.loads(result.data.decode())['access_token']
			response = self.client.post('/api/v2/products',
				headers=dict(Authorization="Bearer " + access_token),
				data=self.product_data,)

			self.assertEqual(response.status_code, 201)


		# def test_get_one_product(self):
		# 	response=self.client.get("api/v2/products/1",content_type="application/json")
		# 	self.assertEqual(response.status_code,200)



if __name__=="__main__":
	unittest.main()
