from flask import render_template, flash
from app import app, db

@app.route('/')
@app.route('/home_template', methods=['GET'])
def Home():
    items = [
        {'barcode': id, 'type': item_type, 'size': item_size}
    ]
    return render_template('home_template.html', title='Home')

@app.route('/Incoming')
def Incoming():
    return render_template('Incoming.html', title='Incoming')

@app.route('/Outgoing')
def Outgoing():
    return render_template('Outgoing.html', title='Outgoing')

@app.route('/New_inventory')
def New_inventory():
    return render_template('New_inventory.html', title='New_inventory')
