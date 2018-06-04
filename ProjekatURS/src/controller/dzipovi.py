'''

Modul koji zadrzi metode kontrolera za entitet dzip.

@author: Marko Krizan
'''

from model.singleton import Projekat
from util.pickleUnpickle import Pickle, UnPickle

def DodajDzip(dzip):
    '''
    Metoda koja prima objekat klase dzip, smesta ga u kolekciju i perzistira.
    
    :param dzip: objekat klase Dzip
    '''
    Projekat().dzipovi.append(dzip)
    Pickle('dzipovi.bin', Projekat().dzipovi)
    
def dzipIzOznake(oznaka):
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje vraca konkretan objekat klase Dzip.
    
    :param oznaka: string vrednost oznake
    '''
    for i in Projekat().dzipovi:
        if i.oznaka == oznaka:
            return i

def generisiOznaku():
    '''
    Metoda koja generise vrednost za atribut oznake objekta.
    
    '''
    brojac = 1
    for i in Projekat().dzipovi:
        brojac += 1
    oznaka = 'dz' + str(brojac)
    return oznaka

def IzmeniDzip(dzip):
    '''
    Metoda koja prima objekat klase dzip i koristi njegove vrednosti da izmeni postojeci objekat u kolekciji.
    
    :param dzip: objekat klase Dzip
    '''
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
    '''
    Metoda koja prima string vrednost oznake i na osnovu nje vraca pronalazi objekat dzipa u kolekciji i
    uklanja ga.
    
    :param oznaka: string vrednost oznake
    '''
    dzip_za_brisanje = None
    for i in Projekat().dzipovi:
        if i.oznaka == oznaka:
            dzip_za_brisanje = i
    Projekat().dzipovi.remove(dzip_za_brisanje)
    Pickle('dzipovi.bin', Projekat().dzipovi)
    
def nadjiDzipove(kriterijum, pogon, zadnja_klupa):
    '''
    Metoda koja prima string vrednost oznake, pogona na sva 4 tocka i spustajuce zadnje klupe i na osnovu njih
    vraca kolekciju konkretnih objekata koje se koriste kao rezultat pretrage.
    
    :param kriterijum: string vrednost kriterijuma pretrage
    :param pogon: bool vrednost postojanja pogona na sva 4 tocka
    :param zadnja_klupa: bool vrednost postojanja spustajuce zadnje klupe
    '''
    trazeniDzipovi = []
    q = str(kriterijum.lower())
    #pogon i zadnja klpua?
    for i in Projekat().dzipovi:
        if((q in i.oznaka.lower() or q in str(i.opis.lower()) or q in str(i.duzina) or q in str(i.sirina) 
           or q in str(i.visina) or q in str(i.maksimalna_brzina) or q in str(i.godina_proizvodnje) or q in str(i.konjskih_snaga))
            and( pogon == i.pogon_na_sva_cetiri_tocka and zadnja_klupa == i.spustajuca_zadnja_klupa)):
            trazeniDzipovi.append(i)
    return trazeniDzipovi
    
    
def sortirajDzipove(kriterijum):
    '''
    Metoda koja prima string vrednost kriterijuma za sortiranje i na osnovu nje vraca sortiranu kolekciju
    objkeata dzipova prema vrednostima atributa za koji su vezani kriterijumi.
    
    :param kriterijum: string vrednost kriterijuma za sortiranje
    '''
    if kriterijum == 'maksimalna_brzina':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.maksimalna_brzina)
        return sortiranaKolekcija
    elif kriterijum == 'konjskih_snaga':
        sortiranaKolekcija = sorted(Projekat().dzipovi, key=lambda x: x.konjskih_snaga)
        return sortiranaKolekcija
    else:
        raise ValueError('Ne postoji takav kriterijum')
    
def prostor_dzipa(dzip):
    '''
    Metoda koja prima objekat klase dzip i vraca objekat izlozbenog prostora koji je vezan za njega.
    
    :param dzip: objekat klase Dzip
    '''
    return dzip.izlozbeni_prostor
