from flask import Flask, send_from_directory, render_template, request
from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)

# Регистрируем блюпринт главной страницы
app.register_blueprint(main_blueprint)

# Регистрируем блюпринт страницы постов
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
