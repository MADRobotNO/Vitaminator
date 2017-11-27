"""
Vitaminator Ver.1.1. - 27.11.17
Created by Martin Agnar Dahl
MAD Robot
Part of a Vitaminator project
"""

"""
Ver.1.1. 27.11.17
Change in functions: listMedicines and checkDailyStatus.
Code is now shorter and program is easier to follow.
"""

"""
Ver.1.0. 26.11.17
First version of aplication. No special functionalities, just a simple code.
"""

from classes.medicines import Medicines
from classes.menu import Menu

running = True

menu = Menu()
medicines = Medicines()

# check if file exists
medicines.isFileExists()

# reset values if a new day
medicines.resetDailyStatus()

while running:
    menu.header()
    print("===============================================================")
    menu.printMenu()
    print("===============================================================")
    userChoice = input("Choose an action: ")
    userChoice = int(userChoice)

    if userChoice == 1:
        medicines.checkDailyStatus()

    elif userChoice == 2:
        medicines.changeDailyStatus()

    elif userChoice == 3:
        medicines.listMedicines()

    elif userChoice == 4:
        print("Adding a medicine...")
        name = input("Type a name of the medicine: ")
        description = input("Description of the medicine: ")
        doses = int(input("Daily dose (tab): "))
        medicines.addMedicine(name, description, doses)

    elif userChoice == 5:
        medicines.removeMedicine()
    elif userChoice == 6:
        quit()

