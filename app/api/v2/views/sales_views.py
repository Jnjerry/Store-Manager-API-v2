from datetime import datetime
from flask import Flask, jsonify, make_response,request
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.sales_models import Sale
from app.api.v2.models.product_models import Product




class Sales(Resource):
    def get(self):
        sales = Sale.get_sales(self)
        if not sales:
            return make_response(jsonify({"message": "No sale record found"}))
        return make_response(jsonify({"sales":sales}),201)


    def post(self):
        data =request.get_json()
        # sale_id = data['sale_id']
        product_id  = data['product_id']
        quantity = data['quantity']
        attendant=data['attendant']



        product=Sale.get_product_by_id(product_id)
        print(product)


        if product is None:
            return {"message":"Product is not available"},404

        price = product[3]
        remaining_q=int(product[5]) - int(quantity)
        total_sale = int(product[4]) * int(quantity)
        name = product[1]
        date_created = datetime.now()


        if remaining_q < 0:
            return {"message": "Not enough in stock"}

        newsale = Sale(product_id,quantity,remaining_q,price,name,attendant,date_created).create_sale()
        print(newsale)
        Sale.decrease_quantity(product_id,remaining_q)


        return make_response(jsonify(
            {"message":"Sale record created successfully"}
            ), 201)
        # "status":"created",
        #     "product":newsale



class DeleteSale(Resource):
    def delete(self,sale_id):
        Sale.delete_product(sale_id)
        return {"message":"Deleted successfully"}


class Get_sale_id(Resource):
    def get(self,sale_id):
        sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
        if sal:
            return make_response(jsonify({'sale':sal[0]}),200)
        else:
            return jsonify({'message': "specific sale not found"})
            return 404
