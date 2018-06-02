'''
Created on Jun 1, 2018

@author: Freeman
'''

from tkinter import *
from tkinter import ttk

from controller.prostori import prostorIzOznake
from model.singleton import Projekat
import tkinter as tk
#from view.detaljiProstori import DetaljiProstor
from view.gui_utils import Centriraj
from tkinter import messagebox
from controller.automobili import automobilIzOznake
import view.detaljiProstori
from view import detaljiProstori


class DetaljiAutomobili(tk.Tk):
    def __init__(self, glavni, oznakaAutomobila):
        
        
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
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()
    
    def prostor(self):
        prostor = self.automobil.izlozbeni_prostor
        detaljiProstori.ProstorInfo(self, prostor.oznaka)
        
    def Napuni(self):
        #moguc prolaz kroz sve atribute:
        '''
        for attr, value in self.automobil.__dict__.items():
            self.textWidget.insert(INSERT, str(attr) + " : " + str(value) + "\n")
        '''
        
        '''
        self.textWidget.insert(INSERT, 'Oznaka: ' + self.automobil.oznaka + "\n")
        self.textWidget.insert(INSERT, 'Opis: ' + self.automobil.opis + "\n")
        self.textWidget.insert(INSERT, 'Duzina: ' + str(self.automobil.duzina) + "\n")
        self.textWidget.insert(INSERT, 'Sirina: ' + str(self.automobil.sirina) + "\n")
        self.textWidget.insert(INSERT, 'Visina: ' + str(self.automobil.visina) + "\n")
        self.textWidget.insert(INSERT, 'Maksimalna brzina: ' + str(self.automobil.maksimalna_brzina) + "\n")
        self.textWidget.insert(INSERT, 'Godina proizvodnje: ' + str(self.automobil.godina_proizvodnje) + "\n")
        self.textWidget.insert(INSERT, 'Izlozbeni prostor: ' + self.automobil.izlozbeni_prostor.oznaka + "\n")
        self.textWidget.insert(INSERT, 'Broj vrata: ' + str(self.automobil.broj_vrata) + "\n")
        self.textWidget.insert(INSERT, 'Broj sedista: ' + str(self.automobil.broj_sedista) + "\n")
        self.textWidget.insert(INSERT, 'Tip menjaca: ' + str(self.automobil.tip_menjaca.name) + "\n")
        
        #read only - moguce samo nakon pisanja
        self.textWidget.config(state=DISABLED)
        '''
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
        
        
