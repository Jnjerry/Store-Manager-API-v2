rom app.api.db.db_con import db_connect
from flask_jwt_extended import create_access_token,get_jwt_identity
from flask import abort
import datetime

class Sales(object):

	def __init__(self, email, password, roles):
		self.email = email
		self.password = password
		self.roles = roles

	@staticmethod
	def create(data):
		query = "INSERT INTO users (name,email,password,roles)" \
				"VALUES('%s','%s', '%s','%s')"% (
					data['name'],data['email'],data['password'],data['roles'])
		return query
