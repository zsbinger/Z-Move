from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from application.database import Database
from application.exercises.forms import ExerciseForm
import datetime

exercises_blueprint = Blueprint('exercises', __name__,
                                template_folder='templates/')


@exercises_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = ExerciseForm()
    if form.validate_on_submit():
        flash('Your workout has been added.')
        session['exercise_name'] = form.name.data
        session['exercise_description'] = form.description.data
        if request.method == "POST":
            # save to mongodb database
            name = form.name.data
            description = form.description.data
            # muscles = form.muscles.data
            video_link = form.video_link.data
            images = form.photo.data
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            Database.insert('exercises', {'name': name,
                                          'description': description,
                                          # 'muscles': muscles,
                                          'video_link': video_link,
                                          'images': images,
                                          'date': formatted_date})
        return redirect(url_for('exercises.add'))

    return render_template('add.html', form=form)


@exercises_blueprint.route("/view", methods=["GET", "POST"])
def view():
    exercises = [
        (exercise["name"],
         exercise["description"]
         )
        for exercise in Database.find_all('exercises')
    ]

    return render_template("view.html", exercises=exercises)
