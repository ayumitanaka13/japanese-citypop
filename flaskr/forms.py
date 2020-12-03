from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User

class LoginForm(Form):
    email = StringField('Mail:', validators=[DataRequired(), Email('Your email adress is not correct.')])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login:')

class RegisterForm(Form):
    email = StringField('Mail:', validators=[DataRequired(), Email()])
    username = StringField('Name:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired(), EqualTo('password_confirm', message='Your password is not correct.')])
    password_confirm = PasswordField('Password check:', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('Your email adress is already registered.')
