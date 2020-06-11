from flask import Flask
from login_system.conf import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def createApp(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)

    db.init_app(app)

    from login_system.users.routes import users
    from login_system.main.routes import main

    # Registers the blueprints
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app