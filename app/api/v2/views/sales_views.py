from datetime import datetime
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.product_models import Product
from app.api.v2.models.sales_models import Sale



parser = reqparse.RequestParser()
parser.add_argument('product_id', required=True, help="Id cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")

class Sales(Resource):

	def post(self):
		"""posts a single product"""
		args = parser.parse_args()
		product_id = args['product_id']
		quantity = args['quantity']

		product = Product.get_by_id(product_id)
		if product is None:
			return {"message": "Product is unavailable"}, 404

		remains = product[5] - quantity
		total_price = product[4] * quantity
		name = product[1]
		date_created = datetime.now()

		# if remains <= 0:
		# 	return {"message":"The quantity you want to sell exceeds the available inventory"}

		new_sale = Sale(product_id, quantity, remains, total_price, name, date_created)

		#decrement quantity of product
		# product['quantity'] = remains
		# Sale.quantity_decrease(product_id, product)




		new_sale.save()

		return make_response(jsonify(
			{"message":"Sale record created successfully",
			"status":"created",
			"product":new_sale.__dict__}
			), 201)
