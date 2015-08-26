from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    loginid = StringField('loginid', validators=[DataRequired()])
    logincode = PasswordField('logincode', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
