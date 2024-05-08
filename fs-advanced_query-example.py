import os   
import firebase_admin as fa
from firebase_admin import firestore
from shared_func_firebase import *
from google.cloud.firestore_v1.base_query import FieldFilter

app = init_app(db_url=None)

db = firestore.client()

age_threshold = 20

query = db.collection('Employee').where(filter=FieldFilter("age", ">", age_threshold))

results = query.get()

for doc in results:
    print(f" Document ID : {doc.id}")
    print(f" Name : {doc.get('name')}")
    print(f" Age : {doc.get('age')}")
    print(f" Email : {doc.get('email')}")

