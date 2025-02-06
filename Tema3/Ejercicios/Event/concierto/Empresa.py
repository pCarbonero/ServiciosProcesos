from time import *
from threading import *
from random import *

class Empresa(Thread):
    ticket = 5000
    def __init__(self, nombre, event:Event):
        Thread.__init__(self, name=nombre)
        self.evento = event  

    def genticket(self):
        return f"#{self.ticket}"

    def run(self):
        print(f"Comienza la oferta ")
        self.evento.set()
        sleep(5)
        self.evento.clear()
        print(f"Termina la oferta ")