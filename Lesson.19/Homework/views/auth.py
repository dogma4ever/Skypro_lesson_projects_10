from utils import generate_access_token, generate_refresh_token, check_token
from flask_restx import Resource, Namespace
from flask import request, abort
from models import User, UserSchema
from setup_db import db


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')
        user = db.session.query(User).filter(User.username == username).one_or_none()

        if not user:
            return None

        hash_password = self.get_hash()

        if not username and not password:
            abort(400)

        if hash_password != user.password:
            abort(401)

        data = {
            "username": user.username,
            "role": user.role
        }

        access_token = generate_access_token(data)
        refresh_token = generate_refresh_token(data)

        return {"access_token": access_token, "refresh_token": refresh_token, "exp": data["exp"]}


    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        check_token(token)
