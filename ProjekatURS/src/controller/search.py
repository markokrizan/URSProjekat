'''
Created on May 12, 2018

@author: freeman
'''
from model.singleton import Projekat

def nadjiProstore(kriterijum):
    trazeniProstori = []
    q = kriterijum.lower()
    if (kriterijum != ''):
        for i in Projekat().prostori:
            if(q in i.oznaka.lower() or q in i.opis.lower() or q in i.lokacija.lower()):
                trazeniProstori.append(i)
        return trazeniProstori
                
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



if __name__ == '__main__':
    pass