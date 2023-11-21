from datetime import datetime
import os

from bson.json_util import dumps
from flask import Flask, Response, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def note_list():
    notes = mongo.cx.get_database('hsa5').get_collection('notes').find()
    return Response(dumps(list(notes)), headers={'Content-Type': 'application/json'})

@app.route('/', methods=['POST'])
def note_create():
    data = request.get_json()
    data['created_at'] = datetime.now()
    instance = mongo.cx.get_database('hsa5').get_collection('notes').insert_one(data)
    return jsonify({'_id': str(instance.inserted_id)})

@app.route('/', methods=['DELETE'])
def note_erase():
    mongo.cx.get_database('hsa5').get_collection('notes').delete_many({})
    return Response(dumps({}), status=204, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True, threaded=True)
