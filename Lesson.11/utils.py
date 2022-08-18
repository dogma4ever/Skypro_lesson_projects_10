import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, encoding='utf-8') as file:
        candidates_list = json.load(file)
        return candidates_list


def get_candidate(candidates, candidate_id):
    """возвращает одного кандидата по его id"""
    for candidat in candidates:
        if candidat.get("id") == candidate_id:
            return candidat


def get_candidates_by_name(candidates, candidate_name):
    """возвращает кандидатов по имени"""
    searched_candidates = []
    for candidat in candidates:
        if candidate_name.title() in candidat.get("name"):
            searched_candidates.append(candidat)
        return searched_candidates


def get_candidates_by_skill(candidates, skill_name):
    """возвращает кандидатов по навыку"""
    candidates_by_skill = []
    for candidat in candidates:
        candidat_skill_str = candidat.get("skills")
        candidat_skill_str = candidat_skill_str.replace(" ", "")
        candidat_skill_list = candidat_skill_str.split(",")
        for skill in candidat_skill_list:
            if skill == skill_name or skill == skill_name.title():
                candidates_by_skill.append(candidat)
    return candidates_by_skill
