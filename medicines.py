import os.path
import json
import datetime


class Medicines:
    def __init__(self):
        # name: description, doses, status = True
        self.medicines = {}
        self.medicines_temp = {}
        self.medicines_new = {}
        self.now = datetime.date.today()
        self.day = datetime.date.weekday(self.now)

    # Check if data file exists
    def isFileExists(self):
        check = os.path.isfile("./classes/listOfMed.dat")
        if check is True:
            pass
        else:
            file = open("./classes/listOfMed.dat", "w")
            file.write("{}")
            file.close()

    # Reading data file
    def readFile(self):
        with open("./classes/listOfMed.dat", "r+") as outfile:
            self.medicines_temp = json.load(outfile)

    # Writing to a data file
    def writeFile(self, content):
        with open("./classes/listOfMed.dat", "w+") as outfile:
            json.dump(content, outfile)

    # Adding medicine to the file
    def addMedicine(self, name, description, doses, status=False, number=1):
        number = doses
        self.readFile()
        self.medicines[name] = [description, doses, status, number]
        check_name = name in self.medicines_temp.keys()

        if check_name:
            print("This medicine already exists")
            return

        elif not check_name:
            for key in self.medicines:
                print(key, "successfully added!")
                self.medicines_new = {**self.medicines_temp, **self.medicines}
                self.writeFile(self.medicines_new)

    # Removes medicine from the file
    def removeMedicine(self):
        self.readFile()
        self.listMedicines()
        j = 1
        id_val = input("Which medicine You would like to remove? Choose number from the list: ")
        id_val_int = int(id_val)
        if id_val_int > len(self.medicines_temp):
            print("Wrong value!")
            return
        else:
            for key in self.medicines_temp:
                if str(j) == id_val:
                    print(key, "deleted")
                    del self.medicines_temp[key]
                    self.writeFile(self.medicines_temp)
                    return
                j += 1

    # Lists all medicines
    def listMedicines(self):
        self.readFile()
        i = 1
        if len(self.medicines_temp) == 0:
            print("None")
        else:
            for key in self.medicines_temp:
                print(str(i) + ".", str(key) + ":", self.medicines_temp[key][0])
                i += 1

    # list daily status of medicines
    def checkDailyStatus(self):
        self.listMedicines()
        self.readFile()
        i = 1
        c = input("Choose which You would like to check: ")
        for key in self.medicines_temp:
            if str(i) == c:
                print(key, "was chosen.")
                print("Daily status is:")
                if self.medicines_temp[key][2]:
                    print("You took already Your daily dose.")
                else:
                    print("You need to take", self.medicines_temp[key][3], "more.")
                return
            i += 1

    # Change status of a medicine
    def changeDailyStatus(self):
        self.listMedicines()
        self.readFile()
        i = 1
        c = input("Choose which You would like to take: ")
        for key in self.medicines_temp:
            status_value = self.medicines_temp[key][3]
            if str(i) == c:
                print(key, "was taken.")
                self.medicines_temp[key][3] = status_value - 1
                if self.medicines_temp[key][3] == 0:
                    self.medicines_temp[key][2] = True
                print("Status changed")
                self.writeFile(self.medicines_temp)
                return
            i += 1

    # Resets value of taken medicines every day
    def resetDailyStatus(self):
        check = os.path.isfile("./classes/resetStat.dat")
        if check is True:
            pass
        else:
            file = open("./classes/resetStat.dat", "w")
            file.write(str(self.day))
            file.close()
            print("File created")

        resetFile = open("./classes/resetStat.dat", "r+")
        value = resetFile.read()
        resetFile.close()

        if value == str(self.day):
            pass
        else:
            self.readFile()
            for key in self.medicines_temp:
                status_value = self.medicines_temp[key][1]
                self.medicines_temp[key][3] = status_value
                self.medicines_temp[key][2] = False
            self.writeFile(self.medicines_temp)
            resetFile = open("./classes/resetStat.dat", "w+")
            resetFile.write(str(self.day))
            resetFile.close()
