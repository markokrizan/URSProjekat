'''
Modul koji sadrzi metode za serijalizaciju i deserijalizaciju kolekcija objekata u fajl cime se vrsi perzistiranje.

@author: Aleksandar Rancic
'''

import pickle
import os, os.path

#Don't use file names that have the same name as Python standard library modules.!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def Pickle(imeFajla, lista): 
    '''
    Metoda koja prima ime fajla i kolekciju objekata i serijalizuje kolekciju u fajl.
    
    :param imeFajla: string vrednost imena fajla
    :param lista: kolekcija objekata 
    '''
    try:
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', imeFajla)), 'wb')
        pickle.dump(lista, binary_file)
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
    
    
def UnPickle(imeFajla):
    '''
    Metoda koja prima ime fajla iz kojeg deserijalizuje objekte u kolekciju i vrati je.
    
    :param imeFajla: string vrednost imena fajla
    '''
    try:
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', imeFajla)), 'rb')
        lista = pickle.load(binary_file)
        
        return lista
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
