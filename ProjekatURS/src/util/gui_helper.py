'''
Created on May 31, 2018

@author: freeman
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
        
        '''
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
        
        '''
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