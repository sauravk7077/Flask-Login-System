from flask.blueprints import Blueprint
from flask import render_template, flash

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title="Home")