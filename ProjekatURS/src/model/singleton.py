'''
Created on May 12, 2018

@author: freeman
'''
from util.pickleUnpickle import UnPickle

class Projekat(object):
    _instance = None
    #prvo proveri da li je vec kreirana instanca
    def __new__(self):
        if not self._instance:
           self._instance = super(Projekat, self).__new__(self) 
           self.prostori = UnPickle('prostori.bin')
           self.automobili = UnPickle('automobili.bin')
           self.dzipovi = UnPickle('dzipovi.bin')
           self.kvadovi = UnPickle('kvadovi.bin')  
        return self._instance
