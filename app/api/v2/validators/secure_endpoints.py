from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort
from app.api.v2.models.user_models import User


def admin_required(f):
    """ A decorator for restricting endpoints to only admins"""
    @wraps(f)
    def decorator(*args, **kwargs):
        current_user = User.get_by_email(get_jwt_identity())
        role = current_user[5]
        if role == 'attendant':
            msg = "Only administrators can access this endpoint"
            abort(406, msg)
        return f(*args, **kwargs)
    return decorator

def attendant_required(f):
    """ A decorator for restricting certain routes to only superadmin/owner of the store"""
    @wraps(f)
    def decorator(*args, **kwargs):
        current_user = User.get_by_email(get_jwt_identity())
        role= current_user[5]
        if role == 'admin':
            msg = "Only attendant can access this endpoint"
            abort(406, msg)
        return f(*args, **kwargs)
    return decorator
