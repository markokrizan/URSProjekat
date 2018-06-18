'''
Modul u kojem se nalaze testovi koje je pisao student: Marko Krizan
Radjeno pomocu biblioteke: pytest

Testirane funkcije: controller.automobili.nadjiAutomobile i controller.dzipovi.nadjiDzipove 

@author: Marko Krizan
'''

import pytest

from controller.automobili import nadjiAutomobile
from controller.dzipovi import nadjiDzipove
from model.salon import Automobil, Dzip


#nadjiAutomobile:
def test_nadji_automobil():
    a = nadjiAutomobile('automobil_za_test')
    assert a!= None
    assert a[0].opis == 'automobil_za_test'
    
def test_nadji_automobil_pogresna_vrednost():
    a = nadjiAutomobile('adsgasdgasdfasdg')
    assert a!= None
    assert len(a) == 0
    
def test_nadji_automobil_none():
    with pytest.raises(ValueError):
        nadjiAutomobile(None)
        
def test_nadji_automobil_int():
    a = nadjiAutomobile(23)
    assert a!= None
    assert a[0].opis == 'automobil_za_test'
    
def test_nadji_automobil_reverse_case():
    a = nadjiAutomobile('AUTOMOBIL_ZA_TEST')
    assert a!= None
    assert a[0].opis == 'automobil_za_test'
    
def test_nadji_automobil_similar():
    a = nadjiAutomobile('automobil_za_testt')
    assert a!= None
    assert len(a) == 0
    
def test_nadji_automobil_multiple():
    a = nadjiAutomobile('brzina')
    assert a!= None
    assert type(a[0]) is Automobil
    assert type(a[1]) is Automobil
    assert type(a[2]) is Automobil
    assert type(a[3]) is Automobil
    assert type(a[4]) is Automobil
    
#nadjiDzipove

def test_nadji_dzipove():
    dz = nadjiDzipove('dzip1', True, False)
    assert dz!= None
    assert dz[0].opis == 'dzip1'
    


def test_nadji_dzipove_pogresna_vrednost():
    a = nadjiDzipove('dzip1', False, False)
    assert a!= None
    assert len(a) == 0
    

def test_nadji_dzipove_none():
    with pytest.raises(ValueError):
        nadjiDzipove('dzip1', True, None)

       
def test_nadji_dzipove_int():
    dz = nadjiDzipove(80, True, False)
    assert dz!= None
    assert dz[0].opis == 'dzip1'

   
def test_nadji_dzipove_reverse_case():
    dz = nadjiDzipove('DZIP1', True, False)
    assert dz!= None
    assert dz[0].opis == 'dzip1'

   
def test_nadji_dzipove_similar():
    dz = nadjiDzipove('dzipp1', False, False)
    assert dz!= None
    assert len(dz) == 0
    
    
def test_nadji_dzipove_multiple():
    dz = nadjiDzipove('dzip', True, False)
    assert dz!= None
    assert type(dz[0]) is Dzip
    assert type(dz[1]) is Dzip
 


    
    
    

    
    
    
