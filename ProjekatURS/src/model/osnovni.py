'''
Created on May 12, 2018

@author: freeman
'''

class Identifikacija(object):
    def __init__(self,oznaka,opis,**kwargs):
        super().__init__(**kwargs)
        self.oznaka=oznaka
        self.opis=opis
    def __str__(self, *args, **kwargs):
        return "{} {}".format(self.oznaka,self.opis)
    
    
class Dimenzije(object):
    def __init__(self,duzina,sirina,visina,**kwargs):
        super().__init__(**kwargs)
        self.duzina=duzina
        self.sirina=sirina
        self.visina=visina

    @property
    def duzina(self):
        return self.__duzina

    @duzina.setter
    def duzina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za duzinu mora biti veca od 0")
        self.__duzina = value

    @property
    def sirina(self):
        return self.__sirina

    @sirina.setter
    def sirina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za sirinu mora biti veca od 0")
        self.__sirina = value

    @property
    def visina(self):
        return self.__visina

    @visina.setter
    def visina(self, value):
        if value <= 0:
            raise ValueError("Vrednost za visinu mora biti veca od 0")
        self.__visina = value
    def zapremina(self):
        return self.duzina*self.sirina*self.visina

    def __str__(self):
        return "{} {} {}".format(self.duzina,self.sirina,self.visina)

if __name__ == '__main__':
    pass