from app.api.db.db_con import db_connect
from werkzeug.security import generate_password_hash
from psycopg2 import sql
import psycopg2.extras




class User(object):
    @staticmethod
    def create(data):
        query = "INSERT INTO users (name,email,password)" \
                "VALUES('%s','%s', '%s')"% (
                    data['name'],data['email'],data['password'])
        return query

    @staticmethod
    def exists(data):
        if data['email']:
            query="SELECT * FROM users WHERE email = '%s';" % data['email']

            con = db_connect()
            cur = con.cursor()
            cur.execute(query)
            return cur.fetchone()
        return False

    @staticmethod
    def get_by_email(email):
        if email:
            query="SELECT * FROM users WHERE email = '%s';" % email

            con = db_connect()
            cur = con.cursor()
            cur.execute(query)
            return cur.fetchone()
    @staticmethod
    def get_all(self):
        query = "SELECT * FROM users"

        con = db_connect()
        cur = con.cursor()
        cur.execute(query)
        return cur.fetchall()
