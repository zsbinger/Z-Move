from flask import render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, IntegerField,
                     SelectField, TextField, TextAreaField,
                     DateField, SubmitField)
from wtforms.validators import DataRequired

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
    load_workout_button = SubmitField(label='Load Previous Workout')