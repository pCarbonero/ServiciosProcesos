from threading import *
from time import *
from random import *

class Contador(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.lock = Lock()
        self.contador = 0

    def run(self):       
        with self.lock:
            while self.contador < 1000:
                self.contador += 1
                print(self.contador)


if __name__ == '__main__':
    contador = Contador()  
    hilos = [] 
    for i in range (10):
        hilo = Thread(target=contador.incrementar)
        hilos.append(hilo)
        hilo.start()