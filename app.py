from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import requests
import subprocess

app = Flask(__name__)

def update_db(db_file):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://docs.google.com/spreadsheets/d/1HUL5jcpy5-nsw_b9TFPVhXsGkZ9NiiwfT0Wc5JG-jmY/edit?usp=sharing',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
        }
    resp = requests.get("""https://docs.google.com/spreadsheets/export?
        format=csv&
        id=1HUL5jcpy5-nsw_b9TFPVhXsGkZ9NiiwfT0Wc5JG-jmY&gid=444587373""", headers=headers)
    if int(resp.status_code) == 200:
        f = open(db_file+'.csv','w+')
        f.write(resp.content)
        f.close()
    else:
        print("Error fetching updated database")


@app.route("/refresh")
def refresh():
    update_db('new_flood_stat')
    return render_template("index.html")

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
reviews = collection.find(projection=FIELDS)

@app.route("/floodstat/review")
def floodstat_reivew():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    reviews = collection.find(projection=FIELDS)
    json_reviews = []
    for r in reviews:
        json_reviews.append(r)
    json_reviews = json.dumps(json_reviews, default=json_util.default)
    connection.close()
    return json_reviews

if __name__ == "__main__":
    update_db('flood_stat')
    app.run(host='0.0.0.0',port=5000,debug=True)
