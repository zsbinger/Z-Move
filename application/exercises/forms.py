from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, IntegerField,
                     SelectField, TextField, TextAreaField,
                     DateField, SubmitField, FieldList)
from wtforms.validators import DataRequired
# from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

# images = UploadSet('images', IMAGES)


class ExerciseForm(FlaskForm):
    name = StringField('Exercise Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    # muscles = FieldList('Muscles')
    video_link = StringField('Video')
    # upload = FileField('image', validators=[
    #     FileRequired(),
    #     FileAllowed(images, 'Images only!')
    # ])
    # photo = FileField(validators=[FileRequired()])
    photo = FileField()

    add_exercise_button = SubmitField('Add Exercise')
