from threading import *
from time import *
from random import *
from datos import *

class Productor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre) 

    def run(self):
        while True:
            sleep(randint(1,10))
            with Datos.c:
                
                while Datos.q.qsize() >= 5:
                    print(f'{self.name} quiere producir pero la cola de datos llena, esperando para insertar')
                    Datos.c.wait()

            sleep(randint(1,3))
            dato = randint(1,9999)
            Datos.insertarDato(dato)
            print(f'{self.name} inserto el dato {dato}')

            with Datos.c:
                Datos.c.notify_all()
