'''
Modul u kojem se nalaze testovi koje je pisao student: Aleksandar Rancic
Radjeno pomocu biblioteke: pytest

Testirane funkcije: controller.automobili.sortirajAutomobile i controller.dzipovi.sortirajDzipove

@author: Aleksandar Rancic
'''
import pytest

from controller.automobili import sortirajAutomobile
from model.singleton import Projekat
from controller.dzipovi import sortirajDzipove


def test_sortiraj_automobile():
    sorted = sortirajAutomobile('maksimalna_brzina')
    assert sorted != None
    assert len(sorted) == len(Projekat().automobili)
    
def test_sortiraj_automobile_pogresna_vrednost():
    with pytest.raises(ValueError):
        sortirajAutomobile('asdfasdfasdfasdfasdf')
        
def test_sortiraj_automobile_none():
    with pytest.raises(ValueError):
        sortirajAutomobile(None)
        
def test_sortiraj_automobile_int():
    with pytest.raises(ValueError):
        sortirajAutomobile(123)
        
def test_sortiraj_automobile_reverse_case():
    with pytest.raises(ValueError):
        sortirajAutomobile('MAKSIMALNA_BRZINA')

def test_sortiraj_automobile_similar():
    with pytest.raises(ValueError):
        sortirajAutomobile('maksimalna_brzinaa')

#dzipovi:       
        
def test_sortiraj_dzipove():
    sorted = sortirajDzipove('konjskih_snaga')
    assert sorted != None
    assert len(sorted) == len(Projekat().dzipovi)
    
def test_sortiraj_dzipove_pogresna_vrednost():
    with pytest.raises(ValueError):
        sortirajDzipove('asdfasdfasdfasdfasdf')
        
def test_sortiraj_dzipove_none():
    with pytest.raises(ValueError):
        sortirajDzipove(None)
        
def test_sortiraj_dzipove_int():
    with pytest.raises(ValueError):
        sortirajDzipove(123)
        
def test_sortiraj_dzipove_reverse_case():
    with pytest.raises(ValueError):
        sortirajDzipove('KONJSKIH_SNAGA')

def test_sortiraj_dzipove_similar():
    with pytest.raises(ValueError):
        sortirajDzipove('konjskih_snagaa')
        


    
