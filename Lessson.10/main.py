from flask import Flask
from functions import *
app = Flask(__name__)

candidates = get_all()


@app.route("/")
def page_index():
    list_of_candidats = ''
    for candidat in candidates:
        candidat_name = candidat.get("name")
        candidat_position = candidat.get("position")
        candidat_skills = candidat.get("skills")
        list_of_candidats += candidat_name + "<br>" + candidat_position + "<br>" + candidat_skills + "<br>" + "<br>"
    return f"<pre>{list_of_candidats}</pre>"


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    candidat = get_by_pk(candidates, pk)
    candidat_url = candidat.get("picture")
    candidat_name = candidat.get("name")
    candidat_position = candidat.get("position")
    candidat_skills = candidat.get("skills")
    return f"<img src='({candidat_url})'><br><pre>{candidat_name}<br>{candidat_position}<br>{candidat_skills}</pre>"

app.run()
