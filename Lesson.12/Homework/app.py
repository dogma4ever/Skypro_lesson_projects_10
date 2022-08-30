from flask import Flask, send_from_directory, render_template, request
from functions import read_from_file, search_posts
from main.views import main_blueprint
from loader.views import loader_blueprint


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринт главной страницы
app.register_blueprint(main_blueprint)

# Регистрируем блюпринт страницы постов
app.register_blueprint(loader_blueprint)


@app.route('/search')
def search_page():
    """эта вьюшка отбрабатывает аргументы полученные из адресной строки"""
    s = request.args['s']
    se = search_posts(read_from_file(s))
    return render_template('post_list.html', search=se)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
