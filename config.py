import os 

prod = False

if prod:
    path_cred_firebase = os.environ.get("FIREBASE_PROD_CRED")
else:
    path_cred_firebase = os.environ.get("FIREBASE_DEV_CRED")

rt_db_url = "https://s33ding-default-rtdb.firebaseio.com/"
bucket = "gs://s33ding.appspot.com"
bucket = bucket.replace("gs://","")
