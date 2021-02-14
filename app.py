__author__ = 'zsbinger'

import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
# request is a value that has something inside it whenever
# we are in a function responding to a request (made by the browser)
from pymongo import MongoClient
from dotenv import load_dotenv

from forms import WorkoutForm

load_dotenv()

def create_app():
    # creates new Flask app and object with a unique name
    app = Flask(__name__)

    client = MongoClient(
        os.environ.get('MONGODB_URI')
        # serverSelectionTimeoutMS=3000  # 3 seconds
    )
    app.db = client.workouttracker

    app.config['SECRET_KEY'] = 'bingers'

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/recent", methods=["GET"])
    def recent():

        workouts_with_date = [
            (workout["content"],
             workout["date"],
             datetime.datetime.strptime(workout["date"], "%Y-%m-%d").strftime("%b %d")
             )
            for workout in app.db.workouts.find({})
        ]

        return render_template("recent.html", workouts=workouts_with_date)

    @app.route("/creation", methods=["GET", "POST"])
    def creation():
        form = WorkoutForm()
        if form.validate_on_submit():
            flash('Your workout has been added.')
            session['workout_content'] = form.workout_content.data
            if request.method == "POST":
                # save to mongodb database
                workout_content = form.workout_content.data
                formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
                app.db.workouts.insert({"content": workout_content, "date": formatted_date})

            return redirect(url_for('creation'))

        return render_template("creation.html", form=form)

    @app.route("/exercises")
    def exercises():
        return render_template("exercises.html")

    @app.route("/<user>/home", methods=["GET", "POST"])
    def user_home():
        if request.method == "POST":
            entry_content = request.form.get("workout")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.workouts.insert({"content": entry_content, "date": formatted_date})

        workouts_with_date = [
            (workout["content"],
             workout["date"],
             datetime.datetime.strptime(workout["date"], "%Y-%m-%d").strftime("%b %d")
             )
            for workout in app.db.workouts.find({})
        ]

        return render_template("home.html", workouts=workouts_with_date)

    return app
