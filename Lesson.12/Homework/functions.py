import json, logging

"""logging.basicConfig(filename="basic.log", level=logging.ERROR)
logging.getLogger("Error")"""


def load_posts() -> list[dict]:
    """считываем из файла данные"""
    with open("posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts(search_phrase: str) -> list[dict]:
    """ищем пост в файле"""
    posts_list = []
    for post in load_posts():
        if search_phrase.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list


def write_to_file(path, data):
    """дописываем данные в файл"""
    with open(path, 'a',  encoding='utf-8') as f:
        f.write(data + '\n')


def save_picture(picture) -> None:
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)
    return path


def add_post():
    pass