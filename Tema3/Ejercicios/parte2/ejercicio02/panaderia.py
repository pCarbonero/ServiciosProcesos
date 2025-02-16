from threading import *
from time import *
from random import *

class Panaderia(Thread):
    dependiente = False
    c = Condition()
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        sleep(randint(1,3))
        print(f"{self.name} llega a la panaderia ")
        with Panaderia.c:
            while Panaderia.dependiente:
                print(f"{self.name} espera para ser atentido ")
                Panaderia.c.wait()
            Panaderia.dependiente = True

        print(f"{self.name} esta siendo atentido ")
        sleep(randint(1,5))
        print(f"{self.name} se va de la panaderia ")

        with Panaderia.c:
             Panaderia.dependiente = False
             Panaderia.c.notify_all()


if __name__ == '__main__':
    for i in range(10):
        h = Panaderia(f'Cliente {i+1}')
        h.start()