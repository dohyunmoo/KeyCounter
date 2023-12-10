import os
import json

from datetime import datetime
from pprint import pprint

import firebase_admin
from firebase_admin import credentials, firestore

class DataAttr:
    def __init__(self, date_list):
        self.date_list = date_list
        self.data_length = len(self.date_list)

def run_read(index=0):
    cred = credentials.Certificate(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".secret"), "credentials.json"))
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    doc_ref = db.collection("KeyCounts").get() # receive date from js app 

    doc_ids = [doc.id for doc in doc_ref]

    date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in doc_ids]
    sorted_date_objects = sorted(date_objects, reverse=True)

    sorted_dates = [datetime.strftime(date, "%Y-%m-%d") for date in sorted_date_objects]

    data = DataAttr(sorted_dates)

    print("latest input:")
    pprint(data.date_list[index])

    doc_snapshot = db.collection("KeyCounts").document(data.date_list[index]).get()
    return json.dumps(doc_snapshot.to_dict())

if __name__ == "__main__":
    result = run_read()

    pprint(result)
