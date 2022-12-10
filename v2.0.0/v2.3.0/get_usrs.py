import os

# CREATES AN ARRAY WITH ALL USERS IN THE SYSTEM THAT ARE NOT DEFAULT 

global users
users = [] #define list to store every user 

def get_users():
    for i in os.scandir('c:\\Users'):
        if i.is_dir():
            users.append(i.name)

    #print(users)

    # Remove windows default users
    # dont know why it is unable to remove them all at 1st try so it needs 3 times 

    for i in users:
        if i in ['All Users', 'Default', 'Default User', 'defaultuser0', 'defaultuser00', 'Admin']:
            users.remove(i)
            #print(f)

    for i in users:
        if i in ['All Users', 'Default', 'Default User', 'defaultuser0', 'defaultuser00', 'Admin']:
            users.remove(i)
            #print(f)

    for i in users:
        if i in ['All Users', 'Default', 'Default User', 'defaultuser0', 'defaultuser00', 'Admin']:
            users.remove(i)
            #print(f)

    return users

