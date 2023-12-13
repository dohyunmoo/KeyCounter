import os
import json

from datetime import datetime
from pprint import pprint

import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify
import subprocess

class DataAttr:
    def __init__(self, date_list):
        self.date_list = date_list
        self.data_length = len(self.date_list)

app = Flask(__name__)

cred = credentials.Certificate(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".secret"), "credentials.json"))
firebase_admin.initialize_app(cred)

@app.route("/retrieve/<index>")
@app.route("/retrieve/", defaults={"index": 0})
def retrieve(index):
    try:
        result = run_read(index)
        print(jsonify(result))
        return jsonify(result)
    except subprocess.CalledProcessError as e:
        return f"Error with msg: {e.output}"
    
def run_read(index=0):
    db = firestore.client()

    doc_ref = db.collection("KeyCounts").get() # receive date from js app 

    doc_ids = [doc.id for doc in doc_ref]

    date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in doc_ids]
    sorted_date_objects = sorted(date_objects, reverse=True)

    sorted_dates = [datetime.strftime(date, "%Y-%m-%d") for date in sorted_date_objects]

    data = DataAttr(sorted_dates)

    print("latest input:")
    pprint(data.date_list[int(index)])

    doc_snapshot = db.collection("KeyCounts").document(data.date_list[int(index)]).get()
    return json.dumps(doc_snapshot.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
