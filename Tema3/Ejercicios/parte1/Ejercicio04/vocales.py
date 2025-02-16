from threading import *
from time import *
from random import *

class leeVocales(Thread):
    archivo = "parte1/Ejercicio04/fichero.txt"
    def __init__(self, nombre, vocalBuscada):
        self.vocalBuscada = vocalBuscada
        self.contador = 0
        Thread.__init__(self, name = nombre) 

    #def run(self):
     #   with open(leeVocales.archivo, "r") as f:
      #      for linea in f:
       #         for v in linea:
        #            if v.lower() == self.vocalBuscada:
         #               self.contador += 1

    def run(self):
        with open(leeVocales.archivo, "r") as f:
            for linea in f:
                self.contador += linea.lower().count(self.vocalBuscada)

        print(f'{self.name} ha encontrado {self.contador} veces la vocal {self.vocalBuscada}')



if __name__ == '__main__':
    vocales = ['a', 'e', 'i', 'o', 'u']

    for v in vocales:
        h = leeVocales(f'Buscador {v}', v)
        h.start()
        h.join()

