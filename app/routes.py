from flask import render_template, flash, redirect, url_for, request
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app import app, db
from app.forms import item_template, search_item, enter_mass
from app.models import Laundry, Search
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/home_template', methods=['GET'])
def Home():
    items = Laundry.query.filter_by(status=False)
    return render_template('home_template.html', title='Home', items=items)

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
                if enter.status == True:
                    flash('Item has not been scanned out!')
                if enter.status == False and Search.query.filter_by(barcode=form.barcode.data).first() == None:
                    searched = Search(barcode=enter.barcode, item_type=enter.item_type, item_size=enter.item_size, status=enter.status)
                    db.session.add(searched)
                    db.session.commit()
    elif form.Incoming.data:
        changes = Search.query.all()
        for change in changes:
            cl = Laundry.query.filter_by(barcode=change.barcode).first()
            cl.status=True
            db.session.commit()
        db.session.query(Search).delete()
        db.session.commit()
        return redirect(url_for('Incoming'))
    items = Search.query.filter_by(status=False)    
    return render_template('Incoming.html', title='Incoming', form=form, items=items)

@app.route('/Outgoing', methods = ['GET', 'POST'])
def Outgoing():
    form = search_item()
    enter = Laundry.query.filter_by(barcode=form.barcode.data).first()
    if form.Search.data:
        if form.validate_on_submit():
            if enter is None:
                flash('Barcode is not registered in the inventory.')
            else:
                if Search.query.filter_by(barcode=form.barcode.data).first() != None:
                    flash('Item is already scanned in the Outgoing queue!')
                if enter.status == False:
                    flash('Item has not been scanned in!')
                if enter.status == True and Search.query.filter_by(barcode=form.barcode.data).first() == None:
                    searched = Search(barcode=enter.barcode, item_type=enter.item_type, item_size=enter.item_size, status=enter.status)
                    db.session.add(searched)
                    db.session.commit()
    elif form.Outgoing.data:
        changes = Search.query.all()
        for change in changes:
            cl = Laundry.query.filter_by(barcode=change.barcode).first()
            cl.status=False
            db.session.commit()
        db.session.query(Search).delete()
        db.session.commit()
        return redirect(url_for('Outgoing'))
    items = Search.query.filter_by(status=True) 
    return render_template('Outgoing.html', title='Outgoing', form=form, items=items)

@app.route('/New_inventory', methods = ['GET', 'POST'])
def New_inventory():
    form = item_template()
    if form.submit.data:
        if form.validate_on_submit():
            new_item = Laundry(barcode = form.barcode.data, item_type=form.type.data,item_size=form.size.data, status=True)
            db.session.add(new_item)
            db.session.commit()
            flash('Item has entered the database!')
            return redirect(url_for('New_inventory'))
    if form.delete.data:
        if form.validate_on_submit():
            sub = Laundry.query.filter_by(barcode=form.barcode.data).first()
            if sub is not None:
                Laundry.query.filter_by(barcode=form.barcode.data).delete()
                db.session.commit()
                flash('Item successfully deleted!')
            else:
                flash('Item is not in the inventory!')
            return redirect(url_for('New_inventory'))


    items = Laundry.query.all()
    return render_template('New_inventory.html', title='New_inventory', form=form, items=items)

@app.route('/Enter_mass', methods=['GET', 'POST'])
def Enter_mass():
    form = enter_mass()
    if form.submit.data:
        string = form.mass_text.data
        string_sl = string.splitlines()
        for sl in string_sl:
            col=sl.split()
            new_item = Laundry(barcode = col[0], item_type=col[1], item_size=col[2])
            db.session.add(new_item)
            db.session.commit()
            flash('Items have entered the data base!')
    return render_template('Enter_mass.html', title='Enter List of Items', form=form)