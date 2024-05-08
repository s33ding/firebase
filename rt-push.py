import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db
from shared_func_firebase import *
from config import rt_db_url
import sys

app = init_app(rt_db_url)

new_data = {"teste":[1,2,3]}
inst = rt_push(new_data, ref_name="teste")
