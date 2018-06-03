'''
Created on Jun 1, 2018

@author: Freeman
'''

from tkinter import *
from tkinter import ttk

from controller.prostori import prostorIzOznake, vozila_prostora,\
    putnicka_vozila_prostora, terenska_vozila_prostora, najbrza_vozila,\
    tipVozila
from model.singleton import Projekat
import tkinter as tk
from view.gui_utils import Centriraj
from controller import prostori

from view.detaljiDzipovi import DetaljiDzipovi
from view.detaljiKvadovi import DetaljiKvadovi
#from view.detaljiAutomobili import DetaljiAutomobili
import view.detaljiAutomobili

class DetaljiProstor(tk.Tk):
    def __init__(self, glavni, oznakaProstora):
        
        
        self.prostor = prostorIzOznake(oznakaProstora)
        self.glavni = glavni
        
        #povuci glavni da ne moze da se petlja:
        self.glavni.withdraw()
               
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Detalji")
        tk.Tk.geometry(self, '800x600')
       
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
            
        #KOMPONENTE:
        
        #Notebook:
        self.nb = ttk.Notebook(self)
        self.nb.grid(row = 1, column = 0, columnspan = 50, rowspan = 49, sticky = 'NESW' )
       
       
        #PAGE Vozila:
        pageVozila = ttk.Frame(self.nb)
        
        #definisi grid za svaku od kartica
        rowsp1 = 0
        
        while rowsp1 < 50:
            pageVozila.rowconfigure(rowsp1, weight = 1)
            pageVozila.columnconfigure(rowsp1, weight = 1)
            rowsp1 += 1
            
        # ------------------------------------------------------------
        #Page izlozbeni prostori komponente
        
        #Tree Prostori
        self.treeVozila = ttk.Treeview(pageVozila, columns=("size", "modified"))
        self.treeVozila["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeVozila.column("Oznaka")
        self.treeVozila.column("Opis")
        self.treeVozila.column("Izlozbeni prostor")
        
        self.treeVozila.heading("Oznaka", text="Oznaka")
        self.treeVozila.heading("Opis", text="Opis")
        self.treeVozila.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        self.treeVozila.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        
        ButtonBarVozila = Frame(pageVozila)
        
        detaljiVozilaBTN = Button(ButtonBarVozila, text = "Detalji", command = self.Detalji)
        detaljiVozilaBTN.pack(side = LEFT, padx=1, pady=1)
    
        
        
        
        ButtonBarVozila.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        #**********************************************************************************  
        #Dodavanje izlozbeni prostori page u notebook  
        self.nb.add(pageVozila, text = "Vozila") 
        
        
        #PAGE Putnicka:
        pagePutnicka = ttk.Frame(self.nb)
        
        #definisi grid za svaku od kartica
        rowsp2 = 0
        
        while rowsp2 < 50:
            pagePutnicka.rowconfigure(rowsp2, weight = 1)
            pagePutnicka.columnconfigure(rowsp2, weight = 1)
            rowsp2 += 1
            
        # ------------------------------------------------------------
        #Page izlozbeni prostori komponente
        
        #Tree Prostori
        self.treePutnicka = ttk.Treeview(pagePutnicka, columns=("size", "modified"))
        self.treePutnicka["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treePutnicka.column("Oznaka")
        self.treePutnicka.column("Opis")
        self.treePutnicka.column("Izlozbeni prostor")
        
        self.treePutnicka.heading("Oznaka", text="Oznaka")
        self.treePutnicka.heading("Opis", text="Opis")
        self.treePutnicka.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        self.treePutnicka.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        
        ButtonBarPutnicka = Frame(pagePutnicka)
        
        detaljiPutnickaBTN = Button(ButtonBarPutnicka, text = "Detalji", command = self.Detalji)
        detaljiPutnickaBTN.pack(side = LEFT, padx=1, pady=1)
    
        
        
        
        ButtonBarPutnicka.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        #**********************************************************************************  
        #Dodavanje izlozbeni prostori page u notebook  
        self.nb.add(pagePutnicka, text = "Putnicka") 
        
        
        
        #PAGE Terenska:
        pageTerenska = ttk.Frame(self.nb)
        
        #definisi grid za svaku od kartica
        rowsp3 = 0
        
        while rowsp3 < 50:
            pageTerenska.rowconfigure(rowsp3, weight = 1)
            pageTerenska.columnconfigure(rowsp3, weight = 1)
            rowsp3 += 1
            
        # ------------------------------------------------------------
        #Page izlozbeni prostori komponente
        
        #Tree Prostori
        self.treeTerenska = ttk.Treeview(pageTerenska, columns=("size", "modified"))
        self.treeTerenska["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeTerenska.column("Oznaka")
        self.treeTerenska.column("Opis")
        self.treeTerenska.column("Izlozbeni prostor")
        
        self.treeTerenska.heading("Oznaka", text="Oznaka")
        self.treeTerenska.heading("Opis", text="Opis")
        self.treeTerenska.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        self.treeTerenska.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        
        ButtonBarTerenska = Frame(pageTerenska)
        
        detaljiTerenskaBTN = Button(ButtonBarTerenska, text = "Detalji", command = self.Detalji)
        detaljiTerenskaBTN.pack(side = LEFT, padx=1, pady=1)
    
        
        
        
        ButtonBarTerenska.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        #**********************************************************************************  
        #Dodavanje izlozbeni prostori page u notebook  
        self.nb.add(pageTerenska, text = "Terenska")
        
        
        
         #PAGE Najbrza:
        pageNajbrza = ttk.Frame(self.nb)
        
        #definisi grid za svaku od kartica
        rowsp4 = 0
        
        while rowsp4 < 50:
            pageNajbrza.rowconfigure(rowsp4, weight = 1)
            pageNajbrza.columnconfigure(rowsp4, weight = 1)
            rowsp4 += 1
            
        # ------------------------------------------------------------
        #Page izlozbeni prostori komponente
        
        #Tree Prostori
        self.treeNajbrza = ttk.Treeview(pageNajbrza, columns=("size", "modified"))
        self.treeNajbrza["columns"] = ( "Oznaka", "Opis", "Izlozbeni prostor")
        
        self.treeNajbrza.column("Oznaka")
        self.treeNajbrza.column("Opis")
        self.treeNajbrza.column("Izlozbeni prostor")
        
        self.treeNajbrza.heading("Oznaka", text="Oznaka")
        self.treeNajbrza.heading("Opis", text="Opis")
        self.treeNajbrza.heading("Izlozbeni prostor", text="Izlozbeni prostor")
        
        self.treeNajbrza.grid(row = 3, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        
        ButtonBarNajbrza = Frame(pageNajbrza)
        
        detaljiNajbrzaBTN = Button(ButtonBarNajbrza, text = "Detalji", command = self.Detalji)
        detaljiNajbrzaBTN.pack(side = LEFT, padx=1, pady=1)
    
        
        
        
        ButtonBarNajbrza.grid(row = 19, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        #**********************************************************************************  
        #Dodavanje izlozbeni prostori page u notebook  
        self.nb.add(pageNajbrza, text = "Najbrza")
           
           
           
           
        self.NapuniVozila()
        self.NapuniPutnicka()
        self.NapuniTerenska()  
        self.NapuniNajbrza()  
           
            
        #---------------------------------------------    
        self.protocol( "WM_DELETE_WINDOW", self.quit )   
            
            
    def quit(self):
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()  
        
    def NapuniVozila(self):
        vozila = vozila_prostora(self.prostor)
        for index, i in enumerate(vozila):
            self.treeVozila.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
      
    def NapuniPutnicka(self):
        putnicka = putnicka_vozila_prostora(self.prostor)
        for index, i in enumerate(putnicka):
            self.treePutnicka.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def NapuniTerenska(self):
        terenska = terenska_vozila_prostora(self.prostor)
        for index, i in enumerate(terenska):
            self.treeTerenska.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
    
    def NapuniNajbrza(self):
        najbrza = najbrza_vozila(self.prostor)
        if najbrza != None:
            for index, i in enumerate(najbrza):
                self.treeNajbrza.insert("", 'end' ,text = index + 1, values = (i.oznaka, i.opis, i.izlozbeni_prostor.oznaka))
            
    def Detalji(self):
        trenutniTab = self.nb.index("current")
        if (trenutniTab == 0):
            try:
                selektovani = self.treeVozila.selection()[0]
                oznaka= self.treeVozila.item(selektovani)['values'][0]
                if (tipVozila(self.prostor, oznaka) == 'automobil'):
                    view.detaljiAutomobili.DetaljiAutomobili(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'dzip'):
                    DetaljiDzipovi(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'kvad'):
                    DetaljiKvadovi(self,oznaka)
                
            except IndexError:
                messagebox.showerror("Greska", "Nista nije selektovano")
        elif(trenutniTab == 1):
            try:
                selektovani = self.treePutnicka.selection()[0]
                oznaka = self.treePutnicka.item(selektovani)['values'][0]
                if (tipVozila(self.prostor, oznaka) == 'automobil'):
                    view.detaljiAutomobili.DetaljiAutomobili(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'dzip'):
                    DetaljiDzipovi(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'kvad'):
                    DetaljiKvadovi(self,oznaka)
            except IndexError:
                messagebox.showerror("Greska", "Nista nije selektovano")
        elif(trenutniTab == 2):
            try:
                selektovani = self.treeTerenska.selection()[0]
                oznaka = self.treeTerenska.item(selektovani)['values'][0]
                if (tipVozila(self.prostor, oznaka) == 'automobil'):
                    view.detaljiAutomobili.DetaljiAutomobili(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'dzip'):
                    DetaljiDzipovi(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'kvad'):
                    DetaljiKvadovi(self,oznaka)
            except IndexError:
                messagebox.showerror("Greska", "Nista nije selektovano")
        elif(trenutniTab == 3):
            try:
                selektovani = self.treeNajbrza.selection()[0]
                oznaka = self.treeNajbrza.item(selektovani)['values'][0]
                if (tipVozila(self.prostor, oznaka) == 'automobil'):
                    view.detaljiAutomobili.DetaljiAutomobili(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'dzip'):
                    DetaljiDzipovi(self, oznaka)
                elif(tipVozila(self.prostor, oznaka) == 'kvad'):
                    DetaljiKvadovi(self,oznaka)
            except IndexError:
                messagebox.showerror("Greska", "Nista nije selektovano")
 
                
class ProstorInfo(tk.Tk):
    def __init__(self, glavni, oznakaProstora):
        
        
        self.prostor = prostorIzOznake(oznakaProstora)
        self.glavni = glavni
        
        #povuci glavni da ne moze da se petlja:
        self.glavni.withdraw()
               
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Prostor")
        tk.Tk.geometry(self, '200x150')
       
        self.resizable(False, False)
        Centriraj(self)
        
        #self.korisnik = korisnik
       
       #definisi grid prozora, dosta korisno
       #50*50
        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
            
        self.l1 = Label(self, text="Oznaka: " + self.prostor.oznaka)
        self.l2 = Label(self, text="Opis: " + self.prostor.opis)
        self.l3 = Label(self, text="Lokacija: " + self.prostor.lokacija)
        
        self.l1.grid(row = 1, columnspan = 10, sticky = 'NESW')
        self.l2.grid(row = 2, columnspan = 10, sticky = 'NESW')
        self.l3.grid(row = 4, columnspan = 10, sticky = 'NESW')
        
        self.protocol( "WM_DELETE_WINDOW", self.quit )
        
    def quit(self):
        #print("prozor zatvoren")
        self.glavni.deiconify()
        self.destroy()
        
       
        