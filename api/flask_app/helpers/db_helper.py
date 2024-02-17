import os
import urllib.parse
from pymongo import MongoClient, ASCENDING
from ..constants.env_constants import stages
from settings import MONGO_PASSCODE, MONGO_HOST

stage = os.getenv('stage')

ASC_SORT_ORDER = ASCENDING

def get_database(db_name):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    passcode = MONGO_PASSCODE
    host = MONGO_HOST
    if (stage == stages.get('production')):
        CONNECTION_STRING = "MONGO CONNECTION STRING PROD: IMPORT FROM .ENV"
    elif stage == stages.get('staging'):
        CONNECTION_STRING = "MONGO CONNECTION STRING STAGE: IMPORT FROM .ENV"
    else:
        CONNECTION_STRING = "MONGO CONNECTION STRING OTHER (DEV/LOCAL): IMPORT FROM .ENV"

    mongo_password = urllib.parse.quote(f"{passcode}".encode("utf-8"))
    CONNECTION_STRING = CONNECTION_STRING.format(mongo_password, host, db_name)

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client


def insert_one(collection, insertObj):
    return collection.insert_one(insertObj)
