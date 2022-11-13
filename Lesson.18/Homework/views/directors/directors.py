from flask_restx import Resource, Namespace
from setup_db import db
from models import Director, director_schema, directors_schema
from flask import request

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    def get(self, uid: int):
        try:
            director = Director.query.get(uid)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404

    def put(self, uid):
        director = Director.query.get(uid)
        req_json = request.json
        director.name = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def patch(self, uid):
        director = Director.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            director.title = req_json.get("title")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        director = Director.query.get(uid)
        db.session.delete(director)
        db.session.commit()
        return "", 204