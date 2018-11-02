from app.api.db.db_con import db_connect
import json
import functools
class Product(object):
	@staticmethod
	def create_products(data):
		query = "INSERT INTO products (name,category,description,quantity,price)" \
				"VALUES('%s','%s', '%s','%s','%s')"% (
					data['name'],data['category'],data['description'],data['quantity'],data['price'])
		return query


	@staticmethod
	def get_all(self):
		query="SELECT * FROM products"
		con=db_connect()
		cur=con.cursor()
		cur.execute(query)
		all_products=cur.fetchall()
		if all_products:
			prod_list=[]
			for item in all_products:
				my_item={
					'product_id':item[0],
					'name':item[1],
					'category':item[2],
					'description':item[3],
					'quantity':item[4],
					'price':item[5],

				}
				prod_list.append(my_item)
		return prod_list

	@staticmethod
	def get_by_id(product_id):
			query = "SELECT * FROM products WHERE product_id = '%s';" % product_id
			con=db_connect()
			cur=con.cursor()
			cur.execute(query)
			product=cur.fetchone()
			return product

	@staticmethod
	def update(data,product_id):
		query="UPDATE products SET name='%s',category='%s',description='%s',quantity='%s',price='%s' WHERE product_id='%s' " %(
		data['name'], data['category'],json.dumps(data['description']),data['quantity'],data['price'],product_id)
		return query

	@staticmethod
	def delete_by_id(product_id):
			query = "DELETE  FROM products WHERE product_id = '%s';" % product_id
			return query


	@staticmethod
	def product_exists(product_id):
			query="SELECT * FROM products WHERE product_id = '%s';" % product_id

			con = db_connect()
			cur = con.cursor()
			cur.execute(query)
			return cur.fetchone()

	
