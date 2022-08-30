from flask import Flask, request, render_template, send_from_directory
# Импортируем блюпринты из их пакетов
from catalog.views import catalog_blueprint
from hello.profile import profile_blueprint
from messages.views import messages_blueprint

app = Flask(__name__)
# Ограничиваем размер файла здесь
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


# Регистрируем первый блюпринт
app.register_blueprint(catalog_blueprint)
# И второй тоже регистрируем
app.register_blueprint(profile_blueprint)
# Регистрируем блюпринт c указанием префикса
app.register_blueprint(messages_blueprint, url_prefix='/messages')


@app.route('/')
def form_page():
    """эта вьюшка подтягивает шаблон страницы из файла"""
    return render_template('search.html')


@app.route('/add', methods=["POST"])
def add_page():
    """эта вьюшка отбрабатывает данные переданные в форму на страничке"""
    task = request.form['task_name']
    return f'Вы добавили задачу {task}'


@app.route('/search')
def search_page():
    """эта вьюшка отбрабатывает аргументы полученные из адресной строки"""
    s = request.args['s']
    return f'Вы ввели слово {s}'


"""@app.route('/search')
def search_page():
    '''эта вьюшка отбрабатывает аргументы полученные из адресной строки и смотрит что оно не пустое'''
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово {s}'
    # else
    return 'Вы не ввели ничего'"""


@app.route('/filter')
def filter_page():
    """эта вьюшка отбрабатывает аргументы полученные из адресной строки"""
    from_value = request.args['from']
    to_value = request.args['to']
    return f'Ищем в диапазоне от {from_value} до {to_value}'


@app.route('/upload', methods=['POST'])
def page_upload():
    """ Эта вьюшка обрабатывает форму загрузки файла"""

    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # Сохраняем картинку под родным именем в папку uploads
    picture.save(f"./uploads/{filename}")

    return f"Загружен и сохранен файл {filename}"


@app.route("/uploads/<path:path>")
def static_dir(path):
    """эта вьюшка открывает доступ к файлам по пути"""
    return send_from_directory("uploads", path)


@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413


app.run()
