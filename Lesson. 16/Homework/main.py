import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


def load_data(path):
    with open(path) as file:
        return json.load(file)


def load_offer(path):
    offers = load_data(path)

    for offer in offers:

        db.session.add(Offer(**offer))
        db.session.commit()


def load_user(path):
    users = load_data(path)

    for user in users:
        db.session.add(User(**user))
        db.session.commit()


def load_order(path):
    orders = load_data(path)

    for order in orders:
        db.session.add(Order(**order))
        db.session.commit()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def return_data(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def return_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer": self.customer,
            "executor": self.executor
        }


class Offer(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    order = db.relationship("Order")
    executor = db.relationship("User")

    def return_data(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "order": self.order,
            "executor": self.executor
        }


db.drop_all()
db.create_all()

load_order(r"E:\Skypro_lesson_projects\Lesson. 16\Homework\Data\orders.json")
load_offer(r"E:\Skypro_lesson_projects\Lesson. 16\Homework\Data\offers.json")
load_user(r"E:\Skypro_lesson_projects\Lesson. 16\Homework\Data\users.json")


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(user.return_data())

        return app.response_class(json.dumps(result), mimetype="application/json", status=200)

    if request.method == 'POST':

        data = request.json

        db.session.add(User(**data))

        return app.response_class(json.dumps("Done"), mimetype="application/json", status=200)


@app.route("/users/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_user(sid: int):
    user = User.query.get(sid)
    if request.method == 'GET':
        if user is None:
            return "user not found"

        return json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        }, ensure_ascii=False)

    if request.method == 'PUT':

        if user is None:
            return "user not found"

        data = request.json
        user.id = data.get("id")
        user.first_name = data.get("first_name")
        user.age = data.get("age")
        user.email = data.get("email")
        user.role = data.get("role")
        user.phone = data.get("phone")

        db.session.commit()

    if request.method == 'DELETE':
        if user is None:
            return "user not found"

        db.session.delete(user)
        db.session.commit()


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        result = []
        for order in db.session.query(Order).all():
            result.append(order.return_data())

        return app.response_class(json.dumps(result), mimetype="application/json", status=200)

    if request.method == 'POST':

        data = request.json

        db.session.add(Order(**data))

        return app.response_class(json.dumps("Done"), mimetype="application/json", status=200)


@app.route("/orders/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_order(sid: int):
    order = Order.query.get(sid)
    if request.method == 'GET':

        if order is None:
            return "order not found"

        return json.dumps({
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
        }, ensure_ascii=False)

    if request.method == 'PUT':

        if order is None:
            return "order not found"

        data = request.json
        order.id = data.get("id")
        order.name = data.get("name")
        order.description = data.get("description")
        order.start_date = data.get("start_date")
        order.end_date = data.get("end_date")
        order.address = data.get("address")
        order.price = data.get("price")

        db.session.commit()

    if request.method == 'DELETE':
        if order is None:
            return "order not found"

        db.session.delete(order)
        db.session.commit()


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        result = []
        for offer in db.session.query(Offer).all():
            result.append(offer.return_data())

        return app.response_class(json.dumps(result), mimetype="application/json", status=200)

    if request.method == 'POST':

        data = request.json

        db.session.add(Offer(**data))

        return app.response_class(json.dumps("Done"), mimetype="application/json", status=200)


@app.route("/offers/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_offer(sid: int):
    offer = Offer.query.get(sid)
    if request.method == 'GET':

        if offer is None:
            return "offer not found"

        return json.dumps({
            "id": offer.id,
            "order_id": offer.order_id,
        }, ensure_ascii=False)

    if request.method == 'PUT':

        if offer is None:
            return "offer not found"

        data = request.json
        offer.id = data.get("id")
        offer.order_id = data.get("order_id")

        db.session.commit()

    if request.method == 'DELETE':
        if offer is None:
            return "offer not found"

        db.session.delete(offer)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
