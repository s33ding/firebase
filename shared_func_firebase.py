import os
import firebase_admin as fa
from firebase_admin import credentials, auth, db, firestore
from config import path_cred_firebase

# Simulate the path to Firebase credentials
def get_cred():
    return credentials.Certificate(path_cred_firebase)

def init_app(db_url=None):
    cred = get_cred()
    if db_url is not None:
        app = fa.initialize_app(cred, {"databaseURL":db_url})
    else:
        app = fa.initialize_app(cred)
    print("Firebase Initialized with:", app.name)
    return app

def create_user(email=None, password=None, phone=None):
    if email is None:
        email = input("Enter email: ")
    if password is None:
        password = input("Enter password: ")
    if phone is None:
        phone = input("Enter phone number: ")

    user = auth.create_user(email=email, password=password, phone_number=phone)
    print(f"User created (user.uid): {user.uid}")
    return user

def update_user(uid, email=None, phone_number=None, email_verified=None, password=None, display_name=None, photo_url=None, disabled=None):

    user_data = {}

    if email is not None:
        user_data['email'] = email
    if phone_number is not None:
        user_data['phone_number'] = phone_number
    if email_verified is not None:
        user_data['email_verified'] = email_verified
    if password is not None:
        user_data['password'] = password
    if display_name is not None:
        user_data['display_name'] = display_name
    if photo_url is not None:
        user_data['photo_url'] = photo_url
    if disabled is not None:
        user_data['disabled'] = disabled

    user = auth.update_user(uid, **user_data)
    print('Successfully updated user: {0}'.format(user.uid))


def list_users(by="phone", verbose=True):
    page = auth.list_users()
    lst = []
    for user in page.users:
        lst.append(user)
        if by == "phone":
            user = get_user_by_phone(user.phone_number, verbose)
        if by == "email":
            user = get_user_by_email(user.phone_number, verbose)
    return lst

        

def get_user_by_phone(phone, verbose=True):
    user = auth.get_user_by_phone_number(phone)
    if verbose:
        display_user_info(user)
    return user

def get_user_by_email(email,verbose=True):
    user = auth.get_user_by_email(email)
    if verbose:
        display_user_info(user)
    return user

def fb_get_data(ref_name,verbose=True):
    ref = fa.db.reference(ref_name)
    data= ref.get()
    if verbose:
        print("data:",data)
    return data

def fb_list_nodes(ref_name="/",verbose=True, mylimit = 100):
    ref = db.reference(ref_name)
    top_nodes =  ref.order_by_key().limit_to_first(mylimit).get()
    lst = []
    for key, value in top_nodes.items():
        lst.append(key)
        if verbose:
            print(f"{key}")
    return lst


def fb_push(new_data, ref_name="/", verbose=True):
    try:
        ref = db.reference(ref_name)
        ref.push(new_data)
        print("pushed:")
        print(new_data)
    except Exception as e:
        print("failed!")
        print(e)


def display_user_info(user, verbose=True):

    lst_attributes = [
            'custom_claims',
            'disabled',
            'display_name',
            'email',
            'email_verified',
            'phone_number',
            'photo_url',
            'provider_id',
            'tenant_id',
            'tokens_valid_after_timestamp',
            'uid',
            ]

    for i,v in enumerate(lst_attributes): 
        res = eval(f"user.{v}")
        if verbose:
            print(f"{v}: {res}")
    if verbose:
        print("------------------")

def get_user_by_uid(uid,verbose=True):
    user = auth.get_user(uid)
    if verbose:
        display_user_info(user)
    return user

def generate_password_reset_link(email):
    link = auth.generate_password_reset_link(email)
    print("link:",link)
    return link

def fb_insert_data(data,ref_name):
    try:
        ref = fa.db.reference(ref_name)
        ref.set(data)
        print("inserted:")
        print(data)
    except Exception as e:
        print("failed!")
        print(e)


def fb_update_ref_child(data,ref_name, child_name):
    try:
        ref = fa.db.reference(ref_name)
        ref_child = ref.child(child_name)
        ref_child.update(data)
        print("updated:")
        print("ref:", ref_name) 
        print("ref_child:", child_name) 
        print("data:") 
        print(data)
    except Exception as e:
        print("failed!")
        print(e)

def fs_insert_data(data,collection_name, document_name):
    try:
        db=firestore.client()
        doc_ref = db.collection(collection_name).document(document_name)
        doc_ref.set(data)
        print("inserted:")
        print(data)
    except Exception as e:
        print("failed!")
        print(e)


def fs_get_data(collection_name, verbose=True):
    try:
        db = firestore.client()
        ref = db.collection(collection_name)
        docs = ref.stream()

        dct = {}
        for doc in docs:
            if verbose:
                print("{} => {} ".format(doc.id, doc.to_dict()))
                dct[doc.id] = doc.to_dict()
        return dct
    except Exception as e:
        print("failed!")
        print(e)

