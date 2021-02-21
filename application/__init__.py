import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = MongoClient(
    os.environ.get('MONGODB_URI')
    # serverSelectionTimeoutMS=3000  # 3 seconds
)
db = client.workouttracker

app.config['SECRET_KEY'] = 'bingers'


# register Blueprints (after defining db)
from application.workouts.views import workouts_blueprint

app.register_blueprint(workouts_blueprint, url_prefix='/workouts')
