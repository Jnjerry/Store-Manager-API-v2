from app.api.db.db_con import db_connect
import json

con=db_connect()
cur=con.cursor()

class Product(object):
	def __init__(self, name="", category="", description="", quantity="", price=""):
		self.name = name
		self.category = category
		self.description=description
		self.quantity = quantity
		self.price = price

	@staticmethod
	def create_products(newproduct):
		cur.execute("""INSERT INTO products(name, category, description,quantity,price)
					VALUES('%s', '%s','%s','%s','%s');"""%(
		newproduct.name,newproduct.category,newproduct.description,newproduct.quantity,newproduct.price))
		con.commit()


	@staticmethod
	def get_all(self):
		query="SELECT * FROM products"

		cur.execute(query)
		all_products=cur.fetchall()
		if all_products:
			prod_list=[]
			for item in all_products:
				my_item={
					'product_id':item[0],
					'name':item[1],
					'quantity':item[2],
					'category':item[3],
					'description':item[4],

					'price':item[5],

				}
				prod_list.append(my_item)
		return prod_list

	@staticmethod
	def get_by_id(product_id):
			query = "SELECT * FROM products WHERE product_id = '%s';" % product_id
			cur.execute(query)
			product=cur.fetchall()
			if product:
				prod_id=[]
				for item in product:
					my_item={
						'product_id':item[0],
						'name':item[1],
						'quantity':item[2],
						'category':item[3],
						'description':item[4],

						'price':item[5],

					}
					prod_id.append(my_item)
			return prod_id
	def update(product_id, product):
		cur.execute("UPDATE products SET name = %s, quantity = %s, category = %s, description = %s, price = %s WHERE product_id = %s", (
		product['name'],product['quantity'],product['category'],product['description'],product['price'],product_id))
		con.commit()

	@staticmethod
	def get_product_by_id(product_id):
			query = "SELECT * FROM products WHERE product_id = '%s';" % product_id
			cur.execute(query)
			product=cur.fetchone()
			return product



	@staticmethod
	def delete_by_id(product_id):
		query = "DELETE  FROM products WHERE product_id = '%s';" % product_id
		return query


	@staticmethod
	def product_exists(product_id):
		query="SELECT * FROM products WHERE product_id = '%s';" % product_id
		cur.execute(query)
		return cur.fetchone()

	@staticmethod
	def product_exists_name(name):
			query="SELECT * FROM products WHERE name = '%s';" % name
			cur.execute(query)
			return cur.fetchone()
