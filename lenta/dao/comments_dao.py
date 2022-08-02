import json

from .comment import Comment
from .posts_dao import PostDAO

from flask import current_app as app

class CommentsDAO:
    def load_data(self):
        path_data = app.config.get("PATH_COMMENTS")
        with open(path_data, "r", encoding="utf-8") as file:
            comments_data = json.load(file)
            comments = []
            for comment in comments_data:
                comments.append(Comment(
                    comment["post_id"],
                    comment["commenter_name"],
                    comment["comment"],
                    comment["pk"],
                ))
            return comments

    def get_comments_by_post_id(self, post_id):
        postdao = PostDAO()
        post = postdao.get_post_by_pk(post_id)
        if not post:
            raise ValueError("Такого поста нет")
        comments = self.load_data()
        result = []
        for comment in comments:
            if comment.post_id == post_id:
                result.append(comment)
        return result