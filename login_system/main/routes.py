from flask.blueprints import Blueprint
from flask import render_template, flash
from login_system import database
from login_system.database_models import User, Role
from login_system import flask_bcrypt


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title="Home")