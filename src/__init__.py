from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

from src.plot import Scheduler, convert


app = Flask(__name__)
app.config.from_object('src.config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
# s = Scheduler(timedelta(minutes=5)).add_job(convert, [timedelta(minutes=5)])

from . import routes
