import json

from post import Post

class PostDAO:

    def load_data(self):
        """Common fucntion for reading files"""
        with open("data.json", "r", encoding="utf-8") as file:
            posts_data = json.load(file)
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
        data = self.get_posts_all()
        result = []
        for post in data:
            if query.lower() in post.content.lower():
                result.append(post)
        return result

