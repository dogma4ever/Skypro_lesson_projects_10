import logging
from json import JSONDecodeError
from functions import search_posts

from flask import render_template, Blueprint, request, json


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """это вьюшка главной страницы"""
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    """эта вьюшка показывает посты полученные из аргументов адресной строки"""
    search = request.args.get('s', '')
    logging.info(f"выполняю поиск по слову {search}")
    try:
        posts = search_posts(search)
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла с постами")
        return "Файл не найден"
    except JSONDecodeError:
        logging.error("Не корректный формат файла с постами")
        return "Не корректный файл"
    return render_template('post_list.html', query=search, posts=posts)
