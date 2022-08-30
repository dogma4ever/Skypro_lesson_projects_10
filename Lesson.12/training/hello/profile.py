# hello / profile.py

# Сперва импортируем класс блюпринта
from flask import Blueprint

# Затем создаем новый блюпринт, выбираем для него имя
profile_blueprint = Blueprint('profile_blueprint', __name__)

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@profile_blueprint.route('/profile/<int:user_id>')
def profile_page(user_id):
    return f"Я страничка профиля пользователя {user_id}"