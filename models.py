from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
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
