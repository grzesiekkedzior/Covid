import RestAllData as rd
import RestGlobalData as gd

# Show only one country
#rd.RestAllData('Poland').showData()


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
        self.list = rd.getAllCountries()
        self.combobox_choose_country = tk.ttk.Combobox(self.left_frame)
        self.combobox_choose_country['values'] = list(self.list)
        self.combobox_choose_country.grid(column=1, row=1)
        self.combobox_choose_country.set("Poland")

        #button to combobox
        self.button_choose_country = tk.Button(self.left_frame, text="ok", relief="groove")
        self.button_choose_country.grid(row=1, column=2, padx=5, pady=5, sticky='n')

        #middle
        g = gd.RestGlobalData()
        self.middle_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.middle_frame.grid(row=0, column=2, padx=5, pady=5, sticky='n')

        self.label = tk.Label(self.middle_frame, justify="left", borderwidth=2, relief="groove", font=("Helvetica", 16, "bold"))
        self.label.config(text="GLOBAL SUMMARY"'\n'
                          + "New confirmed - " + str(g.new_confirmed) + '\n'
                          + "Total confirmed - " + str(g.total_confirmed) + '\n'
                          + "New deaths - " + str(g.new_deaths) + '\n'
                          + "Total deaths - " + str(g.total_deaths) + '\n'
                          + "New recovered - " + str(g.new_recovered) + '\n'
                          + "Total recovered - " + str(g.total_recovered) + '\n'
                          + "Global population - 1.7 mld")
        self.label.pack()



        #right
        self.right_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.right_frame.grid(row=0, column=3, padx=5, pady=5, sticky='n')
        self.img = tk.PhotoImage(file="resources/covid-19.gif")
        self.label = tk.Label(self.right_frame, image=self.img)
        self.label.pack()



    def say_hi(self):
        print("hi there, everyone!")



root = tk.Tk()
app = Application(master=root)
app.mainloop()
