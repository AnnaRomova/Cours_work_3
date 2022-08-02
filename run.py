# run.py
import logging
from flask import Flask, jsonify

# Импортируем блюпринт
from coursework2_source.lenta.views import lenta_blueprint
from coursework2_source.lenta.dao.posts_dao import PostDAO

new_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/api.logs")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
new_logger.addHandler(file_handler)


# Создаем экземпляр Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

path_ = app.config.get("PATH")
print(path_)
# регистрируем первый блюпринт
app.register_blueprint(lenta_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "какого здесь происходит?"

@app.route("/api/posts")
def get_posts_json():
    postdao = PostDAO()
    posts = postdao.get_all_posts_json()
    return jsonify(posts)



@app.route("/api/posts/<int:post_id>")
def get_post_by_postId_json(post_id):
    postdao = PostDAO()
    post = postdao.get_post_by_id_json(post_id)
    logging.info("blablablabl")
    return jsonify(post)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()