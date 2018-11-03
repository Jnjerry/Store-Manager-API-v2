from datetime import datetime
from flask import Flask, jsonify, make_response,request
from flask_restful import  Resource
from app.api.v2.validators.secure_endpoints import admin_required,attendant_required
from flask_jwt_extended import jwt_required

from app.api.v2.models.sales_models import Sale
from app.api.v2.models.product_models import Product




class Sales(Resource):

    @jwt_required
    @admin_required
    def get(self):
        sales = Sale.get_sales(self)
        if not sales:
            return make_response(jsonify({"message": "No sale record found"}))
        return make_response(jsonify({"sales":sales}),201)


    @jwt_required
    @attendant_required
    def post(self):
        data =request.get_json()
        # sale_id = data['sale_id']
        product_id= data['product_id']
        quantity = data['quantity']



        product=Product.get_by_id(product_id)
        if not product:
            return {"message": "No product found"},404



        remaining_quantity=int(product[5]) - int(quantity)
        total_sale = int(product[4]) * int(quantity)
        price = product[4]
        date_created = datetime.now()
        product_id = product[0]


        if remaining_quantity < 0:
            return {"message": "Not enough in stock"}

        newsale = Sale(product_id,quantity,remaining_quantity,price,date_created).create_sale()
        print(newsale)
        Sale.decrease_quantity(product_id,remaining_quantity)
        return make_response(jsonify(
            {"message":"Sale record created successfully"}), 201)
