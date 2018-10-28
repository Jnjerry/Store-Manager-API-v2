from app.api.db.db_con import db_connect

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
		return cur.fetchall()

	@staticmethod
	def get_by_id(product_id):
		if product_id:
			query = "SELECT * FROM products WHERE product_id = '%s';" % product_id
			con=db_connect()
			cur=con.cursor()
			cur.execute(query)
			return cur.fetchone()
		return False
