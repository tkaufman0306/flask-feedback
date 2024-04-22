from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    """login form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=6, max=55)],
        )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )