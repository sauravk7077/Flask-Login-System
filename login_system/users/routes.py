from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, flash;
from login_system.users.form import RegistrationForm

users = Blueprint('users', __name__)



@users.route('/register', methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("You have successfully logged in", "blue-info")
        return redirect(url_for('main.home'))
    return render_template('Register.html', title="Register", form=form)

