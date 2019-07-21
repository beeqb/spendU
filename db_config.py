from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from string_provider import StringProvider
import datetime
import logging

DB_NAME = "spending_database"
COLLECTION_NAME = "spending_record"
mongo_string = StringProvider.mongo_string
client = MongoClient(mongo_string)

class DatabaseConfiguration:

    def __init__(self):
        self.db = self.get_database_collection()

    def create_database(client):
        list = client.list_database_names()
        if DB_NAME not in list:
            db = client[DB_NAME]
            spending_record = db[COLLECTION_NAME]
    logging.info("Database ready. Collection ready.")

    try:
        create_database(client)

    except ConnectionFailure:
        print("Server not available")

    def get_database_collection(self):
        db = client[DB_NAME]
        return db[COLLECTION_NAME]
         

