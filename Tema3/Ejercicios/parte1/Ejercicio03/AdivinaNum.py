from threading import *
from time import *
from random import *


class AdivinaNumero(Thread):
    numeroSecreto = randint(0,100)
    numeroAdivinado = False
    s = Semaphore(1)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        sleep(randint(1,5))
        while True:
            sleep(randint(1,5))
            with AdivinaNumero.s:
                if (AdivinaNumero.numeroAdivinado == False):
                    num = randint(0,100)
                    if (num == self.numeroSecreto):
                        print(f'{self.name} ha adivinado el numero {AdivinaNumero.numeroSecreto} 😨😩😤')
                        AdivinaNumero.numeroAdivinado = True
                    else:
                        print(f'{self.name} ha intentado con el {num}')
                else:
                    break

    
if __name__ == '__main__':
    hilos = [AdivinaNumero(f'Hilo-{i}') for i in range(10)]

    for i in range(10):
        hilo = AdivinaNumero(f'hilo {i+1}')
        hilo.start()