from .database import db


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    posts = db.relationship(
        "Post", backref="author", cascade="all, delete-orphan", passive_deletes=True
    )

    def __repr__(self):
        return f"{self.name}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
    )
    body = db.Column(db.Text)

    def __repr__(self):
        return f"{self.body}"


# user = db.relationship("User", backref="post")
