from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length

class item_template(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    status = BooleanField('Status')
    submit = SubmitField('Enter Item')
    delete = SubmitField('Delete')

class search_item(FlaskForm):
    barcode = StringField('Barcode', validators=None)
    Search = SubmitField(label='Search')
    Incoming = SubmitField(label='Incoming')
    Outgoing = SubmitField(label='Outgoing')

class enter_mass(FlaskForm):
    mass_text= TextAreaField(label='String Entry', validators=[DataRequired(),Length(min=1,max=1000)])
    submit = SubmitField(label='Enter Items')





