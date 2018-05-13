'''
Created on May 13, 2018

@author: freeman
'''
from model.singleton import Projekat
from model.salon import *
from util.pickleUnpickle import Pickle, UnPickle


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
        if i.izlozbeni_prostor.__eq__(prostor):
            vozila.append(i)
    for i in Projekat().dzipovi:
        if i.izlozbeni_prostor.__eq__(prostor):
            vozila.append(i)
    for i in Projekat().kvadovi:
        if i.izlozbeni_prostor.__eq__(prostor):
            vozila.append(i)
    return vozila
    
    
    

def najbrza_vozila(prostor):
    najbrza_vozila = []
    vozila = vozila_prostora(prostor)
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




    

    

