import json


def load_posts() -> list[dict]:
    """считываем из файла данные"""
    with open("../posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts(search_phrase: str) -> list[dict]:
    """ищем пост в файле"""
    posts_list = []
    for post in load_posts():
        if search_phrase.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list
