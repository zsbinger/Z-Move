import os
import datetime
from flask import Flask, render_template, request
# request is a value that has something inside it whenever
# we are in a function responding to a request (made by the browser)
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    # creates new Flask app and object with a unique name
    app = Flask(__name__)

    client = MongoClient(
        os.environ.get('MONGODB_URI')
        # serverSelectionTimeoutMS=3000  # 3 seconds
    )
    app.db = client.workouttracker

    @app.route("/", methods=["GET", "POST"])
    def home():
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
