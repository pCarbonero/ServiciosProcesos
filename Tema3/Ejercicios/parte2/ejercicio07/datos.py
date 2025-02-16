from threading import *
from time import *
from random import *
from queue import *


class Datos(Thread):
    q = LifoQueue(maxsize=5)
    datosLlenos = False
    c = Condition()
    cGet = Condition()
    def __init__(self):
        Thread.__init__(self) 


    def insertarDato(dato: int):
            Datos.q.put(dato)

    def cogerDato():
            dato = Datos.q.get()
            return dato
        
