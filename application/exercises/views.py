from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from application.database import Database
# from application.models import Workout
from application.workouts.forms import WorkoutForm
import datetime

exercises_blueprint = Blueprint('exercises', __name__,
                                template_folder='templates/')


@exercises_blueprint.route("/view", methods=["GET", "POST"])
def view():
    exercises = [
        (exercise["name"],
         exercise["description"]
         )
        for exercise in Database.find_all('exercises')
    ]

    return render_template("exercises.html", exercises=exercises)
