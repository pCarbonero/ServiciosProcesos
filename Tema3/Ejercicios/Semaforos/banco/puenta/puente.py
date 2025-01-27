from threading import *
from time import *
from random import *

class Puente(Thread):
    sem = Semaphore(1)
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)    


    def run(self):
        a = randint(1,2)
        if (a == 1):
            self.norte()
        else:
            self.sur()
        print(f"{self.name} llega al otro lado del puente")

    def norte(self):
        self.sem.acquire()
        print(f"{self.name} viaja por el puente al norte")
        sleep(2)
        self.sem.release()
    def sur(self):
        self.sem.acquire()
        print(f"{self.name} viaja por el puente al sur")
        sleep(2)
        self.sem.release()


if __name__ == "__main__":
    for i in range(1, 11):
        Puente(f"Vehiculo {i}").start()