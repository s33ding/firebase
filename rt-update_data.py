import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db
from shared_func_firebase import *
from config import rt_db_url


app = init_app(rt_db_url)

ref_name = "bosses"
child_name = "boss1"

data = {
            'email': 'par@gmail.com',
            'age': 55
    }

rt_update_ref_child(
        data=data,
        ref_name=ref_name, 
        child_name=child_name
        )
