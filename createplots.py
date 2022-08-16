# Cloned from my old menu

from util.user import User
from util.menu import MenuSelection
import json
import random # for random strings
import string # for random strings/get characters
import win32api

def implCTRLHandle():
    win32api.SetConsoleCtrlHandler(on_exit, True)

def on_exit(signal_type):
   print('caught signal:', str(signal_type))

def main():
    print("Welcome to the plot creator v3000")
    print("Input a menu selection")
    pos = 0

    for menuSelection in menu:
        print(str(pos + 1) + ": " + menuSelection.str())
        pos+=1

    ind = input("\n:")

    if(ind == "-1"):
        print("Cancelled.. . . . ..")
        return
    
    print("")
    menu[int(ind)-1].select()
    print("")

    return True

def create():
    print("Create user function:")

    name = input("Input user name: ")
    age = input("Input " + name + "'s age: ")
    initial_user = User(name, age)
    users.append(initial_user)

    while(True):
        comment = input("Input a comment or hit -1 to get to menu\n")
        if comment == "-1":
            break
        
        initial_user.comments.add(comment)
        
    print("Created user", initial_user.toStr())

    # test
    with open('data.dat', 'w') as outfile:
        data = []

        for user in users:
            data.append(user.toJSON())
        
        outfile.write(json.dumps(data, indent=4))

    print("Wrote ", initial_user.toJSON())

    return False

def list():
    for user in users:
        print(user.toStr())

    return False

def delete():
    print("Delete user function")
    pos = 0

    for user in users:
        print(str(pos) + ". " + user.toStr())

    index = input("Input the user index to delete")

    users.remove(users[index])

    return False

implCTRLHandle()
users = []

file = open("data/data.dat", "r")
data = json.loads(file.read())

for userStr in data:
    userDict = json.loads(userStr)
    users.append(User(userDict['name'], userDict['age']))

mainSelection = MenuSelection("", main)
createSelection = MenuSelection("Create plot!", create)
deleteSelection = MenuSelection("Delete plot!", delete)
listSelection = MenuSelection("List function!", list)
menu = [createSelection, deleteSelection, listSelection]

print("This is a test for plots, just to create some, I'm bored")

mainSelection.select()