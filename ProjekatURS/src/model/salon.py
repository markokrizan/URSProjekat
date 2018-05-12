'''
Created on May 12, 2018

@author: freeman
'''
from model.osnovni import Identifikacija, Dimenzije
from enum import Enum


class IzlozbeniProstor(Identifikacija):
    #sve ostale se pakuju u **kwargs i dalje prosledjuje, onda nasledjeni konsruktor salje kome dalje treba
    def __init__(self,oznaka,opis,lokacija):
        super().__init__(oznaka=oznaka,opis=opis)
        self.lokacija=lokacija
    def __str__(self):
        return "{} {} {}".format(self.oznaka,self.opis,self.lokacija)
    
class Vozilo(Identifikacija, Dimenzije):
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor):
        super().__init__(oznaka = oznaka, opis = opis, duzina = duzina, sirina = sirina, visina = visina)
        self.maksimalna_brzina = maksimalna_brzina
        self.godina_proizvodnje = godina_proizvodnje
        self.izlozbeni_prostor = izlozbeni_prostor
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.oznaka,self.opis,self.duzina,self.sirina,self.visina, self.maksimalna_brzina, self.godina_proizvodnje, self.izlozbeni_prostor)

class PutnickoVozilo(Vozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, **kwargs):
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, **kwargs)
        self.broj_vrata = broj_vrata
    def __str__(self):
        return super(PutnickoVozilo, self).__str__() + " " + str(self.broj_vrata)
    
class TerenskoVozilo(Vozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka, **kwargs):
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, **kwargs)
        self.pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka
    def __str__(self):
        return super(TerenskoVozilo, self).__str__() + " " + str(self.pogon_na_sva_cetiri_tocka)
    
class TipMenjaca(Enum):
    MANUELNI = 1
    AUTOMATSKI = 2
 
class Automobil(PutnickoVozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, broj_sedista, tip_menjaca):
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata)
        self.broj_sedista = broj_sedista
        self.tip_menjaca = tip_menjaca
    def __str__(self):
        return super(Automobil, self).__str__() + " " + str(self.broj_sedista) + " " + str(self.tip_menjaca)
    
class Dzip(PutnickoVozilo, TerenskoVozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, pogon_na_sva_cetiri_tocka, konjskih_snaga, spustajuca_zadnja_klupa):
        super().__init__(oznaka = oznaka, opis = opis, duzina = duzina, sirina = sirina, visina = visina, maksimalna_brzina = maksimalna_brzina, godina_proizvodnje = godina_proizvodnje, izlozbeni_prostor = izlozbeni_prostor,  broj_vrata = broj_vrata, pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka)
        self.konjskih_snaga = konjskih_snaga
        self.spustajuca_zadnja_klupa = spustajuca_zadnja_klupa
    def __str__(self):
        #??? multiple inheritance
        return super(Dzip, self).__str__() + " " + str(self.konjskih_snaga) + " " + str(self.spustajuca_zadnja_klupa)

class Kvad(TerenskoVozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka, prostor_za_stvari):
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka)
        self.prostor_za_stvari = prostor_za_stvari
    def __str__(self):
        return super(Kvad, self).__str__() + " " + str(self.prostor_za_stvari)
        
        
        
     


if __name__ == '__main__':
    #Test:
    #prostor, automobil, dzip, kvad - entiteti sa kojima se radi
    prostor = IzlozbeniProstor('p1', 'prostor1', 'Novi Sad')
    automobil = Automobil('a1', 'vozilo1', 1, 2, 3, 60, 1992, prostor, 3, 4, TipMenjaca.AUTOMATSKI)
    dzip = Dzip('dz1', 'dzip1', 2, 3, 4, 80, 1993, prostor, 4,  True, 120, False)
    kvad = Kvad('kv1', 'kvad1', 3, 4, 5, 90, 1995, prostor, True, False)
    
    print(prostor)
    print(automobil)
    print(dzip)
    print(kvad)
    
