from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta


app = Flask(__name__)
app.config.from_object('src.config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)


from plot import Scheduler, convert
s = Scheduler(timedelta(seconds=20)).add_job(convert, [timedelta(seconds=20)])

from . import routes
