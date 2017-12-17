import datetime

class Menu:
    def __init__(self):
        self.menuList = ["Check daily status", "Take a medicine", "List of medicines", "Add a medicine",
                         "Remove a medicine", "Exit"]
        self.now = datetime.date.today()
        self.now1 = self.now.strftime("%A %d. %B %Y")

    def header(self):
        print("===============================================================")
        print("=                 Welcome to Vitaminator!                     =")
        print("=            This program will help You remember              =")
        print("=                  to take Your vitamins.                     =")
        print("===============================================================")
        print("              Today is:", self.now1)
        print("===============================================================")
        print("=                         Menu:                               =")

    def printMenu(self):
        i = 1
        for item in self.menuList:
            print(str(i) + ".", item)
            i += 1
