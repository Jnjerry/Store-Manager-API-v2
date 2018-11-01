import psycopg2
from .queries import queries
from instance.config import app_config
import os
"""connect to the db and return error if connection fails"""
enviroment = os.environ['ENV']
def db_connect():
    try:
        connection=psycopg2.connect(app_config[enviroment].database_url)
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
