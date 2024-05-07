import os
import firebase_admin as fa
from firebase_admin import credentials, auth
from shared_func_firebase import *

app = init_app()


email="teste2@gmail.com"

user = get_user_by_email(email)
