from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, SubmitField, PasswordField

class RegistrationForm(FlaskForm):
    username = StringField(label="Username", render_kw={"placeholder": "Enter your username"},validators=[DataRequired(),Length(min=4, max=5)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Submit")
