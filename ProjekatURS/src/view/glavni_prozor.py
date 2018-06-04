'''
Modul koji sadrzi view klasu za opis glavnog prozora aplikacije, iz kojeg se pozivaju svi drugi.

@author: Marko Krizan
'''

#sudo apt-get install python3-tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.automobili import automobilIzOznake, ObrisiAutomobil,\
    nadjiAutomobile, sortirajAutomobile
from controller.dzipovi import dzipIzOznake, ObrisiDzip, nadjiDzipove,\
    sortirajDzipove
from controller.prostori import prostorIzOznake, ObrisiProstor, nadjiProstore
from model.salon import IzlozbeniProstor, Automobil, Dzip, Kvad
from model.singleton import Projekat
import tkinter as tk
from view.FORME import ProstorCU, Operacija, AutomobilCU, DzipCU, KvadCU
from view.detaljiAutomobili import DetaljiAutomobili
from view.detaljiDzipovi import DetaljiDzipovi
from view.detaljiKvadovi import DetaljiKvadovi
from view.detaljiProstori import DetaljiProstor
from view.gui_utils import Centriraj
from controller.kvadovi import kvadIzOznake, ObrisiKvad, nadjiKvadove,\
    sortirajKvadove


class GlavniProzor(tk.Tk):
    '''
    View klasa glavnog prozora koja opisuje izlged svih pojedinacnih komponenti i funkcionalnosti za njegovo koriscenje.
    Nasledjuje klasu TkInter
    '''
    def __init__(self):
        '''
        Constructor
        
        
        '''
        
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
        
        dodajBTN = Button(CRUDBarProstori, text = "Dodaj", command = self.DodajProstor)
        dodajBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniBTN = Button(CRUDBarProstori, text = "Izmeni", command = self.IzmeniProstor)
        izmeniBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiBTN = Button(CRUDBarProstori, text = "Obrisi", command = self.ObrisiProstor)
        obrisiBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiBTN = Button(CRUDBarProstori, text = "Vozila", command = self.detaljiProstori)
        obrisiBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziBTN = Button(CRUDBarProstori, text = "Trazi", command = lambda: self.NadjiProstor(traziEntry.get()))
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
        
        dodajAutomobiliBTN = Button(CRUDBarAutomobili, text = "Dodaj", command = self.DodajAutomobil)
        dodajAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniAutomobiliBTN = Button(CRUDBarAutomobili, text = "Izmeni", command = self.IzmeniAutomobil)
        izmeniAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniAutomobiliBTN = Button(CRUDBarAutomobili, text = "Obrisi", command = self.ObrisiAutomobil)
        izmeniAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiAutomobiliBTN = Button(CRUDBarAutomobili, text = "Detalji", command = self.detaljiAutomobili)
        detaljiAutomobiliBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziAutomobiliBTN = Button(CRUDBarAutomobili, text = "Trazi", command = lambda: self.NadjiAutomobil(traziAutomobiliEntry.get()))
        traziAutomobiliBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziAutomobiliEntry = Entry(CRUDBarAutomobili)
        traziAutomobiliEntry.pack(side = RIGHT, padx=1, pady=1)
        
    
        
        
        
        CRUDBarAutomobili.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje Automobila *************************************************************
        
        SORTBarAutomobili = Frame(page2)
        
        Label(SORTBarAutomobili, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brzina', 'Broj sedista']
        self.izbor = StringVar()
        self.izbor.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        automobilSortMenu = OptionMenu(SORTBarAutomobili, self.izbor, *ponudjeno, command = lambda x: self.SortirajAutomobile(self.izbor.get()) )
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
        
        DodajDzipBTN = Button(CRUDBarDzipovi, text = "Dodaj", command = self.DodajDzip)
        DodajDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniDzipBTN = Button(CRUDBarDzipovi, text = "Izmeni", command = self.IzmeniDzip)
        izmeniDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiDzipBTN = Button(CRUDBarDzipovi, text = "Obrisi", command = self.ObrisiDzip)
        obrisiDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiDzipBTN = Button(CRUDBarDzipovi, text = "Detalji", command = self.detaljiDzipovi)
        detaljiDzipBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziDzipoviBTN = Button(CRUDBarDzipovi, text = "Trazi", command = lambda: self.NadjiDzip(traziDzipoviEntry.get()))
        traziDzipoviBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziDzipoviEntry = Entry(CRUDBarDzipovi)
        traziDzipoviEntry.pack(side = RIGHT, padx=1, pady=1)
        
        self.saPogonom = IntVar()
        self.saKlupom = IntVar()
        
        pogonCheck = Checkbutton(CRUDBarDzipovi, onvalue = True, offvalue = False, text = "4x4 ", variable = self.saPogonom)
        pogonCheck.pack(side = RIGHT, padx=1, pady=1)
        
        klupaCheck = Checkbutton(CRUDBarDzipovi,onvalue = True, offvalue = False, text = "Zadnja klupa ", variable = self.saKlupom)
        klupaCheck.pack(side = RIGHT, padx=1, pady=1)
        
        refreshButton = Button(CRUDBarDzipovi, text = "R", command = self.OsveziDzipove)
        refreshButton.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarDzipovi.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje dzipova *************************************************************
        
        SORTBarDzipovi = Frame(page3)
        
        Label(SORTBarDzipovi, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brzina', 'Konjskih snaga']
        self.izborDzip = StringVar()
        self.izborDzip.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        dzipoviSortMenu = OptionMenu(SORTBarDzipovi, self.izborDzip, *ponudjeno, command = lambda x: self.SortirajDzipove(self.izborDzip.get()) )
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
        
        dodajKvadBTN = Button(CRUDBarKvadovi, text = "Dodaj", command = self.DodajKvad)
        dodajKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniKvadBTN = Button(CRUDBarKvadovi, text = "Izmeni", command = self.IzmeniKvad)
        izmeniKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiKvadBTN = Button(CRUDBarKvadovi, text = "Obrisi", command = self.ObrisiKvad)
        obrisiKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        detaljiKvadBTN = Button(CRUDBarKvadovi, text = "Detalji", command = self.detaljiKvadovi)
        detaljiKvadBTN.pack(side = LEFT, padx=1, pady=1)
        
        
        
        traziKvadBTN = Button(CRUDBarKvadovi, text = "Trazi", command = lambda: self.NadjiKvad(traziKvadEntry.get()))
        traziKvadBTN.pack(side = RIGHT, padx=1, pady=1)
        
        traziKvadEntry = Entry(CRUDBarKvadovi)
        traziKvadEntry.pack(side = RIGHT, padx=1, pady=1)
        
        self.saPogonomKvad = IntVar()
        self.saProstoromKvad = IntVar()
        
        pogonCheckKvad = Checkbutton(CRUDBarKvadovi, onvalue = True, offvalue = False, text = "4x4 ", variable = self.saPogonomKvad)
        pogonCheckKvad.pack(side = RIGHT, padx=1, pady=1)
        
        stvariCheck = Checkbutton(CRUDBarKvadovi,onvalue = True, offvalue = False, text = "Prostor za stvari ", variable = self.saProstoromKvad)
        stvariCheck.pack(side = RIGHT, padx=1, pady=1)
        
        refreshButton = Button(CRUDBarKvadovi, text = "R", command = self.OsveziKvadove)
        refreshButton.pack(side = RIGHT, padx=1, pady=1)
        
        
        
        CRUDBarKvadovi.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        #Sortiranje kvadova *************************************************************
        
        SORTBARKvadovi = Frame(page4)
        
        Label(SORTBARKvadovi, text="Sortiraj po: ").pack(side = LEFT, padx=1, pady=1)
        
        ponudjeno = ['Maksimalna brzina', 'Godina proizvodnje']
        self.izborKvad = StringVar()
        self.izborKvad.set(ponudjeno[0])
        
        #Unused argument? _ convention, stavio x da primetim
        kvadoviSortMenu = OptionMenu(SORTBARKvadovi, self.izborKvad, *ponudjeno, command = lambda x: self.SortirajKvadove(self.izborKvad.get()) )
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
        '''
        Metoda koja osvezava graficku komponentu za prikaz entiteta izlozbenih prostora tako sto je prvo ocisti i ponovo ucita iz kolekcije.
        '''
        #prvo ocisti
        for i in self.treeProstori.get_children():
            self.treeProstori.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().prostori):
            self.treeProstori.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.lokacija))
    
    def OsveziAutomobile(self):
        '''
        Metoda koja osvezava graficku komponentu za prikaz entiteta automobila tako sto je prvo ocisti i ponovo ucita iz kolekcije.
        '''
        #prvo ocisti
        for i in self.treeAutomobili.get_children():
            self.treeAutomobili.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().automobili):
            self.treeAutomobili.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def OsveziDzipove(self):
        '''
        Metoda koja osvezava graficku komponentu za prikaz entiteta dzipova tako sto je prvo ocisti i ponovo ucita iz kolekcije.
        '''
        #prvo ocisti
        for i in self.treeDzipovi.get_children():
            self.treeDzipovi.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().dzipovi):
            self.treeDzipovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
            
    def OsveziKvadove(self):
        '''
        Metoda koja osvezava graficku komponentu za prikaz entiteta kvadova tako sto je prvo ocisti i ponovo ucita iz kolekcije.
        '''
        #prvo ocisti
        for i in self.treeKvadovi.get_children():
            self.treeKvadovi.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(Projekat().kvadovi):
            self.treeKvadovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    #Funkcije za detalje:
    
    def detaljiProstori(self):
        '''
        Metoda koja poziva view za prikaz detalja o selektovanom entitetu izlozbenog prostora.
        '''
        try:
            selektovani = self.treeProstori.selection()[0]
            oznakaProstora = self.treeProstori.item(selektovani)['values'][0]
            DetaljiProstor(self, oznakaProstora)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
        
    def detaljiAutomobili(self):
        '''
        Metoda koja poziva view za prikaz detalja o selektovanom entitetu automobila.
        '''
        try:
            selektovani = self.treeAutomobili.selection()[0]
            oznakaAutomobila = self.treeAutomobili.item(selektovani)['values'][0]
            DetaljiAutomobili(self, oznakaAutomobila)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
        
    
    def detaljiDzipovi(self):
        '''
        Metoda koja poziva view za prikaz detalja o selektovanom entitetu dzipa.
        '''
        try:
            selektovani = self.treeDzipovi.selection()[0]
            oznakaDzipa = self.treeDzipovi.item(selektovani)['values'][0]
            DetaljiDzipovi(self, oznakaDzipa)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
    
    def detaljiKvadovi(self):
        '''
        Metoda koja poziva view za prikaz detalja o selektovanom entitetu kvada.
        '''
        try:
            selektovani = self.treeKvadovi.selection()[0]
            oznakaKvada = self.treeKvadovi.item(selektovani)['values'][0]
            DetaljiKvadovi(self, oznakaKvada)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
    
    #CREATE / UPDATE / DELETE
    
    #Prostori:
    
    def DodajProstor(self):
        '''
        Metoda koja kreira prazan objekat izlozbenog prostora i prosledi ga formi za obradu koja ce izvrsiti insert funkcionalnost.
        '''
        prostor = IzlozbeniProstor.empty()
        ProstorCU(prostor, Operacija.DODAVANJE, self)
        
    
    def IzmeniProstor(self):
        '''
        Metoda koja formi za obradu entiteta izlozbenog prostora prosledi selektovani objekat nad kojim ona vrsi update funkcionalnost.
        '''
        try:
            selektovani = self.treeProstori.selection()[0]
            oznakaProstora = self.treeProstori.item(selektovani)['values'][0]
            prostor = prostorIzOznake(oznakaProstora)
            ProstorCU(prostor, Operacija.IZMENA, self)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    def ObrisiProstor(self):
        '''
        Metoda koja selektovani objekat izlozbenog prostora prosledjuje kontroleru za uklanjanje iz kolekcije i perzistiranje i osvezava view.
        '''
        try:
            selektovani = self.treeProstori.selection()[0]
            oznakaProstora = self.treeProstori.item(selektovani)['values'][0]
            odgovor = messagebox.askquestion("Obrisi", "Da li ste sigurni?", icon='warning')
            if (odgovor == 'yes'):
                ObrisiProstor(oznakaProstora)
                self.OsveziProstore()
            
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    #Automobili:
    
    def DodajAutomobil(self):
        '''
        Metoda koja kreira prazan objekat automobila i prosledi ga formi za obradu koja ce izvrsiti insert funkcionalnost.
        '''
        automobil = Automobil.empty()
        #print(automobil)
        AutomobilCU(automobil, Operacija.DODAVANJE, self)
        
    
    def IzmeniAutomobil(self):
        '''
        Metoda koja formi za obradu entiteta automobila prosledi selektovani objekat nad kojim ona vrsi update funkcionalnost.
        '''
        try:
            selektovani = self.treeAutomobili.selection()[0]
            oznakaAutomobila = self.treeAutomobili.item(selektovani)['values'][0]
            automobil = automobilIzOznake(oznakaAutomobila)
            AutomobilCU(automobil, Operacija.IZMENA, self)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    def ObrisiAutomobil(self):
        '''
        Metoda koja selektovani objekat automobila prosledjuje kontroleru za uklanjanje iz kolekcije i perzistiranje i osvezava view.
        '''
        try:
            selektovani = self.treeAutomobili.selection()[0]
            oznakaAutomobila = self.treeAutomobili.item(selektovani)['values'][0]
            odgovor = messagebox.askquestion("Obrisi", "Da li ste sigurni?", icon='warning')
            if (odgovor == 'yes'):
                ObrisiAutomobil(oznakaAutomobila)
                self.OsveziAutomobile()
            
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    #Dzipovi
    def DodajDzip(self):
        '''
        Metoda koja kreira prazan objekat dzipa i prosledi ga formi za obradu koja ce izvrsiti insert funkcionalnost.
        '''
        dzip = Dzip.empty()
        #print(automobil)
        DzipCU(dzip, Operacija.DODAVANJE, self)
        
    
    def IzmeniDzip(self):
        '''
        Metoda koja formi za obradu entiteta dzipa prosledi selektovani objekat nad kojim ona vrsi update funkcionalnost.
        '''
        try:
            selektovani = self.treeDzipovi.selection()[0]
            oznakaDzipa = self.treeDzipovi.item(selektovani)['values'][0]
            dzip = dzipIzOznake(oznakaDzipa)
            DzipCU(dzip, Operacija.IZMENA, self)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    def ObrisiDzip(self):
        '''
        Metoda koja selektovani objekat dzipa prosledjuje kontroleru za uklanjanje iz kolekcije i perzistiranje i osvezava view.
        '''
        try:
            selektovani = self.treeDzipovi.selection()[0]
            oznakaDzipa = self.treeDzipovi.item(selektovani)['values'][0]
            odgovor = messagebox.askquestion("Obrisi", "Da li ste sigurni?", icon='warning')
            if (odgovor == 'yes'):
                ObrisiDzip(oznakaDzipa)
                self.OsveziDzipove()
            
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    #Kvadovi:
    
    def DodajKvad(self):
        '''
        Metoda koja kreira prazan objekat kvada i prosledi ga formi za obradu koja ce izvrsiti insert funkcionalnost.
        '''
        kvad = Kvad.empty()
        KvadCU(kvad, Operacija.DODAVANJE, self)
        
    
    def IzmeniKvad(self):
        '''
        Metoda koja formi za obradu entiteta kvada prosledi selektovani objekat nad kojim ona vrsi update funkcionalnost.
        '''
        try:
            selektovani = self.treeKvadovi.selection()[0]
            oznakaKvad = self.treeKvadovi.item(selektovani)['values'][0]
            kvad = kvadIzOznake(oznakaKvad)
            KvadCU(kvad, Operacija.IZMENA, self)
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    def ObrisiKvad(self):
        '''
        Metoda koja selektovani objekat kvada prosledjuje kontroleru za uklanjanje iz kolekcije i perzistiranje i osvezava view.
        '''
        try:
            selektovani = self.treeKvadovi.selection()[0]
            oznakaKvad = self.treeKvadovi.item(selektovani)['values'][0]
            odgovor = messagebox.askquestion("Obrisi", "Da li ste sigurni?", icon='warning')
            if (odgovor == 'yes'):
                ObrisiKvad(oznakaKvad)
                self.OsveziKvadove()
            
        except IndexError:
            messagebox.showerror("Greska", "Nista nije selektovano")
            
    #PRETRAGA:
    
    def NadjiProstor(self, query):
        '''
        Metoda koja prosledjuje kriterijum za pretragu kontroleru od kojeg dobija kolekciju objekata koji su rezultat
        pretrage, sa kojima ponovo puni graficku komponentu za prikaz
        
        :param query: string vrednost kriterijuma za pretragu
        '''
        if(query != ''):
            trazeniProstori = nadjiProstore(query)
            for i in self.treeProstori.get_children():
                self.treeProstori.delete(i)
            #ponovo ucitaj iz kolekcije
            for index, i in enumerate(trazeniProstori):
                self.treeProstori.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.lokacija))
        else:
            self.OsveziProstore()
            
    def NadjiAutomobil(self, query):
        '''
        Metoda koja prosledjuje kriterijum za pretragu kontroleru od kojeg dobija kolekciju objekata koji su rezultat
        pretrage, sa kojima ponovo puni graficku komponentu za prikaz
        
        :param query: string vrednost kriterijuma za pretragu
        '''
        if(query != ''):
            trazeniAutomobili = nadjiAutomobile(query)
            for i in self.treeAutomobili.get_children():
                self.treeAutomobili.delete(i)
            #ponovo ucitaj iz kolekcije
            for index, i in enumerate(trazeniAutomobili):
                self.treeAutomobili.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
        else:
            self.OsveziAutomobile()
    
    def NadjiDzip(self, query):
        '''
        Metoda koja prosledjuje kriterijume za pretragu kontroleru od kojeg dobija kolekciju objekata koji su rezultat
        pretrage, sa kojima ponovo puni graficku komponentu za prikaz
        
        :param query: string vrednost kriterijuma za pretragu
        '''
        pogon = True if self.saPogonom.get() == 1 else False
        zadnja_klupa = True if self.saKlupom.get() == 1 else False
        trazeniDzipovi = nadjiDzipove(query, pogon, zadnja_klupa)
        for i in self.treeDzipovi.get_children():
            self.treeDzipovi.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(trazeniDzipovi):
            self.treeDzipovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
       
    
    def NadjiKvad(self, query):
        '''
        Metoda koja prosledjuje kriterijume za pretragu kontroleru od kojeg dobija kolekciju objekata koji su rezultat
        pretrage, sa kojima ponovo puni graficku komponentu za prikaz
        
        :param query: string vrednost kriterijuma za pretragu
        '''
        pogon = True if self.saPogonomKvad.get() == 1 else False
        stvari = True if self.saProstoromKvad.get() == 1 else False
        trazeniKvadovi = nadjiKvadove(query, pogon, stvari)
        for i in self.treeKvadovi.get_children():
            self.treeKvadovi.delete(i)
        #ponovo ucitaj iz kolekcije
        for index, i in enumerate(trazeniKvadovi):
            self.treeKvadovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
        
        
    
    #SORTIRANJE:
    
    def SortirajAutomobile(self, kriterijum):
        '''
        Metoda koja prima parametar kriterujama za sortiranje koji prosledjuje kontroleru od kojeg dobija sortiranu kolekciju
        koju koristi pri ponovnom osvezavanju graficke komponente za prikaz.
        '''
        if (kriterijum == 'Maksimalna brzina'):
            sortiranaKolekcija = sortirajAutomobile('maksimalna_brzina')
            for i in self.treeAutomobili.get_children():
                self.treeAutomobili.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeAutomobili.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
        elif(kriterijum == 'Broj sedista'):
            sortiranaKolekcija = sortirajAutomobile('broj_sedista')
            for i in self.treeAutomobili.get_children():
                self.treeAutomobili.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeAutomobili.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def SortirajDzipove(self, kriterijum):
        '''
        Metoda koja prima parametar kriterujama za sortiranje koji prosledjuje kontroleru od kojeg dobija sortiranu kolekciju
        koju koristi pri ponovnom osvezavanju graficke komponente za prikaz.
        '''
        if (kriterijum == 'Maksimalna brzina'):
            sortiranaKolekcija = sortirajDzipove('maksimalna_brzina')
            for i in self.treeDzipovi.get_children():
                self.treeDzipovi.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeDzipovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
        elif(kriterijum == 'Konjskih snaga'):
            sortiranaKolekcija = sortirajDzipove('konjskih_snaga')
            for i in self.treeDzipovi.get_children():
                self.treeDzipovi.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeDzipovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def SortirajKvadove(self, kriterijum):
        '''
        Metoda koja prima parametar kriterujama za sortiranje koji prosledjuje kontroleru od kojeg dobija sortiranu kolekciju
        koju koristi pri ponovnom osvezavanju graficke komponente za prikaz.
        '''
        if (kriterijum == 'Maksimalna brzina'):
            sortiranaKolekcija = sortirajKvadove('maksimalna_brzina')
            for i in self.treeKvadovi.get_children():
                self.treeKvadovi.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeKvadovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
        elif(kriterijum == 'Godina proizvodnje'):
            sortiranaKolekcija = sortirajKvadove('godina_proizvodnje')
            for i in self.treeKvadovi.get_children():
                self.treeKvadovi.delete(i)
            for index, i in enumerate(sortiranaKolekcija):
                self.treeKvadovi.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    
        
    
    
    
    
      
    