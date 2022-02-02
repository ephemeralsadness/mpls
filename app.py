from flask import Flask, request, redirect, url_for, flash, render_template

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import LoginManager, login_required, login_user, logout_user

from flask_sqlalchemy import SQLAlchemy


import forms


app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)


import models

@login_manager.user_loader
def load_user(id):
    return models.Users.query.filter_by(id=id).first()

@app.route('/')
@login_required
def hello_world():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        username, password = form.data['username'], form.data['password']
        
        user = db.session.query('users').filter_by(username=username).first()
        print(user.password)
        if user and check_password_hash(user.password, password):
            login_user(user)
            redirect(url_for('hello_world'))
        else:
            flash('Incorrect login or password')
            
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup')
def signup():
    ...


@app.after_request
def redirect_to_login(response):
    if response.status_code == 401:
        return redirect(url_for('login'))

    return response


if __name__ == '__main__':
    app.run(debug=True)
