from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from app.api.v2.models.product_models import Product
from app.api.v2.validators.secure_endpoints import admin_required,attendant_required
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

        @jwt_required
        @attendant_required
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
        @admin_required
        @jwt_required
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
        @jwt_required
        @admin_required
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

class Sales(Resource):
    def create_sale_record():

       user_id = data["user_id"]
       prod_id = data["prod_id"]
       sold_quantity = data["quantity"]
       prod_price = data["prod_price"]
       resp = prod_obj.get_product_by_id(prod_id)
       if resp[0]['prod_quantity'] > sold_quantity and resp[0]['prod_quantity'] > int(resp[0]['minimum_allowed']):
           prod_obj.update_prod_quantity(resp[0]["prod_quantity"] - sold_quantity, prod_id)
           sale_obj = SalesModel(user_id, prod_id, sold_quantity, prod_price)
           sale_obj.create_sale_record()
           return jsonify({"Message": "Sale record created successfully!"}), 201
       return jsonify({"Message": "Sold quantity exceeds what is in stock!"}), 400
