'''
Created on May 31, 2018

@author: freeman
'''

'''
try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        treeAutomobili = Treeview(self)
        
        
        tv['columns'] = ('starttime', 'endtime', 'status', 'nesto', 'nesto1', 'nesto2')
        
        
        tv.column("#0", anchor="w")
        tv.column('starttime', anchor='center', width=100)
        tv.column('endtime', anchor='center', width=100)
        tv.column('status', anchor='center', width=100)
        
        tv.column('nesto', anchor='center', width=100)
        tv.column('nesto1', anchor='center', width=100)
        tv.column('nesto2', anchor='center', width=100)
        
       

        
        tv.heading("#0", text='Sources', anchor='w')
        tv.heading('starttime', text='Start Time')
        tv.heading('endtime', text='End Time')
        tv.heading('status', text='Status')
        
        tv.heading('nesto', text='Nesto')
        tv.heading('nesto1', text='Nesto2')
        tv.heading('nesto1', text='Nesto2')
        
        
        treeAutomobili["columns"] = ( "Oznaka", "Opis", "Duzina", "Sirina", "Visina", "Maksimalna brzina", "Godina proizvodnje",
                                           "Izlozbeni prostor", "Broj vrata", "Broj sedista", "Tip menjaca")
        
        treeAutomobili.column("Oznaka")
        treeAutomobili.column("Opis")
        treeAutomobili.column("Duzina")
        treeAutomobili.column("Sirina")
        treeAutomobili.column("Visina")
        treeAutomobili.column("Maksimalna brzina")
        treeAutomobili.column("Godina proizvodnje")
        treeAutomobili.column("Izlozbeni prostor")
        treeAutomobili.column("Broj vrata")
        treeAutomobili.column("Broj sedista")
        treeAutomobili.column("Tip menjaca")
        
        treeAutomobili.heading("Oznaka", text="Oznaka")
        treeAutomobili.heading("Opis", text="Opis")
        treeAutomobili.heading("Duzina", text="Duzina")
        treeAutomobili.heading("Sirina", text="Sirina")
        treeAutomobili.heading("Visina", text="Visina")
        treeAutomobili.heading("Maksimalna brzina", text="Maksimalna brzina")
        treeAutomobili.heading("Godina proizvodnje", text="Godina proizvodnje")
        treeAutomobili.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        treeAutomobili.heading("Broj vrata", text="Broj vrata")
        treeAutomobili.heading("Broj sedista", text="Broj sedista")
        treeAutomobili.heading("Tip menjaca", text="Tip menjaca")

        
        
        
        
        
        
        
        treeAutomobili.grid(sticky = (N,S,W,E))
        self.treeview = treeAutomobili
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
'''
  
'''      
import sys
from tkinter import *

# My frame for form
class simpleform_ap(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.grid()

    def initialize(self):
        # Dropdown Menu
        optionList = ["Yes","No"]
        self.dropVar=StringVar()
        self.dropVar.set(optionList[0]) # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *optionList,
                                    command=self.func)
        self.dropMenu1.grid(column=1,row=4)

    def func(self,value):
        print (value)


def create_form(argv):
    form = simpleform_ap(None)
    form.title('My form')
    form.mainloop()

if __name__ == "__main__":
    create_form(sys.argv)
    
'''
    
from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
var1.set(1)
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()