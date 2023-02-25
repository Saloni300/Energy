from flask import Flask
from loguru import logger
from pymongo import MongoClient
from pymongo.collection import Collection


CONNECTION_STRING = "mongodb://database"
DB_NAME = 'energy'
COLLECTION_NAME = 'user-consumption'

app = Flask(__name__)

def get_collection() -> Collection:
    client = MongoClient(CONNECTION_STRING)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

@app.route('/', methods=['GET'])
def get():
    """
    Retrieve list of user-consumption records
    """
    collection = get_collection()
    # query = {}
    # projection = {'_id': 0, '': 1, 'event_name': 1, 'status': 1}
    response = collection.find({}, {}).limit(1)[0]
    response['_id'] = str(response['_id'])
    logger.debug(response)
    return response
