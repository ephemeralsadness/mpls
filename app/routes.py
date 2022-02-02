from . import app, db
from app.models import Users
import app.forms as forms

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash


@app.route('/')
@login_required
def hello_world():
    return render_template('main.html')


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


@app.after_request
def redirect_to_login(response):
    if response.status_code == 401:
        return redirect(url_for('login'))

    return response