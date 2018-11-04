from datetime import datetime
from flask import Flask, jsonify, make_response,request
from flask_restful import  Resource
from app.api.v2.validators.secure_endpoints import admin_required,attendant_required
from flask_jwt_extended import jwt_required

from app.api.v2.models.sales_models import Sale
from app.api.v2.models.product_models import Product




class Sales(Resource):

    # @jwt_required
    # @attendant_required
    def get(self):
        sales = Sale.get_sales(self)
        if not sales:
            return make_response(jsonify({"message": "No sale record found"}))
        return make_response(jsonify({"sales":sales}),201)


    # @jwt_required
    # @attendant_required
    def post(self):
        data =request.get_json()
        # sale_id = data['sale_id']
        product_id= data['product_id']
        quantity = data['quantity']



        product=Product.get_product_by_id(product_id)
        if not product:
            return {"message": "No product found"},404



        remaining_quantity=int(product[2]) - int(quantity)
        total_sale = int(product[5]) * int(quantity)
        price = product[5]
        date_created = datetime.now()
        product_id = product[0]


        if remaining_quantity < 0:
            return {"message": "Not enough in stock"}

        newsale = Sale(product_id,quantity,remaining_quantity,price,date_created).create_sale()
        Sale.decrease_quantity(product_id,remaining_quantity)
        return make_response(jsonify(
            {"message":"Sale record created successfully","sale":newsale}), 201)

class SingleSale(Resource):
    def get(self, id):
            sale=Sale.get_by_id(id)
            if not sale:
                return make_response(jsonify({'error': 'sale record not found'}), 404)
            else:
                return make_response(jsonify({'sale': sale}), 200)
