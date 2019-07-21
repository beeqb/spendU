from flask import Flask 
from flask_restful import Resource, reqparse
from  db_config import  DatabaseConfiguration
from bson.json_util import dumps
from bson.objectid import ObjectId   
import json

class Purchases(Resource):

    def __init__(self):
        database_onfiguration = DatabaseConfiguration()
        self.db = database_onfiguration.db

    def requestSetUp(self):
        parser = reqparse.RequestParser()
        list = ["currency","purchase_title","purchase_description", "amount", "location", "time"]
        for item in list:
              parser.add_argument(item)
        return parser.parse_args()

    def createEntry (self, currency, purchase_title, purchase_description, amount, location, time):
        return {
            "currency": currency,
            "purchase_title": purchase_title,
            "purchase_description": purchase_description,
            "amount": amount, 
            "location": location,
            "time": time
        }  

    def add_single_purchase(self, entry):
        self.db.insert_one(entry)

    def find_single_purchase_by_id(self, purchase_id):
        for entry in self.db.find({ "_id": ObjectId(purchase_id)}):
            return dumps(entry)

    def delete_single_purchase(self, purchase_id):
        self.db.delete_one({ "_id": ObjectId(purchase_id)})

    def update_single_purchase(self, purchase_id, new_values):
        myquery = { "_id":  ObjectId(purchase_id)}
        newValues =  { "$set": newValues }
        self.db.update_one(myquery, newValues)

    def get_purchase_list(self):
        return dumps(self.db.find({}))
  
    def entryExists(self, purchase_id):
        for entry in self.db.find({ "_id": ObjectId(purchase_id)}):
            if dumps(entry) == "":
                return True
            return False