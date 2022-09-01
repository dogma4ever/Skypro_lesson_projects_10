import logging
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from functions import save_picture, add_post


# Добавим настройку папки с шаблонами
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# Добавим render_template
@loader_blueprint.route('/post')
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Отсутствтует картнка/текст'
    if picture.filename.split('.')[-1] not in ["jpg", "jpeg", "png", "tiff", "DNG"]:
        logging.info("Загруженный файл не картинка")
        return "Не корректный формат файла"
    try:
        picture_path: str = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла с постами")
        return "Файл не найден"
    except JSONDecodeError:
        logging.error("Не корректный формат файла с постами")
        return "Не корректный файл"
    post: dict = add_post({'pic': picture_path, 'content': content})
    print(post)

    return render_template('post_uploaded.html', post=post)
