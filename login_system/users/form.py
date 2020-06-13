from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FileField
from flask_login import current_user
from login_system.database_models import User

class RegistrationForm(FlaskForm):
    username = StringField(label="Username", \
        render_kw={"placeholder": "Enter your username"},validators=[DataRequired(),Length(min=4, max=10)])
    email = StringField(label="Email",\
        render_kw={"placeholder":"Enter your email"}, validators=[DataRequired(), Email()])
    password = PasswordField(label="Password",\
        render_kw={"placeholder":"Enter your password"}, validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password",\
        render_kw={"placeholder":"Enter your password again."}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Submit")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already taken. Please choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is already taken. Please choose a different one.")


class LoginForm(FlaskForm):
    username = StringField(label="Username", \
        render_kw={"placeholder": "Enter your username"},validators=[DataRequired(),Length(min=4, max=10)])
    password = PasswordField(label="Password",\
        render_kw={"placeholder":"Enter your password"}, validators=[DataRequired(), Length(min=8)])
    remember = BooleanField(label="Remember")
    submit = SubmitField(label="Submit")


class AccountForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    save = SubmitField(label="Save")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This username is already takes. Please choose another one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This email is already takes. Please choose another one.")
    
