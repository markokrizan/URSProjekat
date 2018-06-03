'''
Created on May 13, 2018

@author: freeman
'''

from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

def DodajDzip(dzip):
    Projekat().dzipovi.append(dzip)
    Pickle('dzipovi.bin', Projekat().dzipovi)
    
def dzipIzOznake(oznaka):
    for i in Projekat().dzipovi:
        if i.oznaka == oznaka:
            return i

def generisiOznaku():
    brojac = 1
    for i in Projekat().dzipovi:
        brojac += 1
    oznaka = 'dz' + str(brojac)
    return oznaka

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
    
def ObrisiDzip(oznaka):
    dzip_za_brisanje = None
    for i in Projekat().dzipovi:
        if i.oznaka == oznaka:
            dzip_za_brisanje = i
    Projekat().dzipovi.remove(dzip_za_brisanje)
    Pickle('dzipovi.bin', Projekat().dzipovi)
    
def nadjiDzipove(kriterijum, pogon, zadnja_klupa):
    trazeniDzipovi = []
    q = kriterijum.lower()
    #pogon i zadnja klpua?
    if (kriterijum != ''):
        for i in Projekat().dzipovi:
            if(q in i.oznaka.lower() or q in i.opis.lower() or int(q) == i.__duzina or int(q) == i.sirina 
               or int(q) == i.__visina or int(q) == i.maksimalna_brzina or q in str(i.godina_proizvodnje) or int(q) == i.konjskih_snaga
                or pogon == i.pogon_na_sva_cetiri_tocka or zadnja_klupa == i.spustajuca_zadnja_klupa):
                trazeniDzipovi.append(i)
        return trazeniDzipovi
    
    
def sortirajDzipove(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'konjskih_snaga':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.konjskih_snaga.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')
    
def prostor_dzipa(dzip):
    return dzip.izlozbeni_prostor
