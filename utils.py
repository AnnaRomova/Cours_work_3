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
    """"""
    pass

def get_posts_by_user(user_name):
    """"""
    pass

def get_comments_by_post_id(post_id):
    """"""
    pass

def search_for_posts(query):
    """"""
    pass

def get_post_by_pk(pk):
    """"""
    pass