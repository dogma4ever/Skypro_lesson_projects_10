import json, logging

def load_posts() -> list[dict]:
    """считываем из файла данные"""
    with open("../posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open("../posts.json", 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post


def search_posts(search_phrase: str) -> list[dict]:
    """ищем пост в файле"""
    posts_list = []
    for post in load_posts():
        if search_phrase.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list