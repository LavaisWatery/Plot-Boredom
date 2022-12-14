# Cloned from my old menu

from util.plot import Plot
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
    print("Create plot function:")

    name = input("Input plot name: ")
    initial_plot = Plot(name)
    plots.append(initial_plot)

    while(True):
        comment = input("Input a plot coord (0,0) or hit -1 to get to menu\n")
       
        if comment == "-1":
            break
        
        plotSplit = comment.split(",")
        if len(plotSplit) >= 2:
            plotX = int(plotSplit[0])
            plotY = int(plotSplit[1])
        else:
            plotX = len(initial_plot.plotX) + 1
            plotY = plotSplit[0]

        initial_plot.plotX.append(plotX)
        initial_plot.plotY.append(plotY)
        
    print("Created plot ", initial_plot.toStr())

    # test
    with open('data/data.dat', 'w') as outfile:
        data = []

        for plot in plots:
            data.append(plot.toJSON())
        
        outfile.write(json.dumps(data, indent=4))

    print("Wrote ", initial_plot.toJSON())

    return False

def list():
    for plot in plots:
        print(plot.toStr())

    return False

def delete():
    print("Delete plot function")
    pos = 0

    for plot in plots:
        print(str(pos) + ". " + plot.toStr())

    index = input("Input the plot index to delete")

    plots.remove(plots[index])

    return False

implCTRLHandle()
plots = []

file = open("data/data.dat", "r")
data = json.loads(file.read())

for plotStr in data:
    plotDict = json.loads(plotStr)
    plot = Plot(plotDict['name'])
    data = {
        'name' : plotDict['name'], # I could do this better lol
        'plotX' : plotDict['plotX'],
        'plotY' : plotDict['plotY']
    }
    plot.data = data

    plots.append(plot)

mainSelection = MenuSelection("", main)
createSelection = MenuSelection("Create plot!", create)
deleteSelection = MenuSelection("Delete plot!", delete)
listSelection = MenuSelection("List function!", list)
menu = [createSelection, deleteSelection, listSelection]

print("This is a test for plots, just to create some, I'm bored")

mainSelection.select()