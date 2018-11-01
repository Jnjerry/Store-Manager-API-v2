from datetime import datetime
from flask import Flask, jsonify, make_response,request
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.sales_models import Sale
from app.api.v2.models.product_models import Product
prod_obj = Product()
sales_obj = Sale()



parser = reqparse.RequestParser()
parser.add_argument('product_id', required=True, help="Id cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")

class Sales(Resource):
	"""All products class"""


	def post(self):
		"""posts a single product"""
		data=request.get_json()
		args = parser.parse_args()
		product_id =args['product_id']
		quantity = args['quantity']

		product =Product.get_by_id(product_id)
		price=product[4]


		if product is None:
			return {"message": "Product is unavailable"}, 404



		remains = int(product[5]) - int(quantity)
		price = int(product[4]) * int(quantity)
		name = product[1]
		date_created = datetime.now()
		if remains < 0:
		   return {"message": "Not enough in stock"}

		newsale = Sale(product_id,quantity,remains,price,name,date_created).create_sales(self)
		print(newsale)
		Sale.decrease_quantity(product_id,product)


		return make_response(jsonify(
			{"message":"Sale created",}), 201)

	def get(self):
		"""gets all products"""
		sales = get_sales()
		if sales is None:
			return make_response(jsonify(
				{
				"message": "No sales available"
				}))
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"Sales":sales}), 200)

class SingleSale(Resource):
	'''class represents operations for one sale record'''
	def get(self, id):
		# email = get_jwt_identity()
		# user = get_user(email)
		sale_record = get_sale(id)
		if sale_record is None:
			return make_response(jsonify({"message": "Sale record unavailable"}), 404)
		return make_response(jsonify({"message": "success", "Sale": sale_record}), 200)
