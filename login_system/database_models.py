from login_system import database, login_manager
from flask_user import SQLAlchemyAdapter, UserManager
from flask_login import UserMixin
from flask_security import RoleMixin
from wtforms.validators import ValidationError


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class UserRoles(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    user_id = database.Column(database.Integer(), database.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = database.Column(database.Integer(), database.ForeignKey('role.id', ondelete='CASCADE'))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    image_file = database.Column(database.String(20), nullable=False,
                           default="default.jpg")
    password = database.Column(database.String(60), nullable=False)
    # Relationships
    roles = database.relationship('Role', secondary='user_roles',
                backref=database.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'User(username= { self.username }, email= { self.email })'

class Role(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    name = database.Column(database.String(50), unique=True)
