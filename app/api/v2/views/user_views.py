import psycopg2
from flask import jsonify, make_response, request, json
from flask_restful import Resource,reqparse
from app.api.v2.models.user_models import User
from app.api.db.db_con import db_connect

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
		data = json.loads(request.data)
		print(data)
		# args = parser.parse_args()
		# name = args['name'].strip()
		# email = args['email'].strip()
		# password = args['password'].strip()

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
		args = parser.parse_args()
		name = args['name'].strip()
		email = args['email'].strip()
		password = args['password'].strip()
		user_exists=User.exists(data)


		if not user_exists:
			return make_response(jsonify({'message': 'email does not exist'}), 400)
		else:
			"""create a token after user logs in"""
			return make_response(jsonify({'message':'successful login'}))
