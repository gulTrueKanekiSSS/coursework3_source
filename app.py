from flask import Flask, render_template, request
from functions import functions
from functions.functions import load_posts, load_comments, get_post_by_pk, search_post, get_profile_by_name

app = Flask(__name__)

@app.route('/')
def view_posts():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:pk>")
def view_post(pk):
    posts = get_post_by_pk(pk)
    comments = load_comments(pk)
    return render_template('post.html', comments=comments, posts=posts[0])

@app.route("/search")
def search_post_by_word():
    s = request.args.get('s')
    post = search_post(s)
    return render_template('search.html', post=post)

@app.route('/users/<name>')
def search_user(name):
    posts = get_profile_by_name(name)
    return render_template('user-feed.html', posts=posts, name=name)


app.run()