'''
Modul koji sadrzi klase glavnih entiteta sa kojima se radi.

@author: Marko Krizan
'''
from model.osnovni import Identifikacija, Dimenzije
from enum import Enum


class IzlozbeniProstor(Identifikacija):
    '''
    Klasa entiteta izlozbenog prostora.
    Nasledjuje klasu Indentifikacija.
    '''
    #sve ostale se pakuju u **kwargs i dalje prosledjuje, onda nasledjeni konsruktor salje kome dalje treba
    def __init__(self,oznaka,opis,lokacija):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param lokacija:
        '''
        super().__init__(oznaka=oznaka,opis=opis)
        self.lokacija=lokacija
        
    @staticmethod   
    def empty():
        '''
        Metoda koja kreira "prazan" objekat klase sa default vrednostima.
        '''
        prostor = IzlozbeniProstor('', '', '')
        return prostor
    
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return "{} {} {}".format(self.oznaka,self.opis,self.lokacija)
    
class Vozilo(Identifikacija, Dimenzije):
    '''
    Klasa entiteta Vozilo.
    Nasledjuje klase Indentifikacija i Dimenzije.
    '''
    def __init__(self, oznaka, opis, duzina, sirina, visina, maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        '''
        super().__init__(oznaka = oznaka, opis = opis, duzina = duzina, sirina = sirina, visina = visina)
        self.maksimalna_brzina = maksimalna_brzina
        self.godina_proizvodnje = godina_proizvodnje
        self.izlozbeni_prostor = izlozbeni_prostor
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return "{} {} {} {} {} {} {} {}".format(self.oznaka,self.opis,self.duzina,self.sirina,self.visina, self.maksimalna_brzina, self.godina_proizvodnje, self.izlozbeni_prostor)

class PutnickoVozilo(Vozilo):
    '''
    Klasa entieta Putnicko vozilo.
    Nasledjuje klasu Vozilo.
    '''
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, **kwargs):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        :param broj_vrata:
        '''
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, **kwargs)
        self.broj_vrata = broj_vrata
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return super(PutnickoVozilo, self).__str__() + " " + str(self.broj_vrata)
    
class TerenskoVozilo(Vozilo):
    '''
    Klasa entiteta Terensko vozilo.
    Nasledjuje klasu Vozilo.
    '''
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka, **kwargs):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        :param pogon_na_sva_cetiri_tocka:
        '''
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, **kwargs)
        self.pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka
    def __str__(self):
        return super(TerenskoVozilo, self).__str__() + " " + str(self.pogon_na_sva_cetiri_tocka)
    
class TipMenjaca(Enum):
    '''
    Klasa koja nasledjuje klasu Enumeracija i sadrzi vrednosti za atribut tip menjaca entiteta.
    '''
    MANUELNI = 1
    AUTOMATSKI = 2
 
class Automobil(PutnickoVozilo):
    '''
    Klasa entiteta Automobil.
    Nasledjuje klasu PutnickoVozilo.
    '''
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, broj_sedista, tip_menjaca):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        :param broj_vrata:
        :param broj_sedista:
        :param tip_menjaca:
        
        '''
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata)
        self.broj_sedista = broj_sedista
        self.tip_menjaca = tip_menjaca
        
    @staticmethod   
    def empty():
        '''
        Metoda koja kreira "prazan" objekat klase sa default vrednostima.
        '''
        automobil = Automobil('', '', 1, 1, 1, 1, 1, None, 1, 1, None)
        return automobil
    
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return super(Automobil, self).__str__() + " " + str(self.broj_sedista) + " " + str(self.tip_menjaca)
    
class Dzip(PutnickoVozilo, TerenskoVozilo):
    '''
    Klasa entiteta Dzip.
    Nasledjuje klase PutnickoVozilo i TerenskoVozilo
    '''
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, broj_vrata, pogon_na_sva_cetiri_tocka, konjskih_snaga, spustajuca_zadnja_klupa):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        :param broj_vrata:
        :param pogon_na_sva_cetiri_tocka:
        :param konjskih_snaga:
        :param spustajuca_zadnja_klupa:
        '''
        super().__init__(oznaka = oznaka, opis = opis, duzina = duzina, sirina = sirina, visina = visina, maksimalna_brzina = maksimalna_brzina, godina_proizvodnje = godina_proizvodnje, izlozbeni_prostor = izlozbeni_prostor,  broj_vrata = broj_vrata, pogon_na_sva_cetiri_tocka = pogon_na_sva_cetiri_tocka)
        self.konjskih_snaga = konjskih_snaga
        self.spustajuca_zadnja_klupa = spustajuca_zadnja_klupa
        
    @staticmethod   
    def empty():
        '''
        Metoda koja kreira "prazan" objekat klase sa default vrednostima.
        '''
        dzip = Dzip('', '', 1, 1, 1, 1, 1, None, 1, False, 1, False)
        return dzip
    
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return super(Dzip, self).__str__() + " " + str(self.konjskih_snaga) + " " + str(self.spustajuca_zadnja_klupa)

class Kvad(TerenskoVozilo):
    '''
    Klasa entieta Kvad.
    Nasledjuje TerenskoVozilo.
    '''
    def __init__(self,oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka, prostor_za_stvari):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        :param duzina:
        :param sirina:
        :param visina:
        :param maksimalna_brzina:
        :param godina_proizvodnje:
        :param izlozbeni_prostor:
        :param pogon_na_sva_cetiri_tocka:
        :param prostor_za_stvari:
        '''
        super().__init__(oznaka,opis,duzina,sirina,visina,maksimalna_brzina, godina_proizvodnje, izlozbeni_prostor, pogon_na_sva_cetiri_tocka)
        self.prostor_za_stvari = prostor_za_stvari
        
    @staticmethod   
    def empty():
        '''
        Metoda koja kreira "prazan" objekat klase sa default vrednostima.
        '''
        kvad = Kvad('', '', 1, 1, 1, 1, 1, None, False, False)
        return kvad
    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return super(Kvad, self).__str__() + " " + str(self.prostor_za_stvari)
        
        
        
     


    
    
