from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
from purchases import Purchases
import json

app = Flask(__name__)
api = Api(app)
purchases = Purchases()

@app.route('/purchases/all',  methods=['GET'])
def get_all_purchases():
    try:
        return purchases.get_purchase_list()
    except Exception as e:
            abort(e.code, str(e))
    return purchases.get_purchase_list()

@app.route('/purchases/<string:id>',  methods=['GET'])
def get_single_purchase(id):
    try:
        return purchases.find_single_purchase_by_id(id)
    except Exception as e:
        abort(e.code, str(e))

@app.route('/purchases/<string:item>',  methods=['POST'])
def add_single_purchase(item):
    try:
        args = purchases.requestSetUp()
        entry = purchase_set_up(args)
        purchases.add_single_purchase(entry)
        return "Item {} has been added".format(item), 200
    except Exception as e:
        abort(e.code, str(e))

@app.route('/purchases/<string:id>',  methods=['DELETE'])
def delete_single_purchase(id):
    try:
        purchases.delete_single_purchase(id)
    except Exception as e:
        abort(e.code, str(e))
    return "Item has been deleted", 200

def purchase_set_up(args):
     return purchases.createEntry(
         args["currency"], 
         args["purchase_title"], 
         args["purchase_description"], 
         args["amount"], 
         args["location"], 
         args["time"]
)
    
app.run(host='0.0.0.0', port= 8080, debug=True)