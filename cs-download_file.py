import os   
import firebase_admin as fa
from firebase_admin import firestore
from shared_func_firebase import *
import config 

app = init_app(bucket=config.bucket)

file_name = "files/firebase.png"
destination_path = "media/firebase.png"

cs_download_file(
        file_name = file_name, 
        destination_path = destination_path
        )
