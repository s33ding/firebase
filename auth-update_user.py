import os
import firebase_admin as fa
from firebase_admin import credentials, auth
from shared_func_firebase import *

app = init_app()

lst = list_users(verbose=False)

for usr in lst:
    print(usr.email, "-", usr.uid )

uid = input("uid: ")

user = get_user_by_uid(uid)

if user:
    # Ask what to update
    print("\nSelect the attribute you want to update:")
    print("1. Email")
    print("2. Phone Number")
    print("3. Password")
    print("4. Account Status (Enable/Disable)")
    print("5. Display Name")
    choice = input("Enter your choice (1-5): ")

    kwargs = {}
    if choice == '1':
        kwargs['email'] = input("Enter new email: ")
    elif choice == '2':
        kwargs['phone_number'] = input("Enter new phone number: ")
    elif choice == '3':
        kwargs['password'] = input("Enter new password: ")
    elif choice == '4':
        action = input("Enter 'disable' to disable or 'enable' to enable the user: ").lower()
        kwargs['disabled'] = True if action == 'disable' else False
    elif choice == '5':
        kwargs['display_name'] = input("Enter new display name: ")
    
    # Update the user
    update_user(uid=uid, **kwargs)
else:
    print("No user found with the UID provided.")
