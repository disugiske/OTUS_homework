import requests
from models import User, Post
from models.database import db

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def get_userdata():
    userdata = requests.get(USERS_DATA_URL).json()
    return userdata


def get_posts():
    postdata = requests.get(POSTS_DATA_URL).json()
    return postdata


users_data, posts_data = get_userdata(), get_posts()


def load_json_users():
    for list_data in users_data:
        user_json = User(
            name=list_data.get("name"),
            username=list_data.get("username"),
            email=list_data.get("email"),
            user_id=list_data.get("id"),
        )
        db.session.add(user_json)
    for post_data in posts_data:
        post_json = Post(user_id=post_data.get("userId"), body=post_data.get("body"))
        db.session.add(post_json)
    db.session.commit()


def load_deleted_user():
    for list_data in users_data:
        b = User.query.filter(User.name == list_data.get("name")).all()
        if b == []:
            users = User(
                name=list_data.get("name"),
                username=list_data.get("username"),
                email=list_data.get("email"),
            )

            for data in posts_data:
                if list_data.get("id") == data.get("userId"):
                    db.session.add(Post(author=users, body=data.get("body")))
            db.session.add(users)
    db.session.commit()
