# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Puppy:")
    submit = SubmitField("Add puppy")

class DelForm(FlaskForm):
    id = IntegerField("ID No. of puppy to be remove: ")
    submit = SubmitField("Remove puppy")

class AddOwner(FlaskForm):
    name = StringField("Name of Owner:")
    puppy_id = IntegerField("ID No. of puppy: ")
    submit = SubmitField("Add owner")
