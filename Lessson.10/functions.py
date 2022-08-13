import json


def load_candidates():
    """функция, которая загрузит данные из файла"""
    with open('candidates.json', encoding='utf-8') as file:
        students_list = json.load(file)
        return students_list


def get_all():
    """покажет всех кандидатов"""
    candidates = load_candidates()
    return candidates


def get_by_pk(candidates, pk):
    """вернет кандидата по pk"""
    for candidat in candidates:
        if candidat.get("pk") == pk:
            return candidat


def get_by_skill(candidates, skill_name):
    """функция, которая вернет кандидатов по навыку"""
    candidates_by_skill = []
    for candidat in candidates:
        if skill_name in candidat.get("skills") or skill_name.title() in candidat.get("skills"):\
            candidates_by_skill.append(candidat)
    return candidates_by_skill
