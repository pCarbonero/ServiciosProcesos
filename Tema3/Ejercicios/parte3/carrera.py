from threading import *
from time import *
from random import *

class Carrera(Thread):
    def __init__(self, nombre, b: Barrier):
        self.b = b
        Thread.__init__(self, name = nombre)

    def run(self):
        sleep(randint(1,3))
        print(f"{self.name} ha llegado")
        self.b.wait()
        

        
        sleep(randint(3,10))
        print(f'{self.name} ha llegado a la meta')

if __name__ == '__main__':
    b = Barrier(10)
    for i in range(10):
        h = Carrera(f'Corredor {i+1}', b)
        h.start()