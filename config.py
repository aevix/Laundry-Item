import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #Creates database if app.db isn't available
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLalchemy feature that signals for debugging
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Pagination limit
    POSTS_PER_PAGE = 25
