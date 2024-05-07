import os   
import firebase_admin as fa
from firebase_admin import firestore
from shared_func_firebase import *

app = init_app(db_url=None)

data = {
    'name':'Parwiz',
    'email':'par@gmail.com',
    'lname':'forogh',
    'age':24
}

fs_insert_data(
        data=data, 
        collection_name="Employee",
        document_name="empdoc1"
        )
