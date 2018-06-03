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
        
    @staticmethod   
    def empty():
        prostor = IzlozbeniProstor('', '', '')
        return prostor
    
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
        
    @staticmethod   
    def empty():
        automobil = Automobil('', '', 1, 1, 1, 1, 1, None, 1, 1, None)
        return automobil
    
    def __str__(self):
        return super(Automobil, self).__str__() + " " + str(self.broj_sedista) + " " + str(self.tip_menjaca)
    
class Dzip(PutnickoVozilo, TerenskoVozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, pogon_na_sva_cetiri_tocka, konjskih_snaga, spustajuca_zadnja_klupa):
        super().__init__(oznaka = oznaka, opis = opis, duzina = duzina, sirina = sirina, visina = visina, maksimalna_brzina = maksimalna_brzina, godina_proizvodnje = godina_proizvodnje, izlozbeni_prostor = izlozbeni_prostor,  broj_vrata = broj_vrata, pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka)
        self.konjskih_snaga = konjskih_snaga
        self.spustajuca_zadnja_klupa = spustajuca_zadnja_klupa
        
    @staticmethod   
    def empty():
        dzip = Dzip('', '', 1, 1, 1, 1, 1, None, 1, False, 1, False)
        return dzip
    
    def __str__(self):
        #??? multiple inheritance
        return super(Dzip, self).__str__() + " " + str(self.konjskih_snaga) + " " + str(self.spustajuca_zadnja_klupa)

class Kvad(TerenskoVozilo):
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka, prostor_za_stvari):
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka)
        self.prostor_za_stvari = prostor_za_stvari
        
    @staticmethod   
    def empty():
        kvad = Kvad('', '', 1, 1, 1, 1, 1, None, False, False)
        return kvad
    def __str__(self):
        return super(Kvad, self).__str__() + " " + str(self.prostor_za_stvari)
        
        
        
     


if __name__ == '__main__':
    pass
    
    
