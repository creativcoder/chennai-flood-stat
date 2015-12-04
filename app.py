from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'floodstat'
COLLECTION_NAME = 'review'

FIELDS = {'Timestamp':True,
          'Area Name':True,
          'How Badly your area is affected?':True,
          'Type of your Residence':True,
          'How badly you are personally affected':True,
          'How was the Government\'s response':True,
          '_id':False
          }

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DBS_NAME][COLLECTION_NAME]
projects = collection.find(projection=FIELDS)

@app.route("/floodstat/review")
def floodstat_reivew():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


# for project in projects:
#     print project


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
