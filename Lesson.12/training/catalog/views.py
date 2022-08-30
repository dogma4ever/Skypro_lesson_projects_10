# catalog/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint

# Добавим настройку папки с шаблонами
catalog_blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates')


# Добавим render_template
@catalog_blueprint.route('/catalog')
def catalog_page():
    return render_template("main.html")


# Добавим render_template
@catalog_blueprint.route('/catalog/<cat>')
def category_page(cat):
    return render_template("category.html")


# Добавим render_template
@catalog_blueprint.route('/catalog/<cat>/<int:item>')
def item_page(item):
    return render_template("item.html")
