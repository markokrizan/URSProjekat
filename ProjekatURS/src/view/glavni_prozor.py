'''
Created on May 31, 2018

@author: freeman
'''

#sudo apt-get install python3-tk
from tkinter import *
from tkinter import ttk

from controller.prostori import prostorIzOznake
from model.singleton import Projekat
import tkinter as tk
from view.detaljiProstori import DetaljiProstor
from view.gui_utils import Centriraj
from tkinter import messagebox
from view.detaljiAutomobili import DetaljiAutomobili
from view.detaljiDzipovi import DetaljiDzipovi
from view.detaljiKvadovi import DetaljiKvadovi


class GlavniProzor(tk.Tk):
    def __init__(self):
        
        
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Glavni Prozor")
        tk.Tk.geometry(self, '1024x768')
       
        self.resizable(False, False)
        Centriraj(self)
        
        #self.korisnik = korisnik
       
       #definisi grid prozora, dosta korisno
       #50*50
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
            
            
           
        menu = Menu(self)
        self.config(menu = menu)
        
        subMenu = Menu(menu)
        menu.add_cascade(label = "File", menu = subMenu)
        
        subMenu.add_command(label = "New...")
        subMenu.add_command(label = "Old...")
        subMenu.add_separator()
        subMenu.add_command(label = "Exit")
        
        editMenu = Menu(menu)
        menu.add_cascade(label = "Edit", menu = editMenu)
    
        editMenu.add_command(label = "Redo...") 
           
           
           
       
       
        nb = ttk.Notebook(self)
        nb.grid(row = 1, column = 0, columnspan = 50, rowspan = 49, sticky = 'NESW' )
       
       
        #PAGE PROSTORI:
        page1 = ttk.Frame(nb)
        
        #definisi grid za svaku od kartica
        rowsp1 = 0
        
        while rowsp1 < 50:
            page1.rowconfigure(rowsp1, weight = 1)
            page1.columnconfigure(rowsp1, weight = 1)
            rowsp1 += 1
            
        # ------------------------------------------------------------
        #Page izlozbeni prostori komponente
        
        #Tree Prostori
        self.treeProstori = ttk.Treeview(page1, columns=("size", "modified"))
        self.treeProstori["columns"] = ( "Oznaka", "Opis", "Lokacija")
        
        self.treeProstori.column("Oznaka")
        self.treeProstori.column("Opis")
        self.treeProstori.column("Lokacija")
        
        self.treeProstori.heading("Oznaka", text="Oznaka")
        self.treeProstori.heading("Opis", text="Opis")
        self.treeProstori.heading("Lokacija", text="Lokacija")
        
        self.treeProstori.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        #metoda koje je i osvezavala i ubacivala inicijalne podatke
        #self.Osvezi()
        
        '''
        Primer obicnog dugmeta sa listener funkcijom:
        dodajBTN = Button(CRUDBar, text = "Dodaj", command = self.DodajStudenta)
        dodajBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        Primer dugmenta sa listnerom kojem treba proslediti parametar:
        
        traziBTN = Button(CRUDBar, text = "Trazi", command = lambda: self.NadjiStudenta(traziEntry.get()))
        traziBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziEntry = Entry(CRUDBar)
        traziEntry.pack(side = RIGHT, padx=1, pady=1)
        
        '''
        
        #Kontrole prostori:
        
        CRUDBarProstori = Frame(page1)
        
        dodajBTN = Button(CRUDBarProstori, text = "Dodaj")
        dodajBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniBTN = Button(CRUDBarProstori, text = "Izmeni")
        izmeniBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiBTN = Button(CRUDBarProstori, text = "Vozila", command = self.detaljiProstori)
        obrisiBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziBTN = Button(CRUDBarProstori, text = "Trazi")
        traziBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziEntry = Entry(CRUDBarProstori)
        traziEntry.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarProstori.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        
        
        #**********************************************************************************  
        #Dodavanje izlozbeni prostori page u notebook  
        nb.add(page1, text = "Izlozbeni prostori")
        
        
        
        #-------------------------------------------------------------
        #PAGE AUTOMOBILI: 
        page2 = ttk.Frame(nb)
        
        rowsp2 = 0
        while rowsp2 < 50:
            page2.rowconfigure(rowsp2, weight = 1)
            page2.columnconfigure(rowsp2, weight = 1)
            rowsp2 += 1
        
        # ------------------------------------------------------------
        #Automobili page komponente:
        
        #Tree Automobili
        self.treeAutomobili = ttk.Treeview(page2, columns=("size", "modified"))
        self.treeAutomobili["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeAutomobili.column("Oznaka")
        self.treeAutomobili.column("Opis")
        self.treeAutomobili.column("Izlozbeni prostor")
    
        
        self.treeAutomobili.heading("Oznaka", text="Oznaka")
        self.treeAutomobili.heading("Opis", text="Opis")
        self.treeAutomobili.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        
        self.treeAutomobili.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        #Kontrole automobili:
        
        CRUDBarAutomobili = Frame(page2)
        
        dodajAutomobiliBTN = Button(CRUDBarAutomobili, text = "Dodaj")
        dodajAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniAutomobiliBTN = Button(CRUDBarAutomobili, text = "Izmeni")
        izmeniAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiAutomobiliBTN = Button(CRUDBarAutomobili, text = "Detalji", command = self.detaljiAutomobili)
        detaljiAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziAutomobiliBTN = Button(CRUDBarAutomobili, text = "Trazi")
        traziAutomobiliBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziAutomobiliEntry = Entry(CRUDBarAutomobili)
        traziAutomobiliEntry.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarAutomobili.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje Automobila *************************************************************
        
        SORTBarAutomobili = Frame(page2)
        
        Label(SORTBarAutomobili, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brizna', 'Broj sedista']
        izbor = StringVar()
        izbor.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        automobilSortMenu = OptionMenu(SORTBarAutomobili, izbor, *ponudjeno, command = lambda x: self.SortirajAutomobile(izbor.get()) )
        automobilSortMenu.pack(side = LEFT, padx=1, pady=1)
        
        SORTBarAutomobili.grid(row = 1, column = 0, columnspan = 50, rowspan = 1, sticky = 'NESW' )
        
        
        
        #-------------------------------------------------------------
        #Automobili page dodavanje na notebook
        nb.add(page2, text = "Automobili")
        #---------------------------------------------------------------
        
        
        
        #-------------------------------------------------------------
        #PAGE DZIPOVI:        
        page3 = ttk.Frame(nb)
        
        rowsp3 = 0
        while rowsp3 < 50:
            page3.rowconfigure(rowsp3, weight = 1)
            page3.columnconfigure(rowsp3, weight = 1)
            rowsp3 += 1
        
        # ------------------------------------------------------------
        #Dzipovi page komponente:
        
        #Tree Dzipovi
        self.treeDzipovi = ttk.Treeview(page3, columns=("size", "modified"))
        self.treeDzipovi["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeDzipovi.column("Oznaka")
        self.treeDzipovi.column("Opis")
        self.treeDzipovi.column("Izlozbeni prostor")
    
        
        self.treeDzipovi.heading("Oznaka", text="Oznaka")
        self.treeDzipovi.heading("Opis", text="Opis")
        self.treeDzipovi.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        
        self.treeDzipovi.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        #Kontrole dzipovi:
        
        CRUDBarDzipovi = Frame(page3)
        
        DodajDzipBTN = Button(CRUDBarDzipovi, text = "Dodaj")
        DodajDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniDzipBTN = Button(CRUDBarDzipovi, text = "Izmeni")
        izmeniDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiDzipBTN = Button(CRUDBarDzipovi, text = "Detalji", command = self.detaljiDzipovi)
        detaljiDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziDzipoviBTN = Button(CRUDBarDzipovi, text = "Trazi")
        traziDzipoviBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziDzipoviEntry = Entry(CRUDBarDzipovi)
        traziDzipoviEntry.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarDzipovi.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje dzipova *************************************************************
        
        SORTBarDzipovi = Frame(page3)
        
        Label(SORTBarDzipovi, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brizna', 'Konjeske snage']
        izbor = StringVar()
        izbor.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        dzipoviSortMenu = OptionMenu(SORTBarDzipovi, izbor, *ponudjeno, command = lambda x: self.SortirajDzipove(izbor.get()) )
        dzipoviSortMenu.pack(side = LEFT, padx=1, pady=1)
        
        SORTBarDzipovi.grid(row = 1, column = 0, columnspan = 50, rowspan = 1, sticky = 'NESW' )
        
        
        
        
        #-------------------------------------------------------------
        #Dzipovi page dodavanje na notebook
        nb.add(page3, text = "Dzipovi")
        #---------------------------------------------------------------
        
        
        
        #-------------------------------------------------------------
        #PAGE KVADOVI:        
        page4 = ttk.Frame(nb)
        
        rowsp4 = 0
        while rowsp4 < 50:
            page4.rowconfigure(rowsp4, weight = 1)
            page4.columnconfigure(rowsp4, weight = 1)
            rowsp4 += 1
        
        # ------------------------------------------------------------
        #Kvadovi page komponente:
        
        #Tree Kvadovi
        self.treeKvadovi = ttk.Treeview(page4, columns=("size", "modified"))
        self.treeKvadovi["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeKvadovi.column("Oznaka")
        self.treeKvadovi.column("Opis")
        self.treeKvadovi.column("Izlozbeni prostor")
    
        
        self.treeKvadovi.heading("Oznaka", text="Oznaka")
        self.treeKvadovi.heading("Opis", text="Opis")
        self.treeKvadovi.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        
        self.treeKvadovi.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        #Kontrole kvadovi:
        
        CRUDBarKvadovi = Frame(page4)
        
        dodajKvadBTN = Button(CRUDBarKvadovi, text = "Dodaj")
        dodajKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniKvadBTN = Button(CRUDBarKvadovi, text = "Izmeni")
        izmeniKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiKvadBTN = Button(CRUDBarKvadovi, text = "Detalji", command = self.detaljiKvadovi)
        detaljiKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziKvadBTN = Button(CRUDBarKvadovi, text = "Trazi")
        traziKvadBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziKvadEntry = Entry(CRUDBarKvadovi)
        traziKvadEntry.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarKvadovi.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje kvadova *************************************************************
        
        SORTBARKvadovi = Frame(page4)
        
        Label(SORTBARKvadovi, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brizna', 'Godina proizvodnje']
        izbor = StringVar()
        izbor.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        kvadoviSortMenu = OptionMenu(SORTBARKvadovi, izbor, *ponudjeno, command = lambda x: self.SortirajKvadove(izbor.get()) )
        kvadoviSortMenu.pack(side = LEFT, padx=1, pady=1)
        
        SORTBARKvadovi.grid(row = 1, column = 0, columnspan = 50, rowspan = 1, sticky = 'NESW' )
        
        
        
        
        
        #-------------------------------------------------------------
        #Kvadovi page dodavanje na notebook
        nb.add(page4, text = "Kvadovi")
        #---------------------------------------------------------------
        
        
        #Ucitavanja:
        self.OsveziProstore()
        self.OsveziAutomobile()
        self.OsveziDzipove()
        self.OsveziKvadove()
        
        
    
        
        #------------------------STATUS---------------------------
        #status = Label(self, text = "Ulogovani korisnik: " + self.korisnik.Ime, bd = 1, relief = SUNKEN, anchor = W)
        #status.grid(row = 50, column = 0, columnspan = 50, rowspan = 48, sticky = 'NESW' )
        
    # -----------------------------------------------------------------------------------------------------------------------------    
        
    #Funkcije za osvezavanje:
    
    def OsveziProstore(self):
        #prvo ocisti
        for i in self.treeProstori.get_children():
            self.tree.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().prostori):
            self.treeProstori.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.lokacija))
    
    def OsveziAutomobile(self):
        #prvo ocisti
        for i in self.treeAutomobili.get_children():
            self.tree.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().automobili):
            self.treeAutomobili.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def OsveziDzipove(self):
        #prvo ocisti
        for i in self.treeDzipovi.get_children():
            self.tree.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().dzipovi):
            self.treeDzipovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
            
    def OsveziKvadove(self):
        #prvo ocisti
        for i in self.treeKvadovi.get_children():
            self.tree.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().kvadovi):
            self.treeKvadovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    #Funkcije za detalje:
    
    def detaljiProstori(self):
        try:
            selektovani = self.treeProstori.selection()[0]
            oznakaProstora = self.treeProstori.item(selektovani)['values'][0]
            DetaljiProstor(self, oznakaProstora)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
        
    def detaljiAutomobili(self):
        try:
            selektovani = self.treeAutomobili.selection()[0]
            oznakaAutomobila = self.treeAutomobili.item(selektovani)['values'][0]
            DetaljiAutomobili(self, oznakaAutomobila)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
        
    
    def detaljiDzipovi(self):
        try:
            selektovani = self.treeDzipovi.selection()[0]
            oznakaDzipa = self.treeDzipovi.item(selektovani)['values'][0]
            DetaljiDzipovi(self, oznakaDzipa)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
    
    def detaljiKvadovi(self):
        try:
            selektovani = self.treeKvadovi.selection()[0]
            oznakaKvada = self.treeKvadovi.item(selektovani)['values'][0]
            DetaljiKvadovi(self, oznakaKvada)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
    
    
    
    
    
    
      
    