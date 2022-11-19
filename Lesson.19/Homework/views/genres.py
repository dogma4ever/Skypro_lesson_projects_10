from flask_restx import Resource, Namespace
from flask import request
from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = db.session.query(Genre).get(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        genre = Genre.query.get(rid)
        req_json = request.json
        genre.name = req_json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def patch(self, rid):
        genre = Genre.query.get(rid)
        req_json = request.json
        if "name" in req_json:
            genre.title = req_json.get("title")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, rid: int):
        genre = Genre.query.get(rid)
        db.session.delete(genre)
        db.session.commit()
        return "", 204
