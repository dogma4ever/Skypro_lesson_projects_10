from flask_restx import Resource, Namespace
from flask import request
from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        director = Director.query.get(rid)
        req_json = request.json
        director.name = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def patch(self, rid):
        director = Director.query.get(rid)
        req_json = request.json
        if "name" in req_json:
            director.title = req_json.get("title")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def delete(self, rid: int):
        director = Director.query.get(rid)
        db.session.delete(director)
        db.session.commit()
        return "", 204
