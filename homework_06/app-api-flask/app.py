from os import getenv
from werkzeug.exceptions import NotFound, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError
import logging
from flask_migrate import Migrate
from flask import Flask, request, render_template, url_for, redirect, flash

from forms.posts import PostsForm
from models.create_db_column import User, Post

from models.database import db
from models.jsonplaceholder_requests import load_deleted_user

log = logging.getLogger(__name__)

app = Flask(__name__)
config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="index", methods=["GET", "POST"])
def get_posts_list():
    if request.method == "POST":
        load_deleted_user()
    deleteall = request.args.get('dellall')
    if deleteall == "1":
        db.session.query(Post).delete()
        db.session.query(User).delete()
        db.session.commit()
    users = User.query.all()
    return render_template(
        "posts/list_posts.html",
        users=users,
    )


@app.route("/load_users", endpoint="load_users")
def load_user():
    load_deleted_user()


@app.route("/<int:user_id>/", methods=["GET", "DELETE"], endpoint="details")
def get_user_by_id(user_id: int):
    user = User.query.get(user_id)
    body_list = Post.query.filter_by(user_id=user_id).all()
    if user is None:
        raise NotFound(f"User #{user_id} not found!")

    if request.method == "GET":
        body_str = "".join(map(str, body_list))
        return render_template(
            "posts/details.html",
            user=user,
            body=body_str,
        )
    user_name = user.name
    db.session.delete(user)
    for i in body_list:
        db.session.delete(i)
    # db.session.delete(body)
    db.session.commit()
    flash(f"Deleted product #{user_id} {user_name!r}", "warning")
    url = url_for("index")
    return {"ok": True, "url": url}


@app.get("/about/", endpoint="about")
def hello_name():
    return render_template("about.html")


@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    form = PostsForm()
    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form), 400

    user_name = form.name.data
    email = form.mail.data
    posts = form.post.data
    username = form.username.data

    user_data = User(
        name=user_name,
        username=username,
        email=email,
    )
    post_data = Post(body=posts, author=user_data)
    db.session.add(user_data)
    db.session.add(post_data)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save user {user_name!r}, probably name is not unique!"
        form.form_errors.append(error_text)
        return render_template("posts/add.html", form=form), 400

    # raise BadRequest(error_text)
    except DatabaseError:
        log.exception("could not save user %r", user_name)
        raise InternalServerError(f"could not save user {user_name!r}")

    flash(f"Created new user: {user_data.name}", "success")
    url = url_for("details", user_id=user_data.id)
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True, port=4060)
