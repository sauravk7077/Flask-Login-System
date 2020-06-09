from flask.blueprints import Blueprint
from flask import render_template;
from login_system.users.form import RegistrationForm

users = Blueprint('users', __name__)



@users.route('/register')
def register():
    form = RegistrationForm()
    return render_template('Register.html', title="Register", form=form)

