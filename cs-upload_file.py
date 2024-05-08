import os   
import firebase_admin as fa
from firebase_admin import firestore
from shared_func_firebase import *
import config 

app = init_app(bucket=config.bucket)

file_path = "media/firebase.png"
destination_path = "files/firebase.png"

cs_upload_file(file_path, destination_path)
