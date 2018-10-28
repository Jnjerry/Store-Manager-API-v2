from flask_restful import Api
from flask import Blueprint
from .views.user_views import UserSignUp,UserLogin
from .views.product_views import Products



#version using Blueprint
version2 = Blueprint('api version2', __name__, url_prefix='/api/v2')
api = Api(version2)
api.add_resource(UserSignUp,'/auth/register')
api.add_resource(UserLogin,'/auth/login')
api.add_resource(Products,'/products')


#api end points
