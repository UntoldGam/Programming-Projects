from os.path import isfile 
from json import dump
def newUser(data):
    # data = {"user": ..., "health": ...}
    if isfile(f"./users/{data.userName}"):
        file = open(f"./users/{data.userName}")
        file.write(dump(data))
        file.close()
    else:
        file = open(f"")