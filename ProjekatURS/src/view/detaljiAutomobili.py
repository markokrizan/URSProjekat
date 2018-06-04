'''
Modul koji sadrzi klasu koja opisuje view koji se koristi za prikaz detalja o objektu klase Automobil.

@author: Aleksandar Rancic
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.automobili import automobilIzOznake
from controller.prostori import prostorIzOznake
from model.singleton import Projekat
import tkinter as tk
import view.detaljiProstori 
from view.gui_utils import Centriraj


#from view.detaljiProstori import DetaljiProstor
class DetaljiAutomobili(tk.Tk):
    '''
    Klasa view-a koja opisuje detalje o objektu klase Automobil.
    Naslejduje TkInter klasu.
    '''
    def __init__(self, glavni, oznakaAutomobila):
        '''
        Constructor 
        
        :param glavni: prosledjena referenca na root view koji je pozvao ovaj view
        :param oznakaAutomobila: prosledji objekat klase automobil
        
        '''
        
        
        
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Detalji")
        tk.Tk.geometry(self, '500x300')
       
        self.resizable(False, False)
        Centriraj(self)
        
        #kesiraj:
        self.glavni = glavni
        self.automobil = automobilIzOznake(oznakaAutomobila)
        
        self.glavni.withdraw()
        
        #self.korisnik = korisnik
       
       #definisi grid prozora, dosta korisno
       #50*50
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
            
        
        '''
        #Text Widget
        self.textWidget = Text(self)
        self.textWidget.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        '''
            
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
        Metoda koja po zatvaranju view-a unistava njegov objekat i ponovo iscrtava root view koji ga je pozvao
        '''
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()
    
    def prostor(self):
        '''
        Metoda koja se okida po kliku na dugme ProstorBTN i poziva view koji prikazuje informacije o izlozbenom
        prostoru automobila.
        '''
        prostor = self.automobil.izlozbeni_prostor
        #ProstorInfo(self, prostor.oznaka)
        view.detaljiProstori.ProstorInfo(self, prostor.oznaka)
        
    def Napuni(self):
        '''
        Metoda koja puni graficku komponentu za prikaz informacija o objektu vrednostima atributa prosledjenog objekta klase Automobil.
        '''
        
        
        
        
        #moguc prolaz kroz sve atribute:
        #for attr, value in self.automobil.__dict__.items():
        #    self.textWidget.insert(INSERT, str(attr) + " : " + str(value) + "\n")
        
        
        index = 1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Oznaka", self.automobil.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Opis", self.automobil.opis))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Duzina", self.automobil.duzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Sirina", self.automobil.sirina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Visina", self.automobil.visina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Maksimalna brzina", self.automobil.maksimalna_brzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Godina proizvodnje", self.automobil.godina_proizvodnje))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Izlozbeni prostor", self.automobil.izlozbeni_prostor.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Broj vrata", self.automobil.broj_vrata))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Broj sedista", self.automobil.broj_sedista))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Tip menjaca", self.automobil.tip_menjaca.name))
        
        
