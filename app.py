from flask import Flask, render_template, request
from functions.functions import load_posts, load_comments, get_post_by_pk, search_post, get_profile_by_name
from api.api import blueprint_api
from logger import get_logger

app = Flask(__name__)

log = get_logger(__name__)


@app.route('/')
def view_posts():
    posts = load_posts()
    log.info("Пользователь на главной странице")
    return render_template("index.html", posts=posts)


@app.route("/post/<int:pk>")
def view_post(pk):
    posts = get_post_by_pk(pk)
    log.info(f"Пользователь смотрит пост {pk} подробнее")
    comments = load_comments(pk)
    return render_template('post.html', comments=comments, posts=posts[0])


@app.route("/search")
def search_post_by_word():
    s = request.args.get('s')
    log.info(f"Пользователь ищет пост по запросу {s}")
    post = search_post(s)
    return render_template('search.html', post=post)


@app.route('/users/<name>')
def search_user(name):
    posts = get_profile_by_name(name)
    log.info(f"Пользователь смотрит профиль {name}")
    return render_template('user-feed.html', posts=posts, name=name)


@app.errorhandler(404)
def error_page(e):
    return 'wtf, it is error 404..'


@app.errorhandler(500)
def error_page_f(e):
    return 'wtf, it is error 500..'


app.register_blueprint(blueprint_api)

if __name__ == "__main__":
    app.run()
