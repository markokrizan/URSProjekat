'''
Modul koji sadrzi view klase koje opisuju izgled i funkcionalnost formi za insert i update radnje nad entitetima.

@author: Marko Krizan
'''

from enum import Enum
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.prostori import prostorIzOznake, DodajProstor, \
    IzmeniProstor
from controller.prostori import generisiOznaku as p
from controller.automobili import generisiOznaku as a, DodajAutomobil,\
    IzmeniAutomobil
from controller.dzipovi import generisiOznaku as dz, DodajDzip, IzmeniDzip
from controller.kvadovi import generisiOznaku as kv, DodajKvad, IzmeniKvad
from model.salon import TipMenjaca
from model.singleton import Projekat
import tkinter as tk
from view.gui_utils import Centriraj


class Operacija(Enum):
    '''
    Klasa Operacija koja nasledjuje klasu Enum i cini enumeraciju mogucih vresnoti moda rada view-a radi recikliranja.
    '''
    DODAVANJE = 1
    IZMENA = 2

class ProstorCU(tk.Tk):
    '''
    Klasa koja opisuje view forme za insert i update nad entitetom izlozbeni prostor.
    Nasledjuje klasu TkInter
    '''
    def __init__(self, prostor, operacija, glavni):
        '''
        Constructor
        
        :param prostor: objekat izlozbenog prostora koji se obradjuje (create - prazan, postojeci - update)
        :param operacija: enumeracija koja odredjuje da li se forma koristi za insert ili update
        :param glavni: referenca na root view koji ga poziva
        '''
        tk.Tk.__init__(self)
        
       
        tk.Tk.wm_title(self, "Prostor UD")
        tk.Tk.geometry(self, '200x150')
        self.resizable(False, False)
        Centriraj(self)
        
        self.prostor = prostor
        self.operacija = operacija
        
        #referenca na glavni da se moze iskoristiti Osvezi
        self.glavni = glavni
        
        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        Input = Frame(self)
        
        #oznaka ce se kreirati samo i inkrementirati na odredjen nacin
        self.opisLabel = Label(Input, text = "Opis: ")
        self.lokacijaLabel = Label(Input, text = "Lokacija: ")
        
        self.opisEntry = Entry(Input)
        self.lokacijaEntry = Entry(Input)
        
        #napuni vrednostima, ako se prosledi prazan student bice prazno
        self.opisEntry.insert(0, prostor.opis)
        self.lokacijaEntry.insert(0, prostor.lokacija)
       
        
        
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.ProstorCU)
      
       
        self.opisLabel.grid(row = 1, sticky = E)#
        self.lokacijaLabel.grid(row = 2, sticky = E)
        self.opisEntry.grid(row = 1, column = 1)
        self.lokacijaEntry.grid(row = 2, column = 1)
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.grid(row = 2, column = 0, columnspan = 10, rowspan = 10, sticky = 'NESW' )
        
        
    def ProstorCU(self):
        '''
        Metoda koja se okida po kliku na potvrdiBTN dugme, koja odreduje koji tip operacije je forma radila i prema tome
        poziva metode kontrolera za perzistiranje i metode root view-a za osvezavanje pogleda.
        '''
        if self.operacija == Operacija.DODAVANJE:
            
            
            
            self.prostor.oznaka = p()
            self.prostor.opis = self.opisEntry.get()
            self.prostor.lokacija = self.lokacijaEntry.get()
            
            
            DodajProstor(self.prostor)
            
            self.glavni.OsveziProstore()
            
            #vidi ovo sta se desava, mozda destruktor eksplicitno
            self.withdraw()
            
            
        elif self.operacija == Operacija.IZMENA:
            #print(self.student)
            
            self.prostor.opis = self.opisEntry.get()
            self.prostor.lokacija = self.lokacijaEntry.get()
            
            
            IzmeniProstor(self.prostor)
            
            self.glavni.OsveziProstore()
            
            self.withdraw()
            
            
