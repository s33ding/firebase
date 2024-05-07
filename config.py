import os 

prod = False

#if prod:
#    path_cred_firebase = os.environ.get("FIREBASE_PROD_CRED")
#else:
#    path_cred_firebase = os.environ.get("FIREBASE_DEV_CRED")

path_cred_firebase = os.environ.get("FIREBASE_DEV_CRED")
fb_db_url = "https://s33ding-default-rtdb.firebaseio.com/"
