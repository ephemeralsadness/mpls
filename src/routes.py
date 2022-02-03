from datetime import datetime

from src import app, db
from src.models import Users, DataBit, LabelPoint
import src.forms as forms

from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from copy import deepcopy
import json


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
@login_required
def hello_world():
    return render_template('main.html', username=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        username, password = form.data['username'], form.data['password']
        
        user = db.session.query(Users).filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('hello_world'))
        else:
            flash('Incorrect login or password')
            
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.SignUp()
    
    if request.method == 'POST' and form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        code = form.data['code']
        
        if code == 'TEST':
            db.session.add(Users(username, password))
            db.session.commit()
            user = db.session.query(Users).filter_by(username=username).first()
            login_user(user)
            return redirect(url_for('hello_world'))
        else:
            flash('Incorrect invite code')
            
    return render_template('signup.html', form=form)


@app.route('/submit', methods=['POST'])
def submit():
    username = request.headers.get('username', '')
    password = request.headers.get('password', '')
    data = request.headers.get('data', '{}')

    user = db.session.query(Users).filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        db.session.add(DataBit(username, data, datetime.now().timestamp()))
        db.session.commit()
        return 'Added!'
    else:
        return 'Bad credentials!'


@app.route('/plot', methods=['GET'])
@login_required
def plot():
    points = db.session.query(LabelPoint).filter_by(username=current_user.username).all()

    temp = {
        'data': [{
            'data': [],
            'label': None
        }],
        'labels': []
    }

    data = {}

    for point in points:
        if point.label not in data:
            data[point.label] = deepcopy(temp)
        data[point.label]['data'][0]['data'].append(point.y)
        data[point.label]['data'][0]['label'] = point.label
        data[point.label]['labels'].append(point.x)

    return data


@app.after_request
def redirect_to_login(response):
    if response.status_code == 401:
        return redirect(url_for('login'))

    return response
