'''

Modul koji zadrzi metode kontrolera za entitet automobil.

@author: Aleksandar Rancic
'''
from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

def DodajAutomobil(automobil):
    '''
    Metoda koja prima objekat klase automobil, smesta ga u kolekciju i perzistira.
    
    :param automobil: objekat klase automobil
    '''
    Projekat().automobili.append(automobil)
    Pickle('automobili.bin', Projekat().automobili)
    
def automobilIzOznake(oznaka):
    '''
    Metoda koja prima string vrednost atributa oznake i na osnovu nje u kolekciji
    pronalazi konkretan objekat klase automobil i vraca ga.
    
    :param oznaka: string vrednost atributa oznake
    '''
    for i in Projekat().automobili:
        if i.oznaka == oznaka:
            return i

def generisiOznaku():
    '''
    Metoda koja generise string koji ce se koristit kao atribut oznake objekta klase automobil.
    
    '''
    brojac = 1
    for i in Projekat().automobili:
        brojac += 1
    oznaka = 'a' + str(brojac)
    return oznaka

def IzmeniAutomobil(automobil):
    '''
    Metoda koja prima objekat klase automobil i koristi njegove vrednosti da izmeni vec postojeci objekat
    u kolekciji.
    
    :param automobil: objekat klase automobil
    '''
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
            i.tip_menjaca = automobil.tip_menjaca
    Pickle('automobili.bin', Projekat().automobili)

def ObrisiAutomobil(oznaka):
    '''
    Metoda koja prima string vrednost atributa oznake i na osnovu nje u kolekciji
    pronalazi konkretan objekat klase automobil uklanja ga i ponovo perzistira kolekciju.
    
    :param oznaka: string vrednost atributa oznake
    '''
    automobil_za_brisanje = None
    for i in Projekat().automobili:
        if i.oznaka == oznaka:
            automobil_za_brisanje = i
    Projekat().automobili.remove(automobil_za_brisanje)
    Pickle('automobili.bin', Projekat().automobili)
    
def nadjiAutomobile(kriterijum):
    '''
    Metoda koja na osnovu proslednjenog kriterijuma pronalazi objekte iz kolekcije automobila i vraca ih
    da budu korisceni kao rezultat pretrage.
    
    :param kriterijum: string vrednost kriterijuma po kojem ce se vrsiti pretraga
    '''
    if(kriterijum is None):
        raise ValueError("Kriterijum ne sme biti nedefinisan")
    trazeniAutomobili = []
    q = str(kriterijum).lower()
    if (kriterijum != ''):
        for i in Projekat().automobili:
            if(q in i.oznaka.lower() or q in str(i.opis.lower()) or q in str(i.duzina) or q in str(i.sirina) 
               or q in str(i.visina) or q in str(i.maksimalna_brzina) or q in str(i.godina_proizvodnje) or q in str(i.broj_vrata)
                or q in str(i.broj_sedista) or q in str(i.tip_menjaca.name)):
                trazeniAutomobili.append(i)
        return trazeniAutomobili
    
    
def sortirajAutomobile(kriterijum):
    '''
    Metoda koja na osnovu proslednjenog kriterijuma sortira kompletnu kolekciju automobila po 
    rastucem poretku u odnosu na vrednost atributa koji je u vezi za kriterijumom.
    
    :param kriterijum: string vrednost kriterijuma po kojem ce se vrsiti pretraga
    '''
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.maksimalna_brzina)
        return sortiranaKolekcija
    elif kriterijum == 'broj_sedista':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.broj_sedista)
        return sortiranaKolekcija
    else:
        raise ValueError('Nepostojeci ili nedefinisani kriterijum') 
    

def prostor_automobila(automobil):
    '''
    Metoda koja prima objekat klase automobil i koristi njegove vrednosti da izmeni vec postojeci objekat
    u kolekciji.
    
    :param automobil: objekat klase automobil
    '''
    if (automobil != None):
        return automobil.izlozbeni_prostor
    

    
    
    
    
    