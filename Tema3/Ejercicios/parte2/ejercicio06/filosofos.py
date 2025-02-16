from threading import *
from time import *
from random import *

class Palillos(Thread):
    palillo = [False, False, False, False, False]
    c = Condition()
    c2 = Condition()
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
            while self.palillos.palillo[m1] == True:
                print(f"{self.name} espera para coger el palillo {m1}")
                self.palillos.c.wait()
            self.palillos.palillo[m1] = True

        print(f"{self.name} ha cogido {m1}")

        with self.palillos.c2:
            while self.palillos.palillo[m2] == True:
                print(f"{self.name} espera para coger el palillo {m2}")
                self.palillos.c2.wait()
            self.palillos.palillo[m2] = True

        print(f"{self.name} ha cogido {m2}")
        print(f"{self.name} empieza a comer")
        sleep(randint(1,3))
        print(f"{self.name} ha terminado de comer")

        with self.palillos.c:
            self.palillos.palillo[m1] = False
            self.palillos.c.notify_all()

        with self.palillos.c2:
            self.palillos.palillo[m2] = False
            self.palillos.c2.notify_all()


    