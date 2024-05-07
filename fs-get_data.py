import os   
import firebase_admin as fa
from firebase_admin import firestore
from shared_func_firebase import *

app = init_app(db_url=None)

dct = fs_get_data(
        collection_name="Employee"
        )
