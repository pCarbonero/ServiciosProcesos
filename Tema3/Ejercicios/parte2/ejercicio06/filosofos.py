from threading import *
from time import *
from random import *

class Palillos(Thread):
    palillo = [False, False, False, False, False]
    c = Condition()
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)


class Filosofo(Thread):
    def __init__(self, nombre, codigo, palillos):
        self.palillos = palillos
        self.codigo: int = codigo
        Thread.__init__(self, name = nombre)

    def run(self):
        m1 = self.codigo
        if self.codigo == 4:
            m2 = 0
        else:
            m2 = self.codigo + 1

        print(f'{self.name} está pensando...')
        sleep(randint(1,3))
        print(f'{self.name} va a comer')
        
        with self.palillos.c:
            while self.palillos.palillo[m1] == True or self.palillos.palillo[m2] == True:
                print(f"{self.name} espera para comer con los palillos {m1} y {m2}")
                self.palillos.c.wait()
            self.palillos.palillo[m1] = True
            self.palillos.palillo[m2] = True
        print(f"{self.name} ha cogido {m1} y {m2}")
        sleep(randint(1,3))
        print(f"{self.name} ha terminado de comer")
        with self.palillos.c:
            self.palillos.palillo[m1] = False
            self.palillos.palillo[m2] = False
            self.palillos.c.notify_all()


    