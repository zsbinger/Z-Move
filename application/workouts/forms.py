from flask_wtf import FlaskForm
from wtforms.widgets import html_params
from markupsafe import Markup
from wtforms import (StringField, BooleanField, IntegerField,
                     SelectField, TextField, TextAreaField,
                     DateField, SubmitField, Field)
from wtforms.validators import DataRequired


class ButtonWidget(object):
    """
    https://gist.github.com/doobeh/239b1e4586c7425e5114
    Renders a multi-line text area.
    `rows` and `cols` ought to be passed as keyword args when rendering.
    """
    input_type = "button"

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        return Markup('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
        )


class ButtonField(StringField):
    widget = ButtonWidget()


class WorkoutForm(FlaskForm):
    # name = StringField('Workout Name', validators=[DataRequired()])
    name = StringField('Workout Name')
    # add check to make sure that this is an integer
    num_rounds = IntegerField()
    scored_checkbox = BooleanField('Scored')

    # will eventually be a dictionary to keep track of each component
    # of the workout
    # workout_content = TextAreaField('Workout')
    exercise1 = StringField('Exercise')
    num_sets1 = IntegerField('Sets')
    num_reps1 = IntegerField('Reps')
    # add exercise drop down with list pulled from database

    add_section_button1 = ButtonField('Add Section', id='addSectionButton1')
    add_exercise_button1 = SubmitField('Add Exercise', id='addExerciseButton1')
    submit_workout_button = SubmitField(label='Submit Workout')
    save_workout_button = SubmitField(label='Save Workout')
    load_workout_button = SubmitField(label='Load Previous Workout')