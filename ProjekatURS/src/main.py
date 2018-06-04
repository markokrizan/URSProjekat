'''
Modul koji sadrzi main blok za pokretanje aplikacije.

@author: Marko Krizan
'''

from view.glavni_prozor import *

if __name__ == '__main__':
    
    glavni = GlavniProzor()
    glavni.mainloop()