'''
Created on May 12, 2018

@author: freeman
'''

import pickle
import os, os.path

#Don't use file names that have the same name as Python standard library modules.!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def Pickle(imeFajla, lista): 
    try:
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', imeFajla)), 'wb')
        pickle.dump(lista, binary_file)
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
    
    
def UnPickle(imeFajla):
    try:
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', imeFajla)), 'rb')
        lista = pickle.load(binary_file)
        
        return lista
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
