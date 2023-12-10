import os

import python_src.counter as counter
import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint

def run():
    cred = credentials.Certificate(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".secret"), "credentials.json"))
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    doc_ref = db.collection("KeyCounts").document(counter.get_current_day())

    result = counter.main()

    try:
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            data = doc_snapshot.to_dict()
            updated = counter.update(target=data, sample=result)

            doc_ref.set(updated)
        else:
            doc_ref.set({"KeyPresses": result})
    except Exception as e:
        print(f"failure with {e}")
