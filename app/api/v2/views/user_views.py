from flask import jsonify, make_response, request
from flask_restful import Resource,reqparse
from app.api.v2.models.user_models import User
from app.api.db.db_con import db_connect
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="name cannot be blank")
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('password', required=True, help="password cannot be blank")

class UserSignUp(Resource):
	def get(self):
		user = User.get_all(self)
		if not user:
			return {"message":"No users yet"},400
		return make_response(jsonify(
			{"message":"All users in the system","users":user,"status":"okay"}),200)


	def post(self):
		data = request.get_json()
		args = parser.parse_args()
		name = args['name'].strip()
		email = args['email'].strip()
		# roles = args['roles'].strip()
		password = args['password'].lower().strip()
		# role=["admin","attendant"]
		# if roles not in role:
		# 	return make_response(jsonify({'message': 'only admin and attendant roles are accepted'}), 400)
		if User.exists(data):
			return make_response(jsonify({'message': 'user with email already exists'}), 400)
		else:
			query=User.create(data)
			con = db_connect()
			cur = con.cursor()
			cur.execute(query)
			cur.close()
			con.commit()

			return make_response(jsonify({'message': 'user created successfully'}), 201)

class UserLogin(Resource):
	def post(self):
		data = request.get_json()
		# args = parser.parse_args()
		# name = args['name'].strip()
		# email = args['email'].strip()
		# password = args['password'].strip()
		user_exists=User.exists(data)


		if user_exists:
			"""create a token after user logs in success"""
			access_token = create_access_token(identity=json_data['email'])
			return make_response(jsonify({'message': "successfully logged in", 'access_token': access_token}), 201)
		else:
			return make_response(jsonify({'message': 'email does not exist'}), 400)







		
