from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from application.database import Database
# from application.models import Workout
from application.workouts.forms import WorkoutForm
import datetime

workouts_blueprint = Blueprint('workouts', __name__,
                               template_folder='templates/')


@workouts_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = WorkoutForm()
    if form.validate_on_submit():
        flash('Your workout has been added.')
        session['workout_content'] = form.workout_content.data
        if request.method == "POST":
            # save to mongodb database
            name = form.name.data
            num_rounds = form.num_rounds.data
            workout_content = form.workout_content.data
            scored = form.scored_checkbox.data
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            # new_workout = Workout(name, num_rounds, workout_content, scored, formatted_date)
            Database.insert('workouts', {'name': name,
                                         'num_rounds': num_rounds,
                                         'scored': scored,
                                         'content': workout_content,
                                         'date': formatted_date})
        # placeholder - will eventually redirect somewhere else
        # that make sense
        return redirect(url_for('workouts.create'))

    return render_template('creation.html', form=form)


@workouts_blueprint.route("/view", methods=["GET"])
def view():
    workouts_with_date = [
        (workout["name"],
         workout["num_rounds"],
         workout["scored"],
         workout["content"],
         workout["date"],
         datetime.datetime.strptime(workout["date"], "%Y-%m-%d").strftime("%b %d")
         )
        for workout in Database.find_all('workouts')
    ]

    return render_template("recent.html", workouts=workouts_with_date)
