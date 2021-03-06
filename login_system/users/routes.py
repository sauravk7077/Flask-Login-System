from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, flash, request;
from login_system.users.form import RegistrationForm, LoginForm, AccountForm, RoleForm
from login_system import flask_bcrypt, database
from login_system.database_models import User, Role
from login_system.users.utils import is_safe_url, isAdmin
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users', __name__)


@users.route('/register', methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data ,password = hashed_pwd)
        user.roles.append(Role.query.filter_by(name = 'member').first())
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

@users.route('/user_control', methods=['GET','POST'])
@login_required
def user_control():
    form = RoleForm()
    if isAdmin():
        print("Hey you are here")
        for user in User.query.all():
            form.username.choices.append(user.username)
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            role = Role.query.filter_by(name=form.name.data).first()
            user.roles.append(role)
            database.session.commit()
            return redirect(url_for('main.home'))
        return render_template('admin_page.html', title = "Admin", form=form)
    flash("You are not allowed to enter the page.", category='danger')
    return redirect(url_for('main.home'))

@users.route('/all_user', methods=['GET'])
@login_required
def all_users():
    if isAdmin():
        data = User.query.all()
        return render_template('all_user.html', data=data)
    flash("Access Denied", category="danger")
    return redirect(url_for('main.home'))