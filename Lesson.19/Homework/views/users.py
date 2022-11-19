from flask_restx import Resource, Namespace
from flask import request
from models import User, UserSchema
from setup_db import db

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        rs = db.session.query(User).all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        new_user = User(**req_json)
        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@user_ns.route('/<int:rid>')
class UserView(Resource):
    def get(self, rid):
        user = db.session.query(User).get(rid)
        user_d = UserSchema().dump(user)
        return user_d, 200

    def put(self, rid):
        user = User.query.get(rid)
        req_json = request.json
        user.username = req_json.get("username")
        user.password = req_json.get("password")
        user.role = req_json.get("role")
        db.session.add(user)
        db.session.commit()
        return "", 204

    def patch(self, rid):
        user = User.query.get(rid)
        req_json = request.json
        if "username" in req_json:
            user.username = req_json.get("username")
        if "password" in req_json:
            user.password = req_json.get("password")
        if "role" in req_json:
            user.role = req_json.get("role")
        db.session.add(user)
        db.session.commit()
        return "", 204

    def delete(self, rid: int):
        user = User.query.get(rid)
        db.session.delete(user)
        db.session.commit()
        return "", 204
