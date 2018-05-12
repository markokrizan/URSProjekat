'''
Created on May 12, 2018

@author: freeman
'''
from model.singleton import Projekat

#Automobili:
def sortirajAutomobile(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'broj_sedista':
        sortiranaKolekcija = sorted(Projekat().automobili, key=lambda x: x.broj_sedista.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum') 
    
    
def sortirajDzipove(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'konjskih_snaga':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.konjskih_snaga.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')   

def sortirajKvadove(kriterijum):
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.maksimalna_brzina.lower())
        return sortiranaKolekcija
    elif kriterijum == 'godina_proizvodnje':
        sortiranaKolekcija = sorted(Projekat().kvadovi, key=lambda x: x.godina_proizvodnje.lower())
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')
    





if __name__ == '__main__':
    pass