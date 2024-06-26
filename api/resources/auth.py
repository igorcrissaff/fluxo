from flask import Blueprint, abort, request, jsonify
from flask_restful import Resource
import flask_jwt_extended as jwt
from datetime import timedelta

from ..models.user import User

auth = Blueprint('auth', __name__)

class Auth(Resource):
    def get(self):
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first()
        if not user:
            return abort(400, "user nor found")
        
        elif not user.check_password(password):
            return abort(400, 'Invalid password')
                
        else:
            token = jwt.create_access_token(
                identity= user,
                expires_delta=timedelta(days=1)
                )
            return token.strip('"')

