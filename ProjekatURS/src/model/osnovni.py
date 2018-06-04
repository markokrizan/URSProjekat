'''
Modul koji sadrzi osnovne indentifikacione klase koje nasledjuju svi ostali entiteti.

@author: Aleksandar Rancic
'''

class Identifikacija(object):
    '''
    Klasa koja sadrzi osnovne indentifikacione atribute
    '''
    def __init__(self,oznaka,opis,**kwargs):
        '''
        Constructor
        
        :param oznaka:
        :param opis:
        
        '''
        super().__init__(**kwargs)
        self.oznaka=oznaka
        self.opis=opis
    def __str__(self, *args, **kwargs):
        '''
        Redefinicja __str__ metode.
        '''
        return "{} {}".format(self.oznaka,self.opis)
    
    
class Dimenzije(object):
    '''
    Klasa koja sadrzi atribute vezane za dimenzije entiteta.
    '''
    def __init__(self,duzina,sirina,visina,**kwargs):
        '''
        Constructor
        
        :param duzina:
        :param sirina:
        :param visina:
        
        '''
        super().__init__(**kwargs)
        self.duzina=duzina
        self.sirina=sirina
        self.visina=visina

    @property
    def duzina(self):
        '''
        Geter metoda atributa duzina
        '''
        return self.__duzina

    @duzina.setter
    def duzina(self, value):
        '''
        Seter metoda atributa duzina
        '''
        if value <= 0:
            raise ValueError("Vrednost za duzinu mora biti veca od 0")
        self.__duzina = value

    @property
    def sirina(self):
        '''
        Geter metoda atributa sirina.
        '''
        return self.__sirina

    @sirina.setter
    def sirina(self, value):
        '''
        Seter metoda atributa sirina.
        '''
        if value <= 0:
            raise ValueError("Vrednost za sirinu mora biti veca od 0")
        self.__sirina = value

    @property
    def visina(self):
        '''
        Geter metoda atributa visina.
        '''
        return self.__visina

    @visina.setter
    def visina(self, value):
        '''
        Seter metoda atributa visina
        '''
        if value <= 0:
            raise ValueError("Vrednost za visinu mora biti veca od 0")
        self.__visina = value
        
    def zapremina(self):
        '''
        Metoda koja racuna zapreminu na osnovu vrednosti atributa duzine sirine i visine
        '''
        return self.duzina*self.sirina*self.visina

    def __str__(self):
        '''
        Redefinicja __str__ metode.
        '''
        return "{} {} {}".format(self.duzina,self.sirina,self.visina)

