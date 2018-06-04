'''

Modul koji zadrzi metode kontrolera za entitet izlozbeni prostor.

@author: Marko Krizan
'''
from model.singleton import Projekat
from model.salon import *
from util.pickleUnpickle import Pickle, UnPickle


def prostorIzOznake(oznaka):
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje vraca konkretan objekat klase IzlozbeniProstor
    
    :param oznaka: string vrednost oznake
    '''
    for i in Projekat().prostori:
        if i.oznaka == oznaka:
            return i
        
def generisiOznaku():
    '''
    Metoda koja generise vrednost koja ce se koristit za atribut oznake objekta klase IzlozbeniProstor
    '''
    brojac = 1
    for i in Projekat().prostori:
        brojac += 1
    oznaka = 'p' + str(brojac)
    return oznaka


def DodajProstor(prostor):
    '''
    Metoda koja prima objekat klase izlozbeni prostor, dodaje ga u kolekciju i perzistira ga.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    Projekat().prostori.append(prostor)
    Pickle('prostori.bin', Projekat().prostori)

def IzmeniProstor(prostor):
    '''
    Metoda koja prima objekat klase izlozbeni prostori koristi njegove vrednosti da izmeni postojeci objekat u kolekciji.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    for i in Projekat().prostori:
        if i.oznaka == prostor.oznaka:
            i.opis = prostor.opis
            i.lokacija = prostor.lokacija
    Pickle('prostori.bin', Projekat().prostori)

def ObrisiProstor(oznaka):
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje vraca nalazi konkretan objekat u kolekciji, uklanja ga
    i ponovo perzistira kolekciju.
    
    :param oznaka: string vrednost oznake
    '''
    prostor_za_brisanje = None
    for i in Projekat().prostori:
        if i.oznaka == oznaka:
            prostor_za_brisanje = i
    Projekat().prostori.remove(prostor_za_brisanje)
    Pickle('prostori.bin', Projekat().prostori)
    

def nadjiProstore(kriterijum):
    '''
    Metoda koja na osnovu proslednjenog kriterijuma pronalazi objekte iz kolekcije prostora i vraca ih
    da budu korisceni kao rezultat pretrage.
    
    :param kriterijum: string vrednost kriterijuma po kojem ce se vrsiti pretraga
    '''
    trazeniProstori = []
    q = kriterijum.lower()
    if (kriterijum != ''):
        for i in Projekat().prostori:
            if(q in i.oznaka.lower() or q in i.opis.lower() or q in i.lokacija.lower()):
                trazeniProstori.append(i)
        return trazeniProstori
    
def vozila_prostora(prostor):
    '''
    Metoda koja vraca sva vozila prosledjenog objekta klase IzlozbeniProstor.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    vozila = []
    for i in Projekat().automobili:
        #if i.izlozbeni_prostor.__eq__(prostor):
        if i.izlozbeni_prostor.oznaka == prostor.oznaka:
            vozila.append(i)
    for i in Projekat().dzipovi:
        if i.izlozbeni_prostor.oznaka == prostor.oznaka:
            vozila.append(i)
    for i in Projekat().kvadovi:
        if i.izlozbeni_prostor.oznaka == prostor.oznaka:
            vozila.append(i)
    return vozila
    

def tipVozila(prostor, oznakaVozila):
    '''
    Metoda koja za proslednjeni prostor i oznaku vozila vraca kojeg je tipa objekat klase cija se oznaka prosledila.
    
    :param prostor: objekat klase IzlozbeniProstor
    :param oznakaVozila: string vrednost atributa oznake objekta klase Automobil
    '''
    vozila = vozila_prostora(prostor)
    for i in vozila:
        if i.oznaka == oznakaVozila:
            if isinstance(i, Automobil):
                return "automobil"
            elif isinstance(i, Dzip):
                return "dzip"
            elif isinstance(i, Kvad):
                return "kvad"
    

def najbrza_vozila(prostor):
    '''
    Metoda koja za proslednjeni prostor vraca kolekciju vozila tog prostora sa najvecom brzinom,
    tj. najvecom vrednosti atributa maksimalna_brzina.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    najbrza_vozila = []
    vozila = vozila_prostora(prostor)
    if len(vozila) != 0:
        maksimalna_brzina = max(object.maksimalna_brzina for object in vozila)
        #najbrze = max(vozila, key=lambda item: item.maksimalna_brzina)
        for i in vozila:
            if i.maksimalna_brzina == maksimalna_brzina:
                najbrza_vozila.append(i)
        
        return najbrza_vozila

    
def putnicka_vozila_prostora(prostor):
    '''
    Metoda koja za proslednjeni prostor vraca kolekciju vozila koja su putnicka,
    tj. su instance klase PutnickoVozilo.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    putnicka = []
    vozila = vozila_prostora(prostor)
    for i in vozila:
        if isinstance(i, PutnickoVozilo):
            putnicka.append(i)
    return putnicka


def terenska_vozila_prostora(prostor):
    '''
    Metoda koja za proslednjeni prostor vraca kolekciju vozila koja su terenska,
    tj. su instance klase TerenskoVozilo.
    
    :param prostor: objekat klase IzlozbeniProstor
    '''
    terenska = []
    vozila = vozila_prostora(prostor)
    for i in vozila:
        if isinstance(i, TerenskoVozilo):
            terenska.append(i)
    return terenska




    

    

