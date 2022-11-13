from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from models import Movie, movie_schema, movies_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        all_movies = Movie.query

        if director_id := request.args.get("director_id"):
            all_movies = all_movies.filter(Movie.director_id == director_id)

        if genre_id := request.args.get("genre_id"):
            all_movies = all_movies.filter(Movie.genre_id == genre_id)

        if year := request.args.get("year"):
            all_movies = all_movies.filter(Movie.year == year)

        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movies_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid: int):
        try:
            movie = Movie.query.get(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, uid):
        movie = Movie.query.get(uid)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def patch(self, uid):
        movie = Movie.query.get(uid)
        req_json = request.json
        if "title" in req_json:
            movie.title = req_json.get("title")
        if "description" in req_json:
            movie.description = req_json.get("description")
        if "trailer" in req_json:
            movie.trailer = req_json.get("trailer")
        if "year" in req_json:
            movie.year = req_json.get("year")
        if "rating" in req_json:
            movie.rating = req_json.get("rating")
        if "genre_id" in req_json:
            movie.rating = req_json.get("genre_id")
        if "director_id" in req_json:
            movie.rating = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        movie = Movie.query.get(uid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204
