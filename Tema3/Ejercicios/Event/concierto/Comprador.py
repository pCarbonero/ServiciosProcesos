from time import *
from threading import *
from random import *
from Empresa import *


class Comprador(Thread):
    def __init__(self, nombre, empresa: Empresa):
        self.empresa = empresa
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} entra en la web")
        sleep(randint(1,3))
        print(f"{self.name} comienza a comprar")
        sleep(randint(1,3))
        if not self.empresa.evento.is_set():
            print(f"{self.name} no puede comprar, se acabó la oferta")
        else:
            self.empresa.ticket += 1 
            print(f"{self.name} termina de comprar. Tiene un ticket con codigo {self.empresa.genticket()}")
        
