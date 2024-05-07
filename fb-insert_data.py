import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db
from shared_func_firebase import *
from config import fb_db_url

app = init_app(fb_db_url)

data = {
    'Employee': {
        'emp1': {
            'name': 'Parwiz',
            'email': 'par@gmail.com',
            'age': 24
        },
        'emp2': {
            'name': 'John',
            'email': 'john@gmail.com',
            'age': 25
        }
    }
}

fb_insert_data(data=data, ref_name="/")
