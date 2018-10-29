from app.api.db.db_con import db_connect
from flask_jwt_extended import create_access_token,get_jwt_identity
from werkzeug.security import check_password_hash
from functools import wraps
from flask import abort
import datetime

class User(object):
    @staticmethod
    def create(data):
        query = "INSERT INTO users (name,email,password,roles)" \
                "VALUES('%s','%s', '%s','%s')"% (
                    data['name'],data['email'],data['password'],data['roles'])
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

    
