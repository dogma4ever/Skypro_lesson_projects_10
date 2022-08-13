from flask import Flask
from functions import *
app = Flask(__name__)

atudents_list = load_candidates()

@app.route("/")
def page_index():
    return "Главная страничка"

app.run()