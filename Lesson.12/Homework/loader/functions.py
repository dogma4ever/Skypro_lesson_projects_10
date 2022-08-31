import json


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
