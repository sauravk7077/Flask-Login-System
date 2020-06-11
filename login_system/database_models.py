from login_system import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    image_file = database.Column(database.String(20), nullable=False,
                           default="default.jpg")
    password = database.Column(database.String(60), nullable=False)

    def __repr__(self):
        return f'User(username= { self.username }, email= { self.email })'