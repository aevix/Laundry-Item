from flask import render_template, flash
from app import app, db


@app.route('/')
@app.route('/home_template', methods=['GET'])
def Home():
    return render_template('home_template.html', title='Home')

@app.route('/Incoming')
def Incoming():
    return render_template('Incoming.html', title='Incoming')

