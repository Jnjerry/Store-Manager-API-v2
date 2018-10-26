from flask_restful import Api
from flask import Blueprint





#version using Blueprint
version2 = Blueprint('api version2', __name__, url_prefix='/api/v2')
api = Api(version2)

#api end points
