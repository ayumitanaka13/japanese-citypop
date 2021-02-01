from flask_wtf import FlaskForm
from wtforms.form import Form
from wtforms.fields import (
    StringField, FileField, PasswordField,
    SubmitField, HiddenField, TextAreaField
)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User, LikeAlbum



class LoginForm(FlaskForm):
    email = StringField(
        'Mail', validators=[DataRequired(), Email('Your email adress is not correct.')]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    submit = SubmitField('Login')



class RegisterForm(FlaskForm):
    email = StringField(
        'Mail', validators=[DataRequired(), Email()]
    )
    username = StringField(
        'Name', validators=[DataRequired()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), EqualTo('password_confirm', message='Your password is not correct.')]
    )
    password_confirm = PasswordField(
        'Password again', validators=[DataRequired()]
    )
    submit = SubmitField('Sign up')

    def validate_email(self, field):
        if User.select_user_by_email(field.data):
            raise ValidationError('Your email adress is already registered.')



class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        'Password',
        validators=[DataRequired(), EqualTo('confirm_password', message='Your password is not correct.')]
    )
    confirm_password = PasswordField(
        'Password again', validators=[DataRequired()]
    )
    submit = SubmitField('Update your password')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('Password should be more than 8 characters.')



class ForgotPasswordForm(FlaskForm):
    email = StringField('Mail: ', validators=[DataRequired(), Email()])
    submit = SubmitField('Set New Password')

    def validate_email(self, field):
        if not User.select_user_by_email(field.data):
            raise ValidationError('This email address does not exsist.')



class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        'Password',
        validators=[DataRequired(), EqualTo('confirm_password', message='Your password is not correct.')]
    )
    confirm_password = PasswordField(
        'Password again', validators=[DataRequired()]
    )
    submit = SubmitField('Password Update')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('Password should be more than 8 characters.')



class UserForm(FlaskForm):
    picture_path = FileField('Upload your icon')
    submit = SubmitField('Submit')



class SearchForm(FlaskForm):
    keyword = StringField(
        '', validators=[DataRequired()]
    )
    submit = SubmitField('Search')



class LikeAlbumForm(FlaskForm):
    from_user_id = HiddenField()
    to_album_id = HiddenField()
    submit = SubmitField('♡ Like')



class LikeSongForm(FlaskForm):
    from_user_id = HiddenField()
    to_artist_id = HiddenField()
    submit = SubmitField('♡ Like')



class CommentForm(FlaskForm):
    to_artist_id = HiddenField()
    comment = TextAreaField()
    submit = SubmitField('Add Comment')