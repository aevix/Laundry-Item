from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length

#this form is for New_inventory.html
class item_template(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    status = BooleanField('Status')
    submit = SubmitField('Enter Item')
    delete = SubmitField('Delete')

#this form is for Incoming.html and Outgoing.html
class search_item(FlaskForm):
    barcode = StringField('Barcode', validators=None)
    Search = SubmitField(label='Search')
    Incoming = SubmitField(label='Incoming')
    Outgoing = SubmitField(label='Outgoing')

#this form is for New_inventory.html when entering large quantity of items into the data base from excel file
class enter_mass(FlaskForm):
    mass_text= TextAreaField(label='String Entry', validators=[DataRequired(),Length(min=1)])
    submit = SubmitField(label='Enter Items')
    Delete_All = SubmitField(label='Delete All')

#this form is for view.html template to look for item in time stamp table
class view_item(FlaskForm):
    barcode = StringField('Barcode', validators=[DataRequired()])
    search = SubmitField(label='Search')





