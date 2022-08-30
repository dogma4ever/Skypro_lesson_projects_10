from flask import render_template, Blueprint

messages_blueprint = Blueprint('messages_blueprint', __name__)

@messages_blueprint.route('/')
def main_page():
    return "Это страничка сообщений"

@messages_blueprint.route('/inbox')
def inbox_page():
    return "Это страничка входящих сообщений"

@messages_blueprint.route('/sent')
def sent_page():
    return "Это страничка отправленных сообщений"

@messages_blueprint.route('/new')
def new_page():
    return "Это страничка новых сообщений"