class AutomobilCU(tk.Tk):
    '''
    Klasa koja opisuje view forme za insert i update nad entitetom automobil.
    Nasledjuje klasu TkInter
    '''
    def __init__(self, automobil, operacija, glavni):
        '''
        Constructor
        
        :param automobil: objekat automobila koji se obradjuje (create - prazan, postojeci - update)
        :param operacija: enumeracija koja odredjuje da li se forma koristi za insert ili update
        :param glavni: referenca na root view koji ga poziva
        '''
        tk.Tk.__init__(self)
        
        '''
        self.izabraniMenjac
        self.izabraniProstor
        '''
        
        tk.Tk.wm_title(self, "Automobil UD")
        tk.Tk.geometry(self, '220x300')
        self.resizable(False, False)
        Centriraj(self)
        
        self.automobil = automobil
        self.operacija = operacija
        
        self.izabraniMenjac = self.automobil.tip_menjaca
        self.izabraniProstor = self.automobil.izlozbeni_prostor
        
        
        
        #referenca na glavni da se moze iskoristiti Osvezi
        self.glavni = glavni
        
        rows = 0
        while rows < 15:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        Input = Frame(self)
        
        #oznaka ce se kreirati sama i inkrementirati na odredjen nacin
        self.opisLabel = Label(Input, text = "Opis: ")
        self.duzinaLabel = Label(Input, text = "Duzina: ")
        self.sirinaLabel = Label(Input, text = "Sirina: ")
        self.visinaLabel = Label(Input, text = "Visina: ")
        self.brzinaLabel = Label(Input, text = "Max. brzina: ")
        self.godinaLabel = Label(Input, text = "God. proizv: ")
        self.prostorLabel = Label(Input, text = "Izloz. prostor: ")
        self.vrataLabel = Label(Input, text = "Broj vrata: ")
        self.sedistaLabel = Label(Input, text = "Broj sedista: ")
        self.menjacLabel = Label(Input, text = "Tip menjaca: ")
        
        self.opisEntry = Entry(Input)
        self.duzinaEntry = Entry(Input)
        self.sirinaEntry = Entry(Input)
        self.visinaEntry = Entry(Input)
        self.brzinaEntry = Entry(Input)
        self.godinaEntry = Entry(Input)
        
        ponudjenoProstora = []
        for i in Projekat().prostori:
            ponudjenoProstora.append(i.oznaka)
        izborProstora = StringVar()
        if (self.automobil.izlozbeni_prostor != None):
            izborProstora.set([s for s in ponudjenoProstora if self.automobil.izlozbeni_prostor.oznaka in s][0])
            self.prostorIzbor(izborProstora.get())
        else:
            izborProstora.set(ponudjenoProstora[0])
            self.prostorIzbor(izborProstora.get())

        self.prostorMenu = OptionMenu(Input, izborProstora, *ponudjenoProstora, command = lambda x: self.prostorIzbor(izborProstora.get()))
        
        self.vrataEntry = Entry(Input)
        self.sedistaEntry = Entry(Input)
        
        ponudjenoMenjaca = []
        for i in TipMenjaca:
            ponudjenoMenjaca.append(i.name)
        izborMenjaca = StringVar()
        if(self.automobil.tip_menjaca != None):
            izborMenjaca.set([s for s in ponudjenoMenjaca if self.automobil.tip_menjaca.name in s][0])
            self.menjacIzbor(izborMenjaca.get())
        else:
            izborMenjaca.set(ponudjenoMenjaca[0])
            self.menjacIzbor(izborMenjaca.get())            
        self.menjacMenu = OptionMenu(Input, izborMenjaca, *ponudjenoMenjaca, command = lambda x: self.menjacIzbor(izborMenjaca.get()))
        
        
        #napuni ostale vrednostima, ako se prosledi prazan student bice prazno
        self.opisEntry.insert(0, automobil.opis)
        self.duzinaEntry.insert(0, automobil.duzina)
        self.sirinaEntry.insert(0, automobil.sirina)
        self.visinaEntry.insert(0, automobil.visina)
        self.brzinaEntry.insert(0, automobil.maksimalna_brzina)
        self.godinaEntry.insert(0, automobil.godina_proizvodnje)
        self.vrataEntry.insert(0, automobil.broj_vrata)
        self.sedistaEntry.insert(0, automobil.broj_sedista)
       
        
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.AutomobilCU)
      
        #Pozicije
        self.opisLabel.grid(row = 1, sticky = E)#
        self.duzinaLabel.grid(row = 2, sticky = E)
        self.sirinaLabel.grid(row = 3, sticky = E)
        self.visinaLabel.grid(row = 4, sticky = E)
        self.brzinaLabel.grid(row = 5, sticky = E)
        self.godinaLabel.grid(row = 6, sticky = E)
        self.prostorLabel.grid(row = 7, sticky = E)
        self.vrataLabel.grid(row = 8, sticky = E)
        self.sedistaLabel.grid(row = 9, sticky = E)
        self.menjacLabel.grid(row = 10, sticky = E)
        
        
        self.opisEntry.grid(row = 1, column = 1)
        self.duzinaEntry.grid(row = 2, column = 1)
        self.sirinaEntry.grid(row = 3, column = 1)
        self.visinaEntry.grid(row = 4, column = 1)
        self.brzinaEntry.grid(row = 5, column = 1)
        self.godinaEntry.grid(row = 6, column = 1)
        self.prostorMenu.grid(row = 7, column = 1)
        self.vrataEntry.grid(row = 8, column = 1)
        self.sedistaEntry.grid(row = 9, column = 1)
        self.menjacMenu.grid(row = 10, column = 1)
        
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.grid(row = 2, column = 0, columnspan = 15, rowspan = 15, sticky = 'NESW' )
        
    
    def prostorIzbor(self, izbor):
        '''
        Metoda koja setuje vrednost atributa izlozbenog prostora na vrednost izabranu iz drop down menija 
        
        :param izbor: string vrednost oznake izlozbenog prostora
        '''
        self.izabraniProstor = izbor
    
    def menjacIzbor(self, izbor):
        '''
        Metoda koja setuje vrednost atributa tipa menjaca na vrednost izabranu iz drop down menija 
        
        :param izbor: string vrednost imena enumeracije tipa menjaca
        '''
        self.izabraniMenjac = izbor
        
        
    def AutomobilCU(self):
        '''
        Metoda koja se okida po kliku na potvrdiBTN dugme, koja odreduje koji tip operacije je forma radila i prema tome
        poziva metode kontrolera za perzistiranje i metode root view-a za osvezavanje pogleda.
        '''
        if self.operacija == Operacija.DODAVANJE:
             
            self.automobil.oznaka = a()
            self.automobil.opis = self.opisEntry.get()
            self.automobil.duzina = int(self.duzinaEntry.get())
            self.automobil.sirina = int(self.sirinaEntry.get())
            self.automobil.visina = int(self.visinaEntry.get())
            self.automobil.maksimalna_brzina = int(self.brzinaEntry.get())
            self.automobil.godina_proizvodnje = int(self.godinaEntry.get())
            self.automobil.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.automobil.broj_vrata = int(self.vrataEntry.get())
            self.automobil.broj_sedista = int(self.sedistaEntry.get())
            self.automobil.tip_menjaca = TipMenjaca[self.izabraniMenjac]
            
            #print(self.automobil)
            
            DodajAutomobil(self.automobil)
            
            self.glavni.OsveziAutomobile()
            
            #vidi ovo sta se desava, mozda destruktor eksplicitno
            self.withdraw()
            
            
        elif self.operacija == Operacija.IZMENA:
            #print(self.student)
            
            self.automobil.opis = self.opisEntry.get()
            self.automobil.duzina = int(self.duzinaEntry.get())
            self.automobil.sirina = int(self.sirinaEntry.get())
            self.automobil.visina = int(self.visinaEntry.get())
            self.automobil.maksimalna_brzina = int(self.brzinaEntry.get())
            self.automobil.godina_proizvodnje = int(self.godinaEntry.get())
            self.automobil.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.automobil.broj_vrata = int(self.vrataEntry.get())
            self.automobil.broj_sedista = int(self.sedistaEntry.get())
            self.automobil.tip_menjaca = TipMenjaca[self.izabraniMenjac]
            
            print(self.automobil)
            
            IzmeniAutomobil(self.automobil)
            
            self.glavni.OsveziAutomobile()
            
            self.withdraw()
            
