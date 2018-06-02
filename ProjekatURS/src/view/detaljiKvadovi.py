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
from controller.kvadovi import kvadIzOznake
import view.detaljiProstori
from view import detaljiProstori

class DetaljiKvadovi(tk.Tk):
    def __init__(self, glavni, oznakaKvada):
        
        
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Detalji")
        tk.Tk.geometry(self, '500x300')
       
        self.resizable(False, False)
        Centriraj(self)
        
        #kesiraj:
        self.glavni = glavni
        self.kvad = kvadIzOznake(oznakaKvada)
        
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
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()
        
    def prostor(self):
        prostor = self.kvad.izlozbeni_prostor
        detaljiProstori.ProstorInfo(self, prostor.oznaka)
        
    def Napuni(self):
        
        index = 1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Oznaka", self.kvad.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Opis", self.kvad.opis))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Duzina", self.kvad.duzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Sirina", self.kvad.sirina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Visina", self.kvad.visina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Maksimalna brzina", self.kvad.maksimalna_brzina))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Godina proizvodnje", self.kvad.godina_proizvodnje))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Izlozbeni prostor", self.kvad.izlozbeni_prostor.oznaka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("4x4", self.kvad.pogon_na_sva_cetiri_tocka))
        index+=1
        self.treeDetalji.insert("", 'end' ,text = index, values = ("Prostor za stvari", self.kvad.prostor_za_stvari))
        
