import psycopg2
from .queries import queries

"""connect to the db and return error if connection fails"""
def db_connect():
    try:
        connection=psycopg2.connect(
        "dbname='store_manager_api' host='localhost' port='5432' user='postgres' password='m@ngun@1'")
        return connection
    except(Exception,psycopg2.DatabaseError) as error:
        print("Connection failed",error)

"""this method takes in queries that create tables"""
"""it is called when the application runs initially"""
def create_tables():
    try:
        con=db_connect()
        cur=con.cursor()
        for query in queries:
            cur.execute(query)
        print("Tables succssfully created")
    except(Exception,psycopg2.DatabaseError) as error:
         print("Connection failed",error)
    finally:
        con=db_connect()
        cur=con.cursor()
        cur.close()
        con.commit()
        
