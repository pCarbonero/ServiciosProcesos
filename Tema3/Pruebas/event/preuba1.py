from time import *
from threading import *
from random import *

class Raton(Thread):
    def __init__(self, nombre, event:Event):
        Thread.__init__(self, name=nombre)
        self.evento = event

    def run(self):
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print(f"El raton {self.name} toma el control del plato ")
        sleep(randint(1,3))
        print(f"El raton {self.name} termina de comer ")
        self.evento.set()


if __name__ == "__main__":
    plato = Event()
    plato.set()
    for i in range(2):
        raton = Raton(f"Raton {i+1}", plato)
        raton.start()