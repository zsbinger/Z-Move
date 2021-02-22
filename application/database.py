import os
from pymongo import MongoClient
from dotenv import load_dotenv


class Database(object):
    # loads environment variables from .env file
    # which contains our Mongo URI connection information
    load_dotenv()
    DATABASE = None

    @staticmethod
    def initialize():
        # establish connection MongoDB database (Mongo atlas)
        client = MongoClient(
            os.environ.get('MONGODB_URI')
            # serverSelectionTimeoutMS=3000  # 3 seconds
        )
        Database.DATABASE = client['workouttracker']
        print('Database connection established')

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find({})

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
