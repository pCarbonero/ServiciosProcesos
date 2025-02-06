from threading import *
from time import *
from random import *

class Caja(Thread): 
    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self, name = nombre)
        self.barrera = barrera

    def run(self): 
        self.barrera.wait()
        print("Hilo", self.name, "entra en caja")
        sleep(randint(1,3))
        print("Hilo", self.name, "sale de caja")