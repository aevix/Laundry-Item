from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models, app

#type "flask run -h localhost -p 3000" command line to start sever on localhost 3000 after "venv/scripts/activate"