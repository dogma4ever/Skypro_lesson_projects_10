import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users2"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename_ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")

db.drop_all()
db.create_all()

group_01 = Group(id=1, name="Group#1")
user_api = User(id=1, name="Api", age=3, group=group_01)
user_ann = User(id=2, name="Ann", age=31)
user_alex = User(id=3, name="Alex", age=38)

users = [user_ann, user_api, user_alex]
db.session.add_all(users)

db.session.commit()


@app.route("/users/first")
def get_first_user():
    user = User.query.first()

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age
    })


@app.route("/users/count")
def get_users_count():
    user_count = User.query.count()

    return json.dumps(user_count)


@app.route("/users")
def get_users():
    user_list = User.query.all()

    user_response = []

    for user in user_list:
        user_response.append({
        "id": user.id,
        "name": user.name,
        "age": user.age
    })

    return json.dumps(user_response)


@app.route("/users/<int:sid>")
def get_user(sid: int):
    user = User.query.get(sid)

    if user is None:
        return "user not found"

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age
    })


if __name__ == '__main__':
    app.run(debug=True)
