"""
Vitaminator Ver.1.2. - 16.12.17
Created by Martin Agnar Dahl
MAD Robot
Part of a Vitaminator project
******************************************
ver.1.2. 16.12.17
GUI added, main file changed, menu file removed, dictionary for vitamins reorganised
******************************************
Ver.1.1. 27.11.17
Change in functions: listMedicines and checkDailyStatus.
Code is now shorter and program is easier to follow.
******************************************
Ver.1.0. 26.11.17
First version of application. No special functionality, just a simple code.
"""


from tkinter import *
import datetime
from classes.medicines import Medicines

medicines = Medicines()

# check if file exists
medicines.isFileExists()

# reset values if a new day
medicines.resetDailyStatus()


class MedApp:

    def __init__(self, master):
        self.list_of_vitamins = []
        self.read_vit_list_from_file()
        self.check_if_items_in_list()

        self.now = datetime.date.today()
        self.now1 = self.now.strftime("%A, %d. %B %Y")

        self.main_menu = Frame(master)
        self.main_menu.pack()

        self.end_frame = Frame(master)
        self.end_frame.pack(side=BOTTOM)

        self.min_width_label = Label(self.main_menu, width=40, text=" ")
        self.min_width_label.grid(row=0, columnspan=2)

        self.welcome_label = Label(self.main_menu,
                                   text="Welcome to Vitaminator! \nThis program will help You remember "
                                        "\nto take Your vitamins.")
        self.welcome_label.grid(row=1, columnspan=2)

        self.date_label = Label(self.main_menu, text="\nToday is: " + str(self.now1))
        self.date_label.grid(row=3, columnspan=2)

        self.menu_label = Label(self.main_menu, text="\nMenu:\n")
        self.menu_label.grid(row=6, column=0)

        self.status_button = Button(self.main_menu, text="Check daily status", width=22, heigh=2,
                                    command=self.check_daily_status)
        self.status_button.grid(row=7, column=0)

        self.take_button = Button(self.main_menu, text="Take a vitamin", width=22, heigh=2, command=self.take_a_vit)
        self.take_button.grid(row=8, column=0)

        self.list_button = Button(self.main_menu, text="List of vitamins", width=22, heigh=2, command=self.list_of_vit)
        self.list_button.grid(row=9, column=0)

        self.add_button = Button(self.main_menu, text="Add new vitamin", width=22, heigh=2, command=self.add_a_vit)
        self.add_button.grid(row=10, column=0)

        self.remove_button = Button(self.main_menu, text="Remove vitamin", width=22, heigh=2,
                                    command=self.remove_vit_from_list)
        self.remove_button.grid(row=11, column=0)

        self.exit_button = Button(self.main_menu, text="Exit", width=22, heigh=2, command=self.quit)
        self.exit_button.grid(row=12, column=0)

        self.empty_end_line = Label(self.end_frame, text=" ", pady=5, padx=90)
        self.empty_end_line.pack()

        self.status_label = Label(self.main_menu, text="\nStatus:\n")
        self.status_label.grid(row=6, column=1)

        self.status_text = Text(self.main_menu, width=50, heigh=7)
        self.status_text.grid(row=10, rowspan=3, column=1)
        self.status_text.propagate(0)

        self.scrollbar = Scrollbar(self.status_text, command=self.status_text.yview, cursor="arrow")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # take button/label
        self.list_def = StringVar()
        self.list_def.set("Choose medicine from list")
        self.list_of_med = OptionMenu(self.main_menu, self.list_def, *self.list_of_vitamins)

        self.confirm_button = Button(self.main_menu, text="Take vitamin", width=22, heigh=2, command=self.confirm_input)

        self.confirm_label_text = StringVar()
        self.confirm_label_text.set("")
        self.confirm_label = Label(self.main_menu, textvariable=self.confirm_label_text)

        # remove button

        self.confirm_remove_button = Button(self.main_menu, text="Remove!", width=22, heigh=2,
                                            command=self.confirm_remove)
        self.confirm_remove_variable = StringVar()
        self.confirm_remove_variable.set("")
        self.confirm_remove_label = Label(self.main_menu, textvariable=self.confirm_remove_variable)

        # Add medicine
        self.medicine_name_variable = StringVar()
        self.medicine_name = Entry(self.main_menu, textvariable=self.medicine_name_variable, width=25)
        self.label_name = Label(self.main_menu, text="Name:")
        self.medicine_dose_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.medicine_dose_variable = StringVar()
        self.medicine_dose_variable.set(self.medicine_dose_list[0])
        self.medicine_dose = OptionMenu(self.main_menu, self.medicine_dose_variable, *self.medicine_dose_list)
        self.label_dose = Label(self.main_menu, text="Daily dose:")
        self.add_medicine_button = Button(self.main_menu, text="Add vitamin", width=22, heigh=1,
                                          command=self.confirm_add)

    # GUI functions
    def check_daily_status(self):
        self.clean_text_box()
        self.read_vit_list_from_file()

        for key in medicines.medicines_temp:
            status = medicines.medicines_temp[key][2]
            if status > 0:
                self.status_text.insert(INSERT, "You need to take " + str(medicines.medicines_temp[key][2])+" of " +
                                        str(key)+"\n")

            else:
                self.status_text.insert(INSERT, "You took Your daily dose of " + str(key) + "\n")

    def add_a_vit(self):
        self.clean_text_box()
        self.label_name.grid(row=7, column=1, sticky=W, padx=60)
        self.medicine_name.grid(row=7, column=1)
        self.label_dose.grid(row=8, column=1, sticky=W, padx=60)
        self.medicine_dose.grid(row=8, column=1)
        self.add_medicine_button.grid(row=9, column=1)

    def confirm_add(self):
        self.read_vit_list_from_file()
        medicines_temp = self.list_of_vitamins

        name = self.medicine_name.get()
        doses = int(self.medicine_dose_variable.get())
        status = True
        number = doses

        v = dict(self.list_of_vitamins)
        check_name = name in v.keys()
        if check_name:
            self.status_text.delete(1.0, END)
            self.status_text.insert(INSERT, "This medicine already exists")

        elif not check_name:
            for key in self.list_of_vitamins:
                self.list_of_vitamins[name] = [doses, status, number]
                medicines_new = {**medicines_temp, **self.list_of_vitamins}
                medicines.writeFile(medicines_new)
                self.status_text.delete(1.0, END)
                self.status_text.insert(INSERT, str(name) + " successfully added!")
                self.update_option_menu_after_add()
                break

    def take_a_vit(self):
        self.clean_text_box()

        self.list_of_med.grid(row=7, column=1)
        self.confirm_button.grid(row=8, column=1)

    def list_of_vit(self):
        self.clean_text_box()
        self.read_vit_list_from_file()
        i = 1
        if len(medicines.medicines_temp) == 0:
            self.status_text.insert(INSERT, "None")
        else:
            for key in medicines.medicines_temp:
                self.status_text.insert(INSERT, str(key) + "\n")
                i += 1

    def confirm_input(self):
        self.read_vit_list_from_file()

        for key in self.list_of_vitamins:
            if key == self.list_def.get():
                status_value = self.list_of_vitamins[key][2]
                if status_value is 0:
                    self.confirm_label_text.set("You took all " + str(self.list_def.get()) + " for today.")
                    self.list_of_vitamins[key][1] = True
                    medicines.writeFile(self.list_of_vitamins)

                elif status_value < 0:
                    self.list_of_vitamins[key][2] = 0
                    self.list_of_vitamins[key][1] = True
                    medicines.writeFile(self.list_of_vitamins)
                    self.confirm_label_text.set("You took all " + str(self.list_def.get()) + " for today.")

                else:
                    self.list_of_vitamins[key][2] = status_value - 1
                    if self.list_of_vitamins[key][2] is 0:
                        self.list_of_vitamins[key][1] = True
                    medicines.writeFile(self.list_of_vitamins)
                    self.confirm_label_text.set("You took one " + str(self.list_def.get()))

        self.confirm_label.grid(row=9, column=1)

    def clean_text_box(self):
        self.status_text.delete(1.0, END)
        self.confirm_label.grid_forget()
        self.list_of_med.grid_forget()
        self.confirm_button.grid_forget()

        self.confirm_remove_button.grid_forget()
        self.confirm_remove_label.grid_forget()
        self.add_medicine_button.grid_forget()
        self.label_dose.grid_forget()
        self.label_name.grid_forget()
        self.medicine_dose.grid_forget()
        self.medicine_name.grid_forget()

    def read_vit_list_from_file(self):
        medicines.readFile()
        self.list_of_vitamins = medicines.medicines_temp

    def remove_vit_from_list(self):
        self.clean_text_box()

        self.list_of_med.grid(row=7, column=1)
        self.confirm_remove_button.grid(row=8, column=1)

    def confirm_remove(self):
        self.read_vit_list_from_file()
        for key in self.list_of_vitamins:
            if key == self.list_def.get():
                del self.list_of_vitamins[key]
                medicines.writeFile(self.list_of_vitamins)
                self.confirm_remove_variable.set(str(self.list_def.get())
                                                   + " is now removed from the list")
                self.update_option_menu_after_remove()
                self.check_if_items_in_list()
                break

    def update_option_menu_after_remove(self):
        self.check_if_items_in_list()
        m = self.list_of_med.children['menu']
        m.delete(0, END)
        newvalues = list(self.list_of_vitamins)
        for val in newvalues:
            m.add_command(label=val, command=lambda v=self.list_def, l=val: v.set(l))
        self.list_def.set(newvalues[0])

        self.confirm_remove_label.grid(row=9, column=1)

    def update_option_menu_after_add(self):
        self.check_if_items_in_list()
        m = self.list_of_med.children['menu']
        m.delete(0, END)
        newvalues = list(self.list_of_vitamins)
        for val in newvalues:
            m.add_command(label=val, command=lambda v=self.list_def, l=val: v.set(l))
        self.list_def.set(newvalues[0])

    def check_if_items_in_list(self):
        self.read_vit_list_from_file()
        if len(self.list_of_vitamins) is 0:
            self.list_of_vitamins = {"None":[0,True,0]}

    def quit(self):
        main_window.destroy()


# main window setup
main_window = Tk()
main_window.title("Vitaminator by MAD Robot")
main_window.geometry("640x480+200+50")

app = MedApp(main_window)

main_window.mainloop()
