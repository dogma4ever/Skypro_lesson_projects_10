from flask_restx import Resource, Namespace
from flask import request
from models import User, UserSchema
from setup_db import db

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = db.session.query(User).all()
        res = UserSchema(many=True).dump(users)
        return res, 200

    def post(self):
        req_json = request.json
        new_user = User(**req_json)
        new_user["password"] = User.get_hash(new_user["password"])
        with db.session.begin():
            db.session.add(new_user)
        return "", 201, {"location": f"/users/{new_user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = db.session.query(User).get(uid)
        user_d = UserSchema().dump(user)
        return user_d, 200

    def put(self, uid):
        user = User.query.get(uid)
        req_json = request.json
        user.username = req_json.get("username")
        user.password = req_json.get("password")
        user.role = req_json.get("role")
        db.session.add(user)
        db.session.commit()
        return "", 204

    def patch(self, uid):
        user = User.query.get(uid)
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

    def delete(self, uid: int):
        user = User.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204
