from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from datetime import timedelta

from app.plot import Scheduler, convert


app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
s = Scheduler(timedelta(minutes=5)).add_job(convert, [timedelta(minutes=5)])

from . import routes
