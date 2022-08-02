from flask import Blueprint, render_template, request
from .dao.posts_dao import PostDAO
from .dao.comments_dao import CommentsDAO

lenta_blueprint = Blueprint('lenta_blueprint', __name__, template_folder="templates")

@lenta_blueprint.route('/')
def page_index():
    postdao = PostDAO()
    posts = postdao.get_posts_all()
    return render_template('index.html', posts=posts)

@lenta_blueprint.route("/posts/<int:pk>")
def page_post(pk):
    postdao = PostDAO()
    post = postdao.get_post_by_pk(pk)
    commentdao = CommentsDAO()
    comments = commentdao.get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)

@lenta_blueprint.route("/search/")
def search_posts():
    postdao = PostDAO()
    s = request.args['s']
    print(s)
    posts = postdao.search_for_posts(s)
    return render_template("search.html", posts=posts)

@lenta_blueprint.route("/users/<string:username>")
def username_posts(username):
    postdao = PostDAO()
    posts = postdao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, username=username)


