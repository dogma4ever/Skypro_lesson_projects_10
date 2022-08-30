# Добавим импорт шаблонизатора
from flask import render_template, Blueprint

# Добавим настройку папки с шаблонами
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='../templates')


# Добавим render_template
@loader_blueprint.route('/post', methods=["GET"])
def load_post_page():
    return render_template("post_form.html")