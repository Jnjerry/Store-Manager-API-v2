import unittest
import json

from app import create_app


class ProductsTestCase(unittest.TestCase):
	def setUp(self):
		self.client= create_app('testing').test_client()

		self.product_data = {"name":"Americanah", "category":"African", "description":"Written by Chimamanda","price":"1500","quantity":"20"}
		self.register = {'name':'tyy','email':'twigy@gail.com', 'password':'dsaf','roles':'admin'}
		self.login= {'name':'tw','email':'"twigmail.com"', 'password':'dsaf'}
		self.unwanted_data={"nam":"Americanah", "categoy":"African"}
		self.header = {"Content-Type": "application/json"}
		product_url = "/api/v2/products"


	def register_user(self,name='',email='',roles='',password=''):
		user_data = json.dumps(self.register)
		return self.client.post('/api/v2/auth/register', headers={'content_type':'application/json'}, data=user_data)

	def login_user(self,name='',email='',password=''):
		user_data = self.login
		return self.client.post('/api/v2/auth/login',headers={'content_type':'application/json'},data=user_data)


	def test_delete_product(self):
		response = self.client.post('/api/v2/auth/login',data = json.dumps(self.login),
		content_type = 'application/json'
		)
		response_data= json.loads(response.data.decode())['access_token']

		response = self.client.delete('/api/v2/products/9',
		headers=dict(Authorization="Bearer " + access_token)
		)
		self.assertEqual(response.status_code, 200)

		# def test_Register_user(self):
        # response = self.client.post(
        # '/api/v2/users/login',
        #  data = json.dumps(dict(
        #     email='ken@gmail.com',password='12345')),
        #  content_type = 'application/json')
        # response_data = json.loads(response.data.decode())
		#
        # token = json.loads(response.data.decode())['access_token']
		#
        # response = self.client.post('/api/v2/auth/user',
        # data = json.dumps(self.register_valid_email),
        # headers=dict(Authorization="Bearer " + token),
        # content_type = 'application/json')
        # response_data = json.loads(response.data)
        # self.assertEqual(response_data["message"],"Enter correct email format")
        # self.assertEqual(response.status_code, 200)
		#
		#
		# # response = self.client.get('/api/v2/products/1',
		# headers=dict(Authorization="Bearer " + self.owner_token))
		# response_data = json.loads(response.data)
		# self.assertEqual("product not available",response_data["message"])
		#




	# def test_create_sale(self):
	#         self.register_user()
	#         result = self.login_user()
	#         access_token = json.loads(result.data.decode())['access_token']
	#
	#
	#         response = self.client.post('/api/v2/products',
	#             data=json.dumps(self.product_data),
	#             headers=dict(Authorization="Bearer " + access_token),
	#             content_type='application/json'
	#             )
	#
	#         self.assertEqual(response.status_code, 201)





if __name__=="__main__":
	unittest.main()
