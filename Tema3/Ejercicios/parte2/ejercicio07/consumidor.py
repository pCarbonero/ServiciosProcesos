from threading import *
from time import *
from random import *
from datos import *

class Consumidor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre) 

    def run(self):
        while True:
            sleep(randint(1,10))
            with Datos.c:
                while Datos.q.empty():
                    print(f'{self.name} quiere consumir pero la cola de datos esta vacia, esperando que se llene')
                    Datos.c.wait()
            sleep(randint(1,3))
            dato = Datos.cogerDato()
            print(f'{self.name} cogio el dato {dato}')

            with Datos.c:
                Datos.c.notify_all()