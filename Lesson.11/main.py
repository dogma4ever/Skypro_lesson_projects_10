from flask import Flask, render_template
from utils import *
app = Flask(__name__)

candidates = load_candidates_from_json('candidates.json')


@app.route("/")
def page_index():
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def page_candidates(id):
    candidate = get_candidate(candidates, id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    searched_candidates = get_candidates_by_name(candidates, candidate_name)
    if not candidate_name:
        return "Кандидат не найден"
    return render_template('search.html', searched_candidates=searched_candidates)


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates_whit_skill = get_candidates_by_skill(candidates, skill)
    return render_template('skill.html', candidates_whit_skill=candidates_whit_skill, skill=skill)


app.run()
