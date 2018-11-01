from ...db.db_con import init_db
class Products():
	def __init__(self, name, quantity, description):
		self.db= init_db()


	def save(self,name,quantity,description):
		payload = {
		'name' : name,
		'quantity' : quantity,
		'description' : description
		}
		query =""" INSERT INTO products (name,quantity,description) VALUES
					(%{name}s,%{price}s,%(quantity)s)"""
		cur=self.db.cursor()
		cur.execute(query,payload)
		self.db.commit()
		return payload
