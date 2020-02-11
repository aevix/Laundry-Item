from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import Enter_new_item
from app.models import Laundry
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/home_template', methods=['GET'])
def Home():
    return render_template('home_template.html', title='Home')

@app.route('/Incoming')
def Incoming():
    return render_template('Incoming.html', title='Incoming')

@app.route('/Outgoing')
def Outgoing():
    return render_template('Outgoing.html', title='Outgoing')

@app.route('/New_inventory', methods = ['GET', 'POST'])
def New_inventory():
    form = Enter_new_item()
    if form.validate_on_submit():
        new_item = Laundry(barcode = form.barcode.data, item_type=form.type.data,item_size=form.size.data)
        db.session.add(new_item)
        db.session.commit()
        flash('Item has entered the database!')
        return redirect(url_for('New_inventory'))
    items = Laundry.query.all()
    return render_template('New_inventory.html', title='New_inventory', form=form, items=items)
