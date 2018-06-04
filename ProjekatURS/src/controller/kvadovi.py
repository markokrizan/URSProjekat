'''

Modul koji zadrzi metode kontrolera za entitet kvad.

@author: Aleksandar Rancic
'''

from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

def DodajKvad(kvad):
    '''
    Metoda koja prima objekat klase kvad, dodaje ga u kolekciju i perzistira je.
    
    :param kvad: objekat klase Kvad
    '''
    Projekat().kvadovi.append(kvad)
    Pickle('kvadovi.bin', Projekat().kvadovi)
    
def kvadIzOznake(oznaka):
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje vraca konkretan objekat klase Kvad.
    
    :param oznaka: string vrednost oznake
    '''
    for i in Projekat().kvadovi:
        if i.oznaka == oznaka:
            return i
        
def generisiOznaku():
    '''
    Metoda koja generise vrednost za atribut oznake objekata klase Kvad.
    
    '''
    brojac = 1
    for i in Projekat().kvadovi:
        brojac += 1
    oznaka = 'kv' + str(brojac)
    return oznaka

def IzmeniKvad(kvad):
    '''
    Metoda koja prima objekat klase kvad i na osnovu njenih vrednosti menja postojeci objekat u kolekciji
    i ponovo perzistira kolekciju.
    
    :param kvad: objekat klase Kvad
    '''
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
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje pronalazi konkretan objekat kvada i uklanja ga 
    iz kolekcije.
    
    :param oznaka: string vrednost oznake
    '''
    kvad_za_brisanje = None
    for i in Projekat().kvadovi:
        if i.oznaka == oznaka:
            kvad_za_brisanje = i
    Projekat().kvadovi.remove(kvad_za_brisanje)
    Pickle('kvadovi.bin', Projekat().kvadovi) 
    
    
def nadjiKvadove(kriterijum, pogon, prostor):
    '''
    Metoda koja prima string vrednost kriterijuma pretrege, vrednost postojanja pogona na sva 4 tocka i prostra za stvari
    i na osnovu njih vraca kolekciju konkretnih objekata klase Kvad koji predstavljaju rezultat pretrage.
    
    :param kriterijum: stirng vrednost kriterijuma pretrage
    :param pogon: bool vrednost postojanja pogona na sva 4 tocka
    :param prostor: bool vrednost postojanja prostora za stvari
    '''
    trazeniKvadovi = []
    q = str(kriterijum.lower())
    
    for i in Projekat().kvadovi:
        if((q in i.oznaka.lower() or q in str(i.opis.lower()) or q in str(i.duzina) or q in str(i.sirina) 
           or q in str(i.visina) or q in str(i.maksimalna_brzina) or q in str(i.godina_proizvodnje))
            and (pogon == i.pogon_na_sva_cetiri_tocka and prostor == i.prostor_za_stvari)):
            trazeniKvadovi.append(i)
    return trazeniKvadovi
    
def sortirajKvadove(kriterijum):
    '''
    Metoda koja prima string vrednost kriterijuma za sortiranje i na osnovu njega vraca sortirane kolekcije
    objkata kvadova prema vrednostima atributa koji su vezani za kriterijum.
    
    :param kriterijum: string vrednost kriterijuma sortiranja
    '''
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.maksimalna_brzina)
        return sortiranaKolekcija
    elif kriterijum == 'godina_proizvodnje':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.godina_proizvodnje)
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')
    
def prostor_kvada(kvad):
    '''
    Metoda koja prima objekat klase Kvad i vraca objekat izlozbenog prostora sa kojim je povezan.
    
    :param kvad: objekat klase Kvad
    '''
    return kvad.izlozbeni_prostor
    

