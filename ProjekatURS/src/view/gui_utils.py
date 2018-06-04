'''
Created on May 31, 2018

Modul koji sadrzi helper metode za view komponente

@author: Marko Krizan
'''

def Centriraj(prozor):
    '''
    Metoda koja prima referencu na view i zatim ga centrira na sredinu ekrana.
    
    :param prozor: referenca na view
    '''
    prozor.withdraw()
    prozor.update_idletasks()
    x = (prozor.winfo_screenwidth() - prozor.winfo_reqwidth()) / 2
    y = (prozor.winfo_screenheight() - prozor.winfo_reqheight()) / 2
    prozor.geometry("+%d+%d" % (x, y))
    prozor.deiconify() 
