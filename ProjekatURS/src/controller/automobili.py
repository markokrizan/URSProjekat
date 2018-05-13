'''
Created on May 13, 2018

@author: freeman
'''
from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

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
    
def nadjiAutomobile(kriterijum):
    trazeniAutomobili = []
    q = kriterijum.lower()
    if (kriterijum != ''):
        for i in Projekat().automobili:
            if(q in i.oznaka.lower() or q in i.opis.lower() or int(q) == i.__duzina or int(q) == i.sirina 
               or int(q) == i.__visina or int(q) == i.maksimalna_brzina or q in str(i.godina_proizvodnje) or int(q) == i.broj_vrata
                or int(q) == i.broj_sedista or q in str(i.tip_menjaca.name)):
                trazeniAutomobili.append(i)
        return trazeniAutomobili
    
    
def sortirajAutomobile(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'broj_sedista':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.broj_sedista.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum') 
    

def prostor_automobila(automobil):
    return automobil.izlozbeni_prostor
    

    
    
    
    
    