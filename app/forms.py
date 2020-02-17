from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length

class item_template(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    status = BooleanField('Status')
    submit = SubmitField('Enter Item')

