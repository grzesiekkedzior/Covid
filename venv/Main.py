import RestAllData as rd
import RestGlobalData as gd
from urllib.request import urlopen
from tkinter import messagebox as mb

import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        #left
        self.left_frame = tk.Frame(self,borderwidth=2, relief="groove")
        self.left_frame.grid(row=0, column=0, padx=5, pady=5, sticky='n')
        self.sep = ttk.Separator(self, orient=tk.VERTICAL)
        self.sep.grid(row=0, column=1, padx=5, pady=5, sticky='ns')

        #combobox
        self.load_all_countries()

        #button to combobox
        self.button_choose_country = tk.Button(self.left_frame, text="show", relief="groove", command=self.load_country)
        self.button_choose_country.grid(row=1, column=2, padx=5, pady=5, sticky='n')

        #middle
        self.global_information()

        #right
        self.show_covid_image()

    def load_all_countries(self):
        self.label2 = tk.Label(self.left_frame, justify="left", borderwidth=2,
                               font=("Helvetica", 12, "bold"))
        self.label2.config(text="Choose country")
        self.label2.grid(row=0, column=1, padx=5, pady=5, sticky='n')
        self.list = rd.getAllCountries()
        self.combobox_choose_country = tk.ttk.Combobox(self.left_frame)
        self.combobox_choose_country.grid_configure(padx=5,pady=5)
        self.combobox_choose_country['values'] = list(self.list)
        self.combobox_choose_country.grid(column=1, row=1)
        self.combobox_choose_country.set("Poland")

    def show_covid_image(self):
        self.right_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.right_frame.grid(row=0, column=3, padx=5, pady=5, sticky='n')
        self.img = tk.PhotoImage(file="resources/covid-19.gif")
        self.label = tk.Label(self.right_frame, image=self.img)
        self.label.pack()

    def global_information(self):
        self.middle_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.middle_frame.grid(row=0, column=2, padx=5, pady=5, sticky='n')
        g = gd.RestGlobalData()
        self.label = tk.Label(self.middle_frame, justify="left", padx=5, borderwidth=2, relief="groove",
                              font=("Helvetica", 16))
        self.label.config(text="GLOBAL SUMMARY"'\n'
                               + "New confirmed - " + str(g.new_confirmed) + '\n'
                               + "Total confirmed - " + str(g.total_confirmed) + '\n'
                               + "New deaths - " + str(g.new_deaths) + '\n'
                               + "Total deaths - " + str(g.total_deaths) + '\n'
                               + "New recovered - " + str(g.new_recovered) + '\n'
                               + "Total recovered - " + str(g.total_recovered) + '\n'
                               + "Global population - 7.6 mld")
        self.label.pack()

    def load_country(self):
        rd.RestAllData(self.combobox_choose_country.get()).showData()

def internet_on():
   try:
        response = urlopen('https://www.google.com/', timeout=5)
        return True
   except:
        return False


if internet_on():
    root = tk.Tk()
    root.title("COVID - 19")
    root.iconbitmap("resources/coronavirus.ico")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
else:
    message = tk.Tk()
    message.withdraw()
    mb.showerror("Internet connection!", "You are not connected to a Network")

