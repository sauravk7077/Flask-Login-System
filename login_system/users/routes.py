from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, flash, request;
from login_system.users.form import RegistrationForm, LoginForm, AccountForm
from login_system import flask_bcrypt, database
from login_system.database_models import User, Role
from login_system.users.utils import is_safe_url
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users', __name__)


@users.route('/register', methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data ,password = hashed_pwd)
        database.session.add(user)
        database.session.commit()
        flash("You have successfully created your account.", "success")
        return redirect(url_for('users.login'))
    return render_template('Register.html', title="Register", form=form)


@users.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and flask_bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You have successfully logged in!", "success")
            next = request.args.get('next')
            if next:
                if not is_safe_url(next):
                    return flask.abort(400)
                else:
                    return redirect(next)
            return redirect(url_for('main.home'))
        flash("You have entered either incorrect username or password.", 'yellow-warning')
    return render_template('Login.html', form=form, title="Log in")


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        database.session.commit()
        flash('Your account details has been updated', 'info')
        return redirect(url_for('main.home'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title="Account", form=form)

@users.route('/user_control')
@login_required
def user_control():
    if current_user.roles.id:
        return redirect(url_for('main.home'))
    return render_template('admin_page.html', title = "Admin")