from flask import Flask
from login_system.conf import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager


database = SQLAlchemy()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
sql_alchemy_adapter  = None
user_manager = None


def createApp(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)

    database.init_app(app)
    flask_bcrypt.init_app(app)
    login_manager.init_app(app)

    from login_system.users.routes import users
    from login_system.main.routes import main

    # Registers the blueprints
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app

