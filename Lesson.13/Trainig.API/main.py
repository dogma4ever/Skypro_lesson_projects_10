from flask import Flask, jsonify, request

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False
list_of_words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


@app.route("/1")
def get_json():
    """отдаем словарь по GET"""
    data = {"name": "Алиса"}
    return jsonify(data)


@app.route("/2")

def get_list_json():
    """отдаем список по GET"""
    return jsonify(list_of_words)


books = [

    {"title": "Введение в Python", "price": 1400},
    {"title": "Python для новичков", "price": 2400},
    {"title": "Python  в схемах и мемах", "price": 1800}

]


@app.route("/books")
def get_books_json():
    """отдаем список книг попавших в выборку по полученому в GET параметру s"""

    s = request.args.get("s").lower()

    books_found = []

    for book in books:
        if s in book["title"].lower():
            books_found.append(book)

    return jsonify(books_found)


@app.route("/data", methods=["POST"])
def receive_data_from_json():
    """забираем данные переданые в POST запросе и складываем их в файл"""
    data = request.json

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(data.get("name") + "\n")
        file.write(data.get("phone") + "\n")
        file.write(data.get("email") + "\n")

    return jsonify({"result": "Данные записаны"})


app.run()
