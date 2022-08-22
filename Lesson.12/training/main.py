import logging
import json
from json import JSONDecodeError

from flask import Flask, request, render_template

# add filemode="w" to overwrite
logging.basicConfig(filename="basic.log", level=logging.INFO)

# Создаем или получаем новый логгер
logger_one = logging.getLogger("one")

# Cоздаем ему обработчик
console_handler = logging.StreamHandler()

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s : %(message)s")
# Применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)

# Добавлякем обработчик к журналу
logger_one.addHandler(console_handler)

logger_one.warning("Логгер первый работает")




logging.basicConfig(filename="basic.log")

try:
    path = "data.json"
    file = open(path)
    items = json.load(file)
    for item in items:
        print(item)
except FileNotFoundError:
    logging.exception("Ошибка доступа к файлу")

except JSONDecodeError:
    # Будет выполнено если файл найден, но не превращается из JSON
    logging.exception("Файл не удается преобразовать")


app = Flask(__name__)

@app.route('/',)
def page_index():
    logging.info("Главная страница запрошена")
    return "Главная страница"

@app.route('/store')
def page_store():
    logging.info("Страница магазина запрошена")
    return "Страница магазина "

@app.route('/store/<cat>')
def page_cat(cat):
    logging.info(f"Страница категории {cat} запрошена")
    return f"Страница категории {cat} "

app.run()