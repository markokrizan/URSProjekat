'''
Modul koji sadrzi klasu koja opisuje view koji prikazuje informacije o objektu klase Dzip.

@author: Aleksandar Rancic
'''

from tkinter import *
from tkinter import ttk

from controller.prostori import prostorIzOznake
from model.singleton import Projekat
import tkinter as tk
#from view.detaljiProstori import DetaljiProstor
from view.gui_utils import Centriraj
from tkinter import messagebox
from controller.dzipovi import dzipIzOznake
import view.detaljiProstori




class DetaljiDzipovi(tk.Tk):
    '''
    Klasa DetaljiDzipovi koja prikazuje detalje o proslednjenom objektu klase Dzip
    Nasledjuje klasu TkInter
    '''
    def __init__(self, glavni, oznakaDzipa):
        
        '''
        Constructor
        
        :param glavni: referenca na root view koji ga poziva
        :param oznakaDzipa: string vrednost oznake prosledjenog objekta dzipa
        
        '''
        
        
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Detalji")
        tk.Tk.geometry(self, '500x300')
       
        self.resizable(False, False)
        Centriraj(self)
        
        #kesiraj:
        self.glavni = glavni
        self.dzip = dzipIzOznake(oznakaDzipa)
        
        self.glavni.withdraw()
        
        #self.korisnik = korisnik
       
       #definisi grid prozora, dosta korisno
       #50*50
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
            
           
        self.treeDetalji = ttk.Treeview(self, columns=("size", "modified"))
        self.treeDetalji["columns"] = ( "Obelezje", "Opis")
        
        self.treeDetalji.column("Obelezje", width=100)
        self.treeDetalji.column("Opis", width=100)
        
        self.treeDetalji.heading("Obelezje", text="Obelezje")
        self.treeDetalji.heading("Opis", text="Opis")
        
        self.treeDetalji.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        #Btn:
        ButtonBar = Frame(self)
        
        OkBTN = Button(ButtonBar, text = "Zatvori", command = self.quit)
        OkBTN.pack(side = RIGHT, padx=1, pady=1)
        
        ProstorBTN = Button(ButtonBar, text = "Prostor", command = self.prostor)
        ProstorBTN.pack(side = LEFT, padx=1, pady=1)
    
        ButtonBar.grid(row = 49, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        self.protocol( "WM_DELETE_WINDOW", self.quit )   
        self.Napuni()
            
            
    def quit(self):
        '''
        Metoda koja unistava objekat ovog view-a i ponovo iscrtava root view koji ga je pozvao.
        '''
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()
        
    def prostor(self):
        '''
        Metoda koja poziva view koji prikazuje detalje o povezanom objektu izlozbenog prostora.
        '''
        prostor = self.dzip.izlozbeni_prostor
        view.detaljiProstori.ProstorInfo(self, prostor.oznaka)
        
    def Napuni(self):
        '''
        Metoda koja puni graficku komponentu vrednostima prosledjenog objekta dzipa i time prikazuje detalje o
        njegovim vrednostima.
        '''
        index = 1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Oznaka", self.dzip.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Opis", self.dzip.opis))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Duzina", self.dzip.duzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Sirina", self.dzip.sirina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Visina", self.dzip.visina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Maksimalna brzina", self.dzip.maksimalna_brzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Godina proizvodnje", self.dzip.godina_proizvodnje))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Izlozbeni prostor", self.dzip.izlozbeni_prostor.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Broj vrata", self.dzip.broj_vrata))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("4x4", self.dzip.pogon_na_sva_cetiri_tocka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Konjskih snaga", self.dzip.konjskih_snaga))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Spustajuca klupa", self.dzip.spustajuca_zadnja_klupa))
