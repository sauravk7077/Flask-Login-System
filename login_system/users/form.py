from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, SubmitField, PasswordField

class RegistrationForm(FlaskForm):
    username = StringField(label="Username", \
        render_kw={"placeholder": "Enter your username"},validators=[DataRequired(),Length(min=4, max=5)])
    email = StringField(label="Email",\
        render_kw={"placeholder":"Enter your email"}, validators=[DataRequired(), Email()])
    password = PasswordField(label="Password",\
        render_kw={"placeholder":"Enter your password"}, validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password",\
        render_kw={"placeholder":"Enter your password again."}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Submit")
