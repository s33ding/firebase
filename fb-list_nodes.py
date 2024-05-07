import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db
from shared_func_firebase import *
from config import fb_db_url
import sys

app = init_app(fb_db_url)
lst = fb_list_nodes()
