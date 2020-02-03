from flask import Flask
from config import config
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

