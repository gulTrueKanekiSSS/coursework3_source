import json

def load_data(file_name):
    with open(file_name) as file:
        data = json.load(file)
    return data

def load_posts():
    data = load_data("data/posts.json")
    return data

def load_comments(post_id):
    data = load_data("data/comments.json")
    comments = []
    for comment in data:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments

def get_post_by_pk(pk):
    data = load_data("data/posts.json")
    posts = []
    for post in data:
        if post['pk'] == pk:
            posts.append(post)
    return posts

def search_post(word):
    data = load_data("data/posts.json")
    posts = []
    for post in data:
        if word.lower() in post['content'].lower():
            posts.append(post)
    return posts

def get_profile_by_name(name):
    data = load_data("./data/posts.json")
    posts = []
    for post in data:
        if name in post['poster_name']:
            posts.append(post)
    return posts





