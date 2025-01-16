import random
from threading import Semaphore, Thread
import time

class Supermercado(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
            Thread.__init__(self, name = nombre)
    
    def run(self):
          print("Hilo ", self.name, "va a una caja")
          Supermercado.semaforo.acquire()
          print("Hilo", self.name, "esta siendo atendido")
          time.sleep(random.randint(1,10))
          print("Hilo", self.name, "esta pagando")
          Supermercado.semaforo.release()
          print("Hilo", self.name, "sale del supermercado")
