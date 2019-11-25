from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired
class Pitch_Form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Write Pitch', validators=[DataRequired()])
    category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[DataRequired()])
    submit = SubmitField('Submit')
class Update_Profile(FlaskForm):
    bio = TextAreaField('Add something more about Yourself...', validators = [DataRequired()])
    submit = SubmitField('Submit')
class CommentsForm(FlaskForm):
    comment = TextAreaField('comment on the post',validators=[DataRequired()])
    submit = SubmitField('Add Comment')
    