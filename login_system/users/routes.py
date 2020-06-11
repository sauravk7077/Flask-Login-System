from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, flash;
from login_system.users.form import RegistrationForm, LoginForm
from login_system import flask_bcrypt, database
from login_system.database_models import User



users = Blueprint('users', __name__)


@users.route('/register', methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data ,password = hashed_pwd)
        database.session.add(user)
        database.session.commit()
        flash("You have successfully created your account.", "blue-info")
        return redirect(url_for('main.home'))
    return render_template('Register.html', title="Register", form=form)


@users.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and flask_bcrypt.check_password_hash(user.password, form.password.data):
            flash("You have successfully logged in", "green-success")
            return redirect(url_for('main.home'))
        flash("You have entered either incorrect username or password.", 'yellow-warning')
    return render_template('Login.html', form=form, title="Log in")