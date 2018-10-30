from app.api.db.db_con import db_connect
import json

class Sales(object):
	@staticmethod
	def create_products(data):
		query = "INSERT INTO sales (sale_id,product,attendant,quantity,price)" \
				"VALUES('%s','%s', '%s','%s','%s')"% (
					data['name'],data['category'],data['description'],data['quantity'],data['price'])
		return query
