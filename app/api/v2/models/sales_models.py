from app.api.db.db_con import db_connect
from flask_jwt_extended import create_access_token,get_jwt_identity
from flask import abort
import datetime

class Sale():

    def __init__(self, product_id="", quantity="", remaining_q="", price="", name="",attendant="", date_created=""):
        self.product_id = product_id
        self.quantity = quantity
        self.remaining_q = remaining_q
        self.price = price
        self.name = name
        self.attendant=attendant
        self.date_created = date_created

    def create_sale(self):
        sale={"product_id":self.product_id,"quantity":self.quantity,"remaining_q":self.remaining_quantity,"price":self.price,"name":self.name, "attendant":self.attendant,"date_created":self.date_created}
        try:
            con=db_connect()
            cur= con.cursor()
            data = cur.execute("INSERT INTO sales(product_id, quantity, remaining_q, price, name,attendant,date_created) VALUES('{}','{}','{}','{}','{}','{}','{}');".format(self.product_id,self.quantity,self.remaining_q,self.price,self.name, self.attendant,self.date_created))
            print(data)
            con.commit()
        except Exception as e:
            print(e)
        return sale

    def get_sales(self):
        query="SELECT * FROM sales"
        con=db_connect()
        cur= con.cursor()
        cur.execute(query)
        db_sales= cur.fetchall()
        if db_sales:
            sales = []
            for items in db_sales:
                item ={
                'sale_id':items[0],
                'products_id':items[1],
                'quantity':items[2],
                'remaining_quantity':items[3],
                'price':items[4],
                'name':items[5],
                'attendant':items[6],
                'date_created':items[7],
                }
                sales.append(item)
            return sales

    def get_product_by_id(product_id):
        con=db_connect()
        cur= con.cursor()
        cur.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        product = cur.fetchone()
        if product is None:
            return None
        con.commit()
        return product
    def decrease_quantity(product_id, remaining_quantity):
        con=db_connect()
        cur= con.cursor()
        cur.execute("UPDATE products SET quantity = %s WHERE product_id = %s", (remaining_quantity,product_id))
        con.commit()
