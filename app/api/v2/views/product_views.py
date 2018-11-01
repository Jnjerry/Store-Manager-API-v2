from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from app.api.v2.models.product_models import Product
from app.api.v2.models.sales_models import Sale
from app.api.v2.validators.secure_endpoints import admin_required
from flask_jwt_extended import jwt_required,get_jwt_claims
from app.api.db.db_con import db_connect

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="name cannot be blank")
parser.add_argument('category', required=False)
parser.add_argument('roles', required=False)
parser.add_argument('description', type=str, required=True, help="description can only be a string")
parser.add_argument('price', type=int , required=True, help="price cannot be empty")
parser.add_argument('quantity', type=int ,required=True, help="quantity has to be n integer")



class Product_List(Resource):

        def get(self):
            product=Product.get_all(self)
            if not product:
                return {"message":"No products yet"},400
            return make_response(jsonify(
                {"message":"All products in the system","product":product,"status":"okay"}),200)


        def post(self):
            data = request.get_json()
            args = parser.parse_args()
            name = args['name'].strip()
            category = args['category'].strip()
            description = args['description'].strip()
            price = args['price']
            quantity = args['quantity']


            if quantity<0:
                return {'message': 'quantity cannot be 0'}, 400
            else:
                query=Product.create_products(data)
                con = db_connect()
                cur = con.cursor()
                cur.execute(query)
                cur.close()
                con.commit()

                return make_response(jsonify({'message': 'product created successfully'}), 201)

        def post(self):
            data = request.get_json()
            args = parser.parse_args()
            name = args['name'].strip()
            category = args['category'].strip()
            description = args['description'].strip()
            price = args['price']
            quantity = args['quantity']


            if quantity<0:
                return {'message': 'quantity cannot be 0'}, 400
            else:
                query=Product.create_products(data)
                con = db_connect()
                cur = con.cursor()
                cur.execute(query)
                cur.close()
                con.commit()

                return make_response(jsonify({'message': 'product created successfully'}), 201)




class Products(Resource):

        """get product by id"""
        def get(self, product_id=None):
                product=Product.get_by_id(product_id)
                if not product :
                    return make_response(jsonify({'error': 'product not found'}), 404)
                else:
                    return make_response(jsonify({'product': product}), 200)
        def put(self,product_id):
            data = request.get_json()

            args = parser.parse_args()
            name = args['name'].strip()
            category = args['category'].strip()
            description = args['description'].strip()
            price = args['price']
            quantity = args['quantity']

            if quantity<0:
                return {'message': 'quantity cannot be 0'}, 400
            else:

                query=Product.update(data,product_id)
                con = db_connect()
                cur = con.cursor()
                cur.execute(query)
                cur.close()
                con.commit()

                return make_response(jsonify({'message': 'product updated successfully'}), 201)

        def delete(self,product_id=None):
            if Product.get_by_id(product_id) != None:
                query=Product.delete_by_id(product_id)
                con = db_connect()
                cur = con.cursor()
                cur.execute(query)
                cur.close()
                con.commit()
                return make_response(jsonify({"message": "product deleted successfully"}), 200)
            else:
                return make_response(jsonify({"message": "product not found"}), 404)
