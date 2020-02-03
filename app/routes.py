from flask import render_template, flash
from app import app, db


@app.route('/')
@app.route('/home_template')
def Home():
    return render_template('home_template.html', title='Home')
