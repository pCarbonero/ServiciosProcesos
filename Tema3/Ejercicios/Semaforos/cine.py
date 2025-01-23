from threading import *
from time import *
from random import *

class Cine(Thread):
    semaphore = Semaphore(20)
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)    


    def run(self):
        self.semaphore.acquire()
        print(self.name, "Entra al cine")    
        sleep(randint(1,3))
        #print(self.name, "Viendo la pelicula")
        #sleep(5)
        self.semaphore.release()
        print(self.name, f'saliendo. Espacios:{Cine.semaphore._value}')
        sleep(randint(1,3))

if __name__ == "__main__":
    for i in range(1, 51):
        Cine(f"Persona {i}").start()