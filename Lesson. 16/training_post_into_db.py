from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

db.drop_all()
db.create_all()

user_john = User(id=1, name="John", age=30)
user_kate = User(id=2, name="Kate", age=31)
user_alex = User(id=3, name="Alex", age=38)

db.session.add(user_alex)

users = [user_kate, user_john]
db.session.add_all(users)

print(db.session.new)

db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
