from threading import *
from time import *
from random import *

class parking(Thread):
    semaphore = Semaphore(5)
    def __init__(self, nombre):
            Thread.__init__(self, name = nombre)

    def run(self):
        parking.semaphore.acquire()
        print(self.name, "aparcando")    
        sleep(randint(1,3))
        print(self.name, "Termina de aparcar") 
        sleep(randint(1,3))
        parking.semaphore.release()
        print(self.name, f'saliendo. Espacios:{parking.semaphore._value}')
        

if __name__ == "__main__":
    for i in range(1, 11):
        parking(f"coche {i}").start()
          

          