class DzipCU(tk.Tk):
    '''
    Klasa koja opisuje view forme za insert i update nad entitetom dzip.
    Nasledjuje klasu TkInter
    '''
    def __init__(self, dzip, operacija, glavni):
        '''
        Constructor
        
        :param dzip: objekat dzipa koji se obradjuje (create - prazan, postojeci - update)
        :param operacija: enumeracija koja odredjuje da li se forma koristi za insert ili update
        :param glavni: referenca na root view koji ga poziva
        '''
        tk.Tk.__init__(self)
        
        
        
        tk.Tk.wm_title(self, "Dzip UD")
        tk.Tk.geometry(self, '220x300')
        self.resizable(False, False)
        Centriraj(self)
        
        self.dzip = dzip
        self.operacija = operacija
        
        #self.izabraniMenjac = self.automobil.tip_menjaca
        self.izabraniProstor = self.dzip.izlozbeni_prostor
       
        
        
        #referenca na glavni da se moze iskoristiti Osvezi
        self.glavni = glavni
        
        rows = 0
        while rows < 15:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        Input = Frame(self)
        
        #oznaka ce se kreirati sama i inkrementirati na odredjen nacin
        self.opisLabel = Label(Input, text = "Opis: ")
        self.duzinaLabel = Label(Input, text = "Duzina: ")
        self.sirinaLabel = Label(Input, text = "Sirina: ")
        self.visinaLabel = Label(Input, text = "Visina: ")
        self.brzinaLabel = Label(Input, text = "Max. brzina: ")
        self.godinaLabel = Label(Input, text = "God. proizv: ")
        self.prostorLabel = Label(Input, text = "Izloz. prostor: ")
        self.vrataLabel = Label(Input, text = "Broj vrata: ")
        self.pogonLabel = Label(Input, text = "Pogon 4x4: ")
        self.konjskihLabel = Label(Input, text = "Konjskih snaga: ")
        self.spustajucaKlupaLabel = Label(Input, text = "Spustajuca klupa: ")
        
        self.opisEntry = Entry(Input)
        self.duzinaEntry = Entry(Input)
        self.sirinaEntry = Entry(Input)
        self.visinaEntry = Entry(Input)
        self.brzinaEntry = Entry(Input)
        self.godinaEntry = Entry(Input)
        
        ponudjenoProstora = []
        for i in Projekat().prostori:
            ponudjenoProstora.append(i.oznaka)
        izborProstora = StringVar()
        if (self.dzip.izlozbeni_prostor != None):
            izborProstora.set([s for s in ponudjenoProstora if self.dzip.izlozbeni_prostor.oznaka in s][0])
            self.prostorIzbor(izborProstora.get())
        else:
            izborProstora.set(ponudjenoProstora[0])
            self.prostorIzbor(izborProstora.get())

        self.prostorMenu = OptionMenu(Input, izborProstora, *ponudjenoProstora, command = lambda x: self.prostorIzbor(izborProstora.get()))
        
        self.vrataEntry = Entry(Input)
        
        
        self.izborPogona = IntVar()
        #da checkbox oslikava vrednost propertija pri izmeni:
        vrednost = 1 if self.dzip.pogon_na_sva_cetiri_tocka == True else 0
        self.izborPogona.set(vrednost)
        self.pogonBox = Checkbutton(Input, variable = self.izborPogona, onvalue = 1, offvalue = 0)
        
        #self.izborPogona.trace('w', self.test)
           
        self.konjskihEntry = Entry(Input) 
        
        
        self.izborKlupe = IntVar()
        vrednost1 = 1 if self.dzip.spustajuca_zadnja_klupa == True else 0
        self.izborKlupe.set(vrednost1)
        self.klupaBox = Checkbutton(Input, variable = self.izborKlupe, onvalue = 1, offvalue = 0)
        
         
        #napuni ostale vrednostima, ako se prosledi prazan student bice prazno
        self.opisEntry.insert(0, dzip.opis)
        self.duzinaEntry.insert(0, dzip.duzina)
        self.sirinaEntry.insert(0, dzip.sirina)
        self.visinaEntry.insert(0, dzip.visina)
        self.brzinaEntry.insert(0, dzip.maksimalna_brzina)
        self.godinaEntry.insert(0, dzip.godina_proizvodnje)
        self.vrataEntry.insert(0, dzip.broj_vrata)
        self.konjskihEntry.insert(0, dzip.konjskih_snaga)
       
        
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.DzipCU)
      
        #Pozicije
        self.opisLabel.grid(row = 1, sticky = E)#
        self.duzinaLabel.grid(row = 2, sticky = E)
        self.sirinaLabel.grid(row = 3, sticky = E)
        self.visinaLabel.grid(row = 4, sticky = E)
        self.brzinaLabel.grid(row = 5, sticky = E)
        self.godinaLabel.grid(row = 6, sticky = E)
        self.prostorLabel.grid(row = 7, sticky = E)
        self.vrataLabel.grid(row = 8, sticky = E)
        self.pogonLabel.grid(row = 9, sticky = E)
        self.konjskihLabel.grid(row = 10, sticky = E)
        self.spustajucaKlupaLabel.grid(row = 11, sticky = E)
        
        
        self.opisEntry.grid(row = 1, column = 1)
        self.duzinaEntry.grid(row = 2, column = 1)
        self.sirinaEntry.grid(row = 3, column = 1)
        self.visinaEntry.grid(row = 4, column = 1)
        self.brzinaEntry.grid(row = 5, column = 1)
        self.godinaEntry.grid(row = 6, column = 1)
        self.prostorMenu.grid(row = 7, column = 1)
        self.vrataEntry.grid(row = 8, column = 1)
        self.pogonBox.grid(row = 9, column = 1)
        self.konjskihEntry.grid(row = 10, column = 1)
        self.klupaBox.grid(row = 11, column = 1)
        
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.grid(row = 2, column = 0, columnspan = 15, rowspan = 15, sticky = 'NESW' )
        
    '''
    def test(self, *args):
        print(self.izborPogona.get())
    '''
    
    def prostorIzbor(self, izbor):
        '''
        Metoda koja setuje vrednost atributa izlozbenog prostora na vrednost izabranu iz drop down menija 
        
        :param izbor: string vrednost oznake izlozbenog prostora
        '''
        self.izabraniProstor = izbor
    
        
    def DzipCU(self):
        '''
        Metoda koja se okida po kliku na potvrdiBTN dugme, koja odreduje koji tip operacije je forma radila i prema tome
        poziva metode kontrolera za perzistiranje i metode root view-a za osvezavanje pogleda.
        '''
        if self.operacija == Operacija.DODAVANJE:
             
            self.dzip.oznaka = dz()
            self.dzip.opis = self.opisEntry.get()
            self.dzip.duzina = int(self.duzinaEntry.get())
            self.dzip.sirina = int(self.sirinaEntry.get())
            self.dzip.visina = int(self.visinaEntry.get())
            self.dzip.maksimalna_brzina = int(self.brzinaEntry.get())
            self.dzip.godina_proizvodnje = int(self.godinaEntry.get())
            self.dzip.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.dzip.broj_vrata = int(self.vrataEntry.get())
            self.dzip.pogon_na_sva_cetiri_tocka = True if self.izborPogona.get() == 1 else False
            self.dzip.konjskih_snaga = int(self.konjskihEntry.get())
            self.dzip.spustajuca_zadnja_klupa = True if self.izborKlupe.get() == 1 else False
            
            print(self.izborPogona.get())
            print(self.izborKlupe.get())
            
            DodajDzip(self.dzip)
            
            self.glavni.OsveziDzipove()
            
            #vidi ovo sta se desava, mozda destruktor eksplicitno
            self.withdraw()
            
            
        elif self.operacija == Operacija.IZMENA:
            #print(self.student)
            
            self.dzip.opis = self.opisEntry.get()
            self.dzip.duzina = int(self.duzinaEntry.get())
            self.dzip.sirina = int(self.sirinaEntry.get())
            self.dzip.visina = int(self.visinaEntry.get())
            self.dzip.maksimalna_brzina = int(self.brzinaEntry.get())
            self.dzip.godina_proizvodnje = int(self.godinaEntry.get())
            self.dzip.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.dzip.broj_vrata = int(self.vrataEntry.get())
            self.dzip.pogon_na_sva_cetiri_tocka = True if self.izborPogona.get() == 1 else False
            self.dzip.konjskih_snaga = int(self.konjskihEntry.get())
            self.dzip.spustajuca_zadnja_klupa = True if self.izborKlupe.get() == 1 else False
            
            '''
            
            print("Pri izmeni:")
            print("Vrednost pogona i klupe posle")
            
            print("izbor pogona " + str(self.izborPogona.get()))
            print("izbor pogona " + str(self.izborKlupe.get()))
            
            print('Vrednost propertija')
            print(self.dzip.pogon_na_sva_cetiri_tocka)
            print(self.dzip.spustajuca_zadnja_klupa)
            
            '''
            
            
            IzmeniDzip(self.dzip)
            
            self.glavni.OsveziDzipove()
            
            self.withdraw()
            
            
