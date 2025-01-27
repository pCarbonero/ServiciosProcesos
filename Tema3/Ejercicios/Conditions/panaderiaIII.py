from threading import *
from time import *
from random import *

class Panaderia(Thread):
    pan = 7 
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

class Comprador(Thread):
    cond = Condition()
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        
        with self.cond:
            if Panaderia.pan > 0:
                Panaderia.pan -= 1
                print(self.name, "Compra un pan")
            Reponedor("Reponedor").start()

class Reponedor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        print("Se repone el pan")
        Panaderia.pan = 7

if __name__ == "__main__":
    for i in range(1, 11):
        Comprador(f"Persona {i}").start()
    
