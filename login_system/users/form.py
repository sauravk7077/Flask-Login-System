from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField(label="username",validators=[DataRequired(),Length(min=4, max=5)])
    email = StringField(label="email", validators=[DataRequired(), Email()])
    submit = SubmitField(label="Submit")
