import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db
from shared_func_firebase import *
from config import fb_db_url
import sys

app = init_app(fb_db_url)

if len(sys.argv) > 1:
    ref_name = sys.argv[1]
else: 
    ref_name = input("ref name: ")

data = fb_get_data(ref_name)
