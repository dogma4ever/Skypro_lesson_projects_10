import json


def read_from_file(path):
    """считываем из файла данные"""
    with open(path, encoding='utf-8') as file:
        post_list = json.load(file)
        return post_list


def search_posts(posts, search_phrase):
    """ищем пост в файле"""
    posts_list = []
    for post in posts:
        if search_phrase in post("content"):
            posts_list.append(post)
    return posts_list


def write_to_file(path, data):
    """дописываем данные в файл"""
    with open(path, 'a',  encoding='utf-8') as f:
        f.write(data + '\n')


