import os
import firebase_admin as fa
from firebase_admin import credentials, auth
from shared_func_firebase import *
import sys

app = init_app()
if len(sys.argv)>1:
    if "@" in sys.argv[1] :
        email=sys.argv[1]
else:
    email=input("email:")

link = generate_password_reset_link(email)
