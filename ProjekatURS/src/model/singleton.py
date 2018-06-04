'''
Modul koji sadrzi singleton klasu Projekat cije vrednosti atributa su kolekcije entiteta

@author: Marko Krizan
'''
from util.pickleUnpickle import UnPickle

class Projekat(object):
    '''
    Singleton klasa Projekat.
    '''
    _instance = None
    #prvo proveri da li je vec kreirana instanca
    def __new__(self):
        '''
        Constructor
        
        Ako postoji instanca klase vrati pokazivac na tu jednu jedinu instancu. 
        Omogucava da se konstantno radi sa jednim objektom ciji atributi su kolekcije koje se manipulisu.
        '''
        if not self._instance:
           self._instance = super(Projekat, self).__new__(self) 
           self.prostori = UnPickle('prostori.bin')
           self.automobili = UnPickle('automobili.bin')
           self.dzipovi = UnPickle('dzipovi.bin')
           self.kvadovi = UnPickle('kvadovi.bin')  
        return self._instance
