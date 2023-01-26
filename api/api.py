from flask import jsonify, Blueprint

from logger import get_logger
from functions.functions import load_posts, get_post_by_pk

blueprint_api = Blueprint("api", __name__)

log = get_logger(__name__)

@blueprint_api.route("/api/posts")
def api_posts():
    posts = load_posts()
    log.info("Пользователь загрузил все посты")
    return jsonify(posts)


@blueprint_api.route("/api/post/<int:pk>")
def api_inform(pk):
    post = get_post_by_pk(pk)
    log.info(f"Пользователь загрузил пост {pk}")
    return jsonify(post)