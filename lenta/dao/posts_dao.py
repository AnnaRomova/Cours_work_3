import json

from .post import Post
from flask import current_app as app

class PostDAO:

    def load_data(self, getJSON=None):
        """Common fucntion for reading files"""
        path_ = app.config.get("PATH_DATA")
        with open(path_, "r", encoding="utf-8") as file:
            posts_data = json.load(file)
            if getJSON:
                return posts_data
            posts = []
        # Создаем список объектов класса Post
            for post in posts_data:
                posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
        return posts

    def get_posts_all(self):
        return self.load_data()

    def get_posts_by_user(self, user_name):
        posts = self.load_data()
        result = []
        for post in posts:
            if post.poster_name == user_name:
                result.append(post)
        if result:
            return result
        else:
            raise ValueError("Такого пользователя нет")

    def search_for_posts(self, query: str):
        data = self.load_data()
        result = []
        for post in data:
            if query.lower() in post.content.lower():
                result.append(post)
        return result

    def get_post_by_pk(self, pk):
        """Return post by pk"""
        data = self.load_data()
        for post in data:
            if post.pk == pk:
                return post
        return None

    def get_all_posts_json(self):
        return self.load_data(getJSON=True)

    def get_post_by_id_json(self, pk):
        posts_json = self.get_all_posts_json()
        for post in posts_json:
            if post["pk"] == pk:
                return post