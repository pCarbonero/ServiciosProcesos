from threading import *
from time import *
from random import *

class Carniceria(Thread):
    s = Semaphore(4)
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        sleep(randint(1,3))
        print(f'{self.name} llega a la carnicería🥩')
        self.s.acquire()
        print(f'{self.name} está siendo atendido 👩‍🍳')
        sleep(randint(1,3))
        self.s.release()
        print(f'{self.name} se va 🏃‍♂️💃')


if __name__ == '__main__':
    for i in range(10):
        h = Carniceria(f'Cliente {i+1}')
        h.start()
