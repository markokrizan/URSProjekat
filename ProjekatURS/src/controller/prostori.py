'''
Created on May 13, 2018

@author: freeman
'''
from model.singleton import Projekat
from model.salon import *
from util.pickleUnpickle import Pickle, UnPickle


def prostorIzOznake(oznaka):
    for i in Projekat().prostori:
        if i.oznaka == oznaka:
            return i
        
def generisiOznaku():
    brojac = 1
    for i in Projekat().prostori:
        brojac += 1
    oznaka = 'p' + str(brojac)
    return oznaka


def DodajProstor(prostor):
    Projekat().prostori.append(prostor)
    Pickle('prostori.bin', Projekat().prostori)

def IzmeniProstor(prostor):
    for i in Projekat().prostori:
        if i.oznaka == prostor.oznaka:
            i.opis = prostor.opis
            i.lokacija = prostor.lokacija
    Pickle('prostori.bin', Projekat().prostori)

def ObrisiProstor(oznaka):
    prostor_za_brisanje = None
    for i in Projekat().prostori:
        if i.oznaka == oznaka:
            prostor_za_brisanje = i
    Projekat().prostori.remove(prostor_za_brisanje)
    Pickle('prostori.bin', Projekat().prostori)
    

def nadjiProstore(kriterijum):
    trazeniProstori = []
    q = kriterijum.lower()
    if (kriterijum != ''):
        for i in Projekat().prostori:
            if(q in i.oznaka.lower() or q in i.opis.lower() or q in i.lokacija.lower()):
                trazeniProstori.append(i)
        return trazeniProstori
    
def vozila_prostora(prostor):
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
    putnicka = []
    vozila = vozila_prostora(prostor)
    for i in vozila:
        if isinstance(i, PutnickoVozilo):
            putnicka.append(i)
    return putnicka


def terenska_vozila_prostora(prostor):
    terenska = []
    vozila = vozila_prostora(prostor)
    for i in vozila:
        if isinstance(i, TerenskoVozilo):
            terenska.append(i)
    return terenska




    

    

