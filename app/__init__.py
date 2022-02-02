from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from . import routes