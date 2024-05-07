import os
import firebase_admin as fa
from firebase_admin import credentials, auth
from shared_func_firebase import *

app = init_app()


phone="+5561981332353"
user = get_user_by_phone(phone)
