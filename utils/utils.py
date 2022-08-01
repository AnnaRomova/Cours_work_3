import json
from os import path

def read_function(path_):
    """Common fucntion for reading files"""
    try:
        file_extension = path.splitext(path_)[-1]
        with open(path_, "r", encoding='utf8') as f:
            if file_extension == '.json':
                data = json.load(f)
            else:
                data = f.read()
        return data
    except:
        print("blabla")

def get_posts_all():
    """Return the list og all posts"""
    # TODO перенести путь в конфиг
    result = read_function(r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\data.json")
    return result

def get_posts_by_user(user_name):
    """Return posts by name"""
    # TODO перенести путь в конфиг, не возвращает пустой список
    posts = read_function(r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\data.json")
    result = []
    for post in posts:
        if post["poster_name"] == user_name:
            result.append(post)
    if result:
        return result
    else:
        raise ValueError("Такого пользователя нет")
        #return result


def get_comments_by_post_id(post_id):
    """Return all comments by post id"""
    # TODO перенести путь в конфиг
    post = get_post_by_pk(post_id)
    if not post:
        raise ValueError("Такого поста нет")
    comments = read_function(r"C:\Users\anna1\skypro_lessons\Cours_work_3\coursework2_source\data\comments.json")
    result = []
    for comment in comments:
        if comment["post_id"] == post_id:
            result.append(comment)
    return result

def search_for_posts(query: str):
    """The function finds posts by a word"""
    data = get_posts_all()
    result = []
    for post in data:
        if query.lower() in post["content"].lower():
            result.append(post)
    return result

def get_post_by_pk(pk):
    """Return post by pk"""
    data = get_posts_all()
    for post in data:
        if post["pk"] == pk:
            return post
    return None