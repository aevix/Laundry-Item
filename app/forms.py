from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
from app.models import Garment

class SearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')