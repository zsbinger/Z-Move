from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, IntegerField,
                     SelectField, TextField, TextAreaField,
                     DateField, SubmitField, Field)
from wtforms.validators import DataRequired


# class ButtonField(Field):
#     widget = TextInput()
#
#     def _value(self):
#         if self.data:
#             return u', '.join(self.data)
#         else:
#             return u''
#
#     def process_formdata(self, valuelist):
#         if valuelist:
#             self.data = [x.strip() for x in valuelist[0].split(',')]
#         else:
#             self.data = []


class WorkoutForm(FlaskForm):
    # name = StringField('Workout Name', validators=[DataRequired()])
    name = StringField('Workout Name')
    # add check to make sure that this is an integer
    num_rounds = IntegerField()
    scored_checkbox = BooleanField('Scored')

    # will eventually be a dictionary to keep track of each component
    # of the workout
    workout_content = TextAreaField('Workout')
    # add exercise drop down with list pulled from database

    add_section_button = SubmitField('Add Section')
    add_exercise_button = SubmitField('Add Exercise')
    submit_workout_button = SubmitField(label='Submit Workout')
    save_workout_button = SubmitField(label='Save Workout')
    load_workout_button = SubmitField(label='Load Previous Workout')