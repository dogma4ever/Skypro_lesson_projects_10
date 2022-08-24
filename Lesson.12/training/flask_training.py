from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('search.html')


@app.route('/search')
def search_page():
    s = request.args['s']
    return f'Вы ввели слово {s}'

"""@app.route('/search')
def search_page():
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово {s}'
    # else
    return 'Вы не ввели ничего'"""


@app.route('/filter')
def filter_page():
    from_value = request.args['from']
    to_value = request.args['to']
    return f'Ищем в диапазоне от {from_value} до {to_value}'


app.run()
