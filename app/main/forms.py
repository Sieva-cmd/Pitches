from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Advertisement','Advertisement'),('Interview','Interview'),('Product','Product'),('Technology','Technology')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit Pitch')