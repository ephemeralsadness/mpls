from datetime import datetime
from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

    def __repr__(self):
        return '<User %r>' % self.username


class DataBit(db.Model):
    __tablename__ = 'databit'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.Float, default=datetime.now().timestamp())
    data = db.Column(db.String(2048))
    
    def __init__(self, username, data):
        self.username = username
        self.data = data

    def __repr__(self):
        return '<DataBit %r>' % self.data


class LabelPoint(db.Model):
    __tablename__ = 'labelpoint'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    label = db.Column(db.String(64), nullable=False)
    x = db.Column(db.Float)
    y = db.Column(db.Float)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)



