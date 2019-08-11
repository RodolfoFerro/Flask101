from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class AgeForm(Form):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])


def legal_or_not(age):
    return (age >= 18)
