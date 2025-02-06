from threading import *
from time import *
from random import *


class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
    def run(self):
        while True:
            print("Soy ", self.name, " y estoy trabajando")
            sleep(randint(1,10))
            print("Soy ", self.name, " y he terminado de trabajar")
