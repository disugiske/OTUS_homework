from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class PostsForm(FlaskForm):
    name = StringField(
        label="Name",
        name="product-name",
        validators=[
            DataRequired(),
        ],
    )
    mail = StringField(
        label="Email",
        name="Your email",
        default=None,
    )
    post = StringField(
        label="Post",
        name="Text body",
        default=None,
    )
    username = StringField(
        label="Username",
        name="post-field",
        default=None,
    )
