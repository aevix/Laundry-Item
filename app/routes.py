from flask import render_template, flash, redirect, url_for, request
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app import app, db
from app.forms import item_template, search_item
from app.models import Laundry, Search
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/home_template', methods=['GET'])
def Home():
    return render_template('home_template.html', title='Home')

@app.route('/Incoming', methods = ['GET', 'POST'])
def Incoming():
    form = search_item()
    enter = Laundry.query.filter_by(barcode=form.barcode.data).first()
    if form.Search.data:
        if form.validate_on_submit():
            if enter is None:
                flash('Barcode is not registered in the inventory.')
            else:
                if Search.query.filter_by(barcode=form.barcode.data).first() != None:
                    flash('Item is already scanned in the incoming queue!')
                else:
                    searched = Search(barcode=enter.barcode, item_type=enter.item_type, item_size=enter.item_size, status=enter.status)
                    db.session.add(searched)
                    db.session.commit()
    elif form.Incoming.data:
        db.session.query(Search).delete()
        db.session.commit()
        return redirect(url_for('Incoming'))
    items = Search.query.all()    
    return render_template('Incoming.html', title='Incoming', form=form, items=items)

@app.route('/Outgoing')
def Outgoing():
    return render_template('Outgoing.html', title='Outgoing')

@app.route('/New_inventory', methods = ['GET', 'POST'])
def New_inventory():
    form = item_template()
    if form.validate_on_submit():
        new_item = Laundry(barcode = form.barcode.data, item_type=form.type.data,item_size=form.size.data, status=True)
        db.session.add(new_item)
        db.session.commit()
        flash('Item has entered the database!')
        return redirect(url_for('New_inventory'))
    items = Laundry.query.all()
    return render_template('New_inventory.html', title='New_inventory', form=form, items=items)
