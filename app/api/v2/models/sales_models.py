from app.api.db.db_con import db_connect
from flask_jwt_extended import create_access_token,get_jwt_identity
from flask import abort
import datetime

class Sale():
	def __init__(self, product_id="", quantity="", remains="", price="", name="", date_created=""):
		self.product_id = product_id
		self.quantity = quantity
		self.remains = remains
		self.price = price
		self.name = name
		self.date_created = date_created

	@staticmethod
	def create_sales(data):
		query = "INSERT INTO sales (product_id,quantity,remains,price,name,date_created)" \
				"VALUES('%s','%s', '%s','%s','%s', now())"% (
				data['product_id'],data['quantity'],3,4,5)
		con=db_connect()
		cur=con.cursor()
		cur.execute(query)
		con.commit()
		return query









	@staticmethod
	def get_by_id(product_id):
		if product_id:
			query = "SELECT * FROM products WHERE product_id = '%s';" % product_id
			con=db_connect()
			cur=con.cursor()
			cur.execute(query)
			return cur.fetchone()
		return False
	# @staticmethod
	# def get_sales():
	# 	query="SELECT * FROM sales"
	# 	con=db_connect()
	# 	cur=con.cursor()
	# 	cur.execute(query)
	# 	all_sales=cur.fetchall()
	#     rows = []
	#     for row in sales:
	#         rows.append(dict(row))
	#     if rows is None:
	#         return None
	#     con.commit()
		# return rows
