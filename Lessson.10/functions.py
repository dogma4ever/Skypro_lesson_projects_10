import json


def load_candidates():
    """функция, которая загрузит данные из файла"""
    with open('candidates.json') as file:
        students_list = json.load(file)
        return students_list


def get_all():
    """функция, которая покажет всех кандидатов"""
    pass


def get_by_pk(pk):
    """функция, которая вернет кандидата по pk"""
    pass


def get_by_skill(skill_name):
    """функция, которая вернет кандидатов по навыку"""
    pass

load_candidates()