'''
Created on May 12, 2018

@author: freeman
'''

from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

#Prostori:
def DodajProstor(prostor):
    Projekat().prostori.append(prostor)
    Pickle('prostori.bin', Projekat().prostori)

def IzmeniProstor(prostor):
    for i in Projekat().prostori:
        if i.oznaka == prostor.oznaka:
            i.opis = prostor.opis
            i.duzina = prostor.duzina
            i.sirina = prostor.sirina
            i.visina = prostor.visina
            i.lokacija = prostor.lokacija
    Pickle('prostori.bin', Projekat().prostori)
            
#Automobili:
def DodajAutomobil(automobil):
    Projekat().automobili.append(automobil)
    Pickle('automobili.bin', Projekat().automobil)

def IzmeniAutomobil(automobil):
    for i in Projekat().automobili:
        if i.oznaka == automobil.oznaka:
            i.opis = automobil.opis
            i.duzina = automobil.duzina
            i.sirina = automobil.sirina
            i.visina = automobil.visina
            i.maksimalna_brzina = automobil.maksimalna_brzina
            i.godina_proizvodnje = automobil.godina_proizvodnje
            i.izlozbeni_prostor = automobil.izlozbeni_prostor
            i.broj_vrata = automobil.broj_vrata
            i.broj_sedista = automobil.broj_sedista
    Pickle('automobili.bin', Projekat().automobili)
            
            
        
#Dzipovi:
def DodajDzip(dzip):
    Projekat().dzipovi.append(dzip)
    Pickle('dzipovi.bin', Projekat().dzipovi)

def IzmeniDzip(dzip):
    for i in Projekat().dzipovi:
        if i.oznaka == dzip.oznaka:
            i.opis = dzip.opis
            i.duzina = dzip.duzina
            i.sirina = dzip.sirina
            i.visina = dzip.visina
            i.maksimalna_brzina = dzip.maksimalna_brzina
            i.godina_proizvodnje = dzip.godina_proizvodnje
            i.izlozbeni_prostor = dzip.izlozbeni_prostor
            i.broj_vrata = dzip.broj_vrata
            i.pogon_na_sva_cetiri_tocka = dzip.pogon_na_sva_cetiri_tocka
            i.konjskih_snaga = dzip.konjskih_snaga 
            i.spustajuca_zadnja_klupa = dzip.spustajuca_zadnja_klupa
    Pickle('dzipovi.bin', Projekat().dzipovi)        
            

#Kvadovi:
def DodajKvad(kvad):
    Projekat().kvadovi.append(kvad)
    Pickle('kvadovi.bin', Projekat().kvadovi)

def IzmeniKvad(kvad):
    for i in Projekat().kvadovi:
        if i.oznaka == kvad.oznaka:
            i.opis = kvad.opis
            i.duzina = kvad.duzina
            i.sirina = kvad.sirina
            i.visina = kvad.visina
            i.maksimalna_brzina = kvad.maksimalna_brzina
            i.godina_proizvodnje = kvad.godina_proizvodnje
            i.izlozbeni_prostor = kvad.izlozbeni_prostor
            i.pogon_na_sva_cetiri_tocka = kvad.pogon_na_sva_cetiri_tocka
            i.prostor_za_stvari = kvad.prostor_za_stvari
    Pickle('kvadovi.bin', Projekat().kvadovi)  
    




if __name__ == '__main__':
    pass