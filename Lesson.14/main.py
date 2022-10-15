import json
import sqlite3
from flask import Flask

app = Flask(__name__)


def get_data_by_sql(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql).fetchall()

    return result


@app.get("/movie/<title>")
def search_by_title(title):
    result = {}
    for item in get_data_by_sql(sql=f"""
            SELECT title, country, release_year, listed_in as genre, description 
            from netflix 
            WHERE title = '{title}'
            ORDER BY release_year DESC
            LIMIT 1
            """):
        result = dict(item)

    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


@app.get("/movie/<int:year1>/to/<int:year2>")
def search_by_year_to_year(year1, year2):
    result = []
    for item in get_data_by_sql(sql=f"""
            SELECT title, release_year
            from netflix 
            WHERE release_year BETWEEN '{year1}' AND '{year2}'
            ORDER BY release_year DESC
            LIMIT 100
            """):
        result.append(dict(item))

    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


@app.get("/rating/<rating>")
def search_by_rating(rating):
    ratings = {"children": ("G", "G"), "family": ("G", "PG", "PG-13"), "adult": ("R", "NC-17")}
    result = []
    for item in get_data_by_sql(sql=f"""
            SELECT title, rating, description
            from netflix 
            WHERE rating IN {ratings.get(rating)}
            LIMIT 100
            """):
        result.append(dict(item))

    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


@app.get("/genre/<genre>")
def search_by_genre(genre):
    result = []
    for item in get_data_by_sql(sql=f"""
            SELECT title, description
            from netflix 
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """):
        result.append(dict(item))

    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        mimetype="application/json",
        status=200
    )


def search_by_actors_pare(actor1, actor2):
    names_list = {}
    for item in get_data_by_sql(sql=f"""
            SELECT "cast"
            from netflix 
            WHERE "cast" LIKE '%{actor1}%' AND "cast" LIKE '%{actor2}%'
            """):
        result = (dict(item))
        cast_names = set(result.get("cast").split(", ")) - set([actor1, actor2])
        for cast_name in cast_names:
            names_list[cast_name] = names_list.get(cast_name, 0) + 1

    for key, value in names_list.items():
        if value > 2:
            return key


def search_by_type_year_genre(types, year, genre):
    result = []
    for item in get_data_by_sql(sql=f"""
            SELECT title, description
            FROM netflix
            WHERE type = '{types}' AND release_year = '{year}' AND listed_in LIKE '%{genre}%'
            """):
        result.append(dict(item))

    return json.dumps(result, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
