import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from application.database import Database


def create_app():
    # create and configure the app
    app = Flask(__name__)
    Database.initialize()

    app.config['SECRET_KEY'] = 'bingers'

    @app.route("/")
    def index():
        return render_template("index.html")

    # register Blueprints (after defining db)
    from application.workouts.views import workouts_blueprint
    app.register_blueprint(workouts_blueprint, url_prefix='/workouts')

    from application.exercises.views import exercises_blueprint
    app.register_blueprint(exercises_blueprint, url_prefix='/exercises')

    return app