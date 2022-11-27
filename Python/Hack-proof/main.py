from os.path import isfile
from json import load
choice = input("Do you have an account or do you need to create one? (L for Login, S for signup) ")

if choice.upper() == "L":
    userName = input("What is your username? ").capitalize()
    password = input(f"What is your password {userName}? ")
    if isfile(f"accounts/{userName}.json"):
        data = load(open(f"accounts/{userName}.json", "r"))
        information = []
        for value in data:
            information.append(data[value])
        savedUser, savedPassword = information
        if savedUser == userName and savedPassword == password:
            print("\nAccess Granted\n")
            print("The following information is highly classified: \n\n"+open("cool document.txt", "r").read()) 
        else:
            print("\nAccess Denied")
    else:
        print("Account details invalid. Account does not exist, please choose signup.")
elif choice.upper() == "S":
    userName = input("Please create a username: ")
    password = input(f"Please create a password {userName}: ")
    if isfile(f"accounts/{userName}.json"):
        file = open(f"accounts/{userName}.json", "w")
        file.write(" {\"username\":\""+userName+"\", \"password\":\""+password+"\"}")
        file.close()
    else:
        file = open(f"accounts/{userName}.json", "x")
        file.write(" {\"username\":\""+userName+"\", \"password\":\""+password+"\"}")
        file.close()