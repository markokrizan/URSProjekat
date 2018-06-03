'''
Created on May 13, 2018

@author: freeman
'''

from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

def DodajKvad(kvad):
    Projekat().kvadovi.append(kvad)
    Pickle('kvadovi.bin', Projekat().kvadovi)
    
def kvadIzOznake(oznaka):
    for i in Projekat().kvadovi:
        if i.oznaka == oznaka:
            return i
        
def generisiOznaku():
    brojac = 1
    for i in Projekat().kvadovi:
        brojac += 1
    oznaka = 'kv' + str(brojac)
    return oznaka

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
    
def ObrisiKvad(oznaka):
    kvad_za_brisanje = None
    for i in Projekat().kvadovi:
        if i.oznaka == oznaka:
            kvad_za_brisanje = i
    Projekat().kvadovi.remove(kvad_za_brisanje)
    Pickle('kvadovi.bin', Projekat().kvadovi) 
    
    
def nadjiKvadove(kriterijum, pogon, prostor):
    trazeniKvadovi = []
    q = kriterijum.lower()
    if (kriterijum != ''):
        for i in Projekat().kvadovi:
            if(q in i.oznaka.lower() or q in i.opis.lower() or int(q) == i.__duzina or int(q) == i.sirina 
               or int(q) == i.__visina or int(q) == i.maksimalna_brzina or q in str(i.godina_proizvodnje)
                or pogon == i.pogon_na_sva_cetiri_tocka or prostor == i.prostor_za_stvari):
                trazeniKvadovi.append(i)
        return trazeniKvadovi
    
def sortirajKvadove(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'godina_proizvodnje':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.godina_proizvodnje.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')
    
def prostor_kvada(kvad):
    return kvad.izlozbeni_prostor
    