class KvadCU(tk.Tk):
    '''
    Klasa koja opisuje view forme za insert i update nad entitetom kvad.
    Nasledjuje klasu TkInter
    '''
    def __init__(self, kvad, operacija, glavni):
        '''
        Constructor
        
        :param kvad: objekat kvada koji se obradjuje (create - prazan, postojeci - update)
        :param operacija: enumeracija koja odredjuje da li se forma koristi za insert ili update
        :param glavni: referenca na root view koji ga poziva
        '''
        
        tk.Tk.__init__(self)
        
        
        
        tk.Tk.wm_title(self, "Kvad UD")
        tk.Tk.geometry(self, '220x300')
        self.resizable(False, False)
        Centriraj(self)
        
        self.kvad = kvad
        self.operacija = operacija
        
        #self.izabraniMenjac = self.automobil.tip_menjaca
        self.izabraniProstor = self.kvad.izlozbeni_prostor
       
        
        
        #referenca na glavni da se moze iskoristiti Osvezi
        self.glavni = glavni
        
        rows = 0
        while rows < 15:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        Input = Frame(self)
        
        #oznaka ce se kreirati sama i inkrementirati na odredjen nacin
        self.opisLabel = Label(Input, text = "Opis: ")
        self.duzinaLabel = Label(Input, text = "Duzina: ")
        self.sirinaLabel = Label(Input, text = "Sirina: ")
        self.visinaLabel = Label(Input, text = "Visina: ")
        self.brzinaLabel = Label(Input, text = "Max. brzina: ")
        self.godinaLabel = Label(Input, text = "God. proizv: ")
        self.prostorLabel = Label(Input, text = "Izloz. prostor: ")
        self.pogonLabel = Label(Input, text = "Pogon 4x4: ")
        self.stvariLabel = Label(Input, text = "Prostor za stvari: ")
        
        
        self.opisEntry = Entry(Input)
        self.duzinaEntry = Entry(Input)
        self.sirinaEntry = Entry(Input)
        self.visinaEntry = Entry(Input)
        self.brzinaEntry = Entry(Input)
        self.godinaEntry = Entry(Input)
        
        ponudjenoProstora = []
        for i in Projekat().prostori:
            ponudjenoProstora.append(i.oznaka)
        izborProstora = StringVar()
        if (self.kvad.izlozbeni_prostor != None):
            izborProstora.set([s for s in ponudjenoProstora if self.kvad.izlozbeni_prostor.oznaka in s][0])
            self.prostorIzbor(izborProstora.get())
        else:
            izborProstora.set(ponudjenoProstora[0])
            self.prostorIzbor(izborProstora.get())

        self.prostorMenu = OptionMenu(Input, izborProstora, *ponudjenoProstora, command = lambda x: self.prostorIzbor(izborProstora.get()))
        
           
        self.izborPogona = IntVar()
        self.izborPogona.set(1 if self.kvad.pogon_na_sva_cetiri_tocka == True else 0)
        self.pogonBox = Checkbutton(Input, variable = self.izborPogona, onvalue = 1, offvalue = 0)
        
        
        self.izborStvari = IntVar()
        self.izborStvari.set(1 if self.kvad.prostor_za_stvari == True else 0)
        self.stvariBox = Checkbutton(Input, variable = self.izborStvari, onvalue = 1, offvalue = 0)
        
         
        #napuni ostale vrednostima, ako se prosledi prazan student bice prazno
        self.opisEntry.insert(0, kvad.opis)
        self.duzinaEntry.insert(0, kvad.duzina)
        self.sirinaEntry.insert(0, kvad.sirina)
        self.visinaEntry.insert(0, kvad.visina)
        self.brzinaEntry.insert(0, kvad.maksimalna_brzina)
        self.godinaEntry.insert(0, kvad.godina_proizvodnje)
        
       
        
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.KvadCU)
      
        #Pozicije
        self.opisLabel.grid(row = 1, sticky = E)#
        self.duzinaLabel.grid(row = 2, sticky = E)
        self.sirinaLabel.grid(row = 3, sticky = E)
        self.visinaLabel.grid(row = 4, sticky = E)
        self.brzinaLabel.grid(row = 5, sticky = E)
        self.godinaLabel.grid(row = 6, sticky = E)
        self.prostorLabel.grid(row = 7, sticky = E)
        self.pogonLabel.grid(row = 8, sticky = E)
        self.stvariLabel.grid(row = 9, sticky = E)
        
        
        self.opisEntry.grid(row = 1, column = 1)
        self.duzinaEntry.grid(row = 2, column = 1)
        self.sirinaEntry.grid(row = 3, column = 1)
        self.visinaEntry.grid(row = 4, column = 1)
        self.brzinaEntry.grid(row = 5, column = 1)
        self.godinaEntry.grid(row = 6, column = 1)
        self.prostorMenu.grid(row = 7, column = 1)
        self.pogonBox.grid(row = 8, column = 1)
        self.stvariBox.grid(row = 9, column = 1)
        
        
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.grid(row = 2, column = 0, columnspan = 15, rowspan = 15, sticky = 'NESW' )
        
    
    def prostorIzbor(self, izbor):
        '''
        Metoda koja setuje vrednost atributa izlozbenog prostora na vrednost izabranu iz drop down menija 
        
        :param izbor: string vrednost oznake izlozbenog prostora
        '''
        self.izabraniProstor = izbor
    
        
    def KvadCU(self):
        '''
        Metoda koja se okida po kliku na potvrdiBTN dugme, koja odreduje koji tip operacije je forma radila i prema tome
        poziva metode kontrolera za perzistiranje i metode root view-a za osvezavanje pogleda.
        '''
        if self.operacija == Operacija.DODAVANJE:
             
            self.kvad.oznaka = kv()
            self.kvad.opis = self.opisEntry.get()
            self.kvad.duzina = int(self.duzinaEntry.get())
            self.kvad.sirina = int(self.sirinaEntry.get())
            self.kvad.visina = int(self.visinaEntry.get())
            self.kvad.maksimalna_brzina = int(self.brzinaEntry.get())
            self.kvad.godina_proizvodnje = int(self.godinaEntry.get())
            self.kvad.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.kvad.pogon_na_sva_cetiri_tocka = True if self.izborPogona.get() == 1 else False
            self.kvad.prostor_za_stvari = True if self.izborStvari.get() == 1 else False
            
            
            DodajKvad(self.kvad)
            
            self.glavni.OsveziKvadove()
            
            #vidi ovo sta se desava, mozda destruktor eksplicitno
            self.withdraw()
            
            
        elif self.operacija == Operacija.IZMENA:
            #print(self.student)
            
            self.kvad.oznaka = kv()
            self.kvad.opis = self.opisEntry.get()
            self.kvad.duzina = int(self.duzinaEntry.get())
            self.kvad.sirina = int(self.sirinaEntry.get())
            self.kvad.visina = int(self.visinaEntry.get())
            self.kvad.maksimalna_brzina = int(self.brzinaEntry.get())
            self.kvad.godina_proizvodnje = int(self.godinaEntry.get())
            self.kvad.izlozbeni_prostor = prostorIzOznake(self.izabraniProstor)
            self.kvad.pogon_na_sva_cetiri_tocka = True if self.izborPogona.get() == 1 else False
            self.kvad.prostor_za_stvari = True if self.izborStvari.get() == 1 else False
            
           
            IzmeniKvad(self.kvad)
            
            self.glavni.OsveziKvadove()
            
            self.withdraw()
