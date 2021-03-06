from datetime import datetime
from flask_login import UserMixin
from src import db, login_manager
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
    timestamp = db.Column(db.Float)
    data = db.Column(db.String(2048))
    
    def __init__(self, username, data, timestamp):
        self.username = username
        self.data = data
        self.timestamp = timestamp

    def __repr__(self):
        return '<DataBit({}, {}, {})>'.format(self.username, self.timestamp, self.data)


class LabelPoint(db.Model):
    __tablename__ = 'labelpoint'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    label = db.Column(db.String(64), nullable=False)
    x = db.Column(db.Float)
    y = db.Column(db.Float)

    def __init__(self, username, label, x, y):
        self.username = username
        self.label = label
        self.x = x
        self.y = y

    @property
    def serialize(self):
        return {
            'username': self.username,
            'label': self.label,
            'x': self.x,
            'y': self.y
        }

    def __repr__(self):
        return '<LabelPoint({}, {}, {}, {})>'.format(self.username, self.label, self.x, self.y)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)



