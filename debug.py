import pickle, os
from classes import *

atm = None
admin = None


if os.path.exists("atm.pkl"):
    atm = pickle.load(open("atm.pkl", "rb"))
    admin = atm.admins["admin"]
else:
    atm = ATM()
    admin = Admin("admin",1234)
    atm.admins[admin.name] = admin




q = 1
while True:
    print("Welcome to DIL Bank")
    q = input("Press 1 to continue 0 to exit")

    if q == "0":
        pickle.dump(atm, open("atm.pkl", "wb"))
        print("Thank you for using DIL Bank")
        break
    user = input("Enter user name : ")
    password = input("Enter your password : ")

    
    cmd = ""
    
    if user in atm.admins.keys():

        if atm.admins[user].pin != int(password):
            print("Wrong Password!")
            continue
        admin = atm.admins[user]
        print("Enter your command")
        while cmd!= 0:
            cmd = input(f"{admin.name}(Admin)> ")
            cmd = handle_admin_command(cmd,atm)

    elif user in atm.users.keys():
        if atm.users[user].pin != int(password):
            print("Wrong Password!")
            continue

        user = atm.users[user]

        print("Enter your command")
        while cmd!= 0:
            cmd = input(f"{user.name}> ")
            cmd = handle_user_command(cmd,atm, user)
    
    else:
        print(f"User Not Found {user}!")
       








