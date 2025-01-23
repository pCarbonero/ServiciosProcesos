from threading import *
from time import *
from random import *

class Banco(Thread):
    semaphore = Semaphore(3)
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)  

    def run(self):
        self.semaphore.acquire()
        print(self.name, "Usa el cajero ")
        sleep(randint(1,3))
        self.semaphore.release()
        print(self.name, f'Se va. Cajeros disponibles: {Banco.semaphore._value}')  
        sleep(randint(1,3))
