import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'qwerty'
    SQLALCHEMY_DATABASE_URI = "sqlite:///src.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False