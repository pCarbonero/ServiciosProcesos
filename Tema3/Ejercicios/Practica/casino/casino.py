from threading import *
from time import *
from random import *


class Casino(Thread):
    s = Semaphore()
    def __init__(self, nombre, barrier: Barrier):
        self.barrier = barrier
        self.continua = True
        Thread.__init__(self, name = nombre) 

    def run(self):
        sleep(randint(1,3))
        print(f'{self.name} ha llegado')
        self.barrier.wait()

        print(f'ESTOY LISTO {self.name}')

        while self.continua:
            sleep(randint(1,5))
            with Casino.s:
                sleep(1)
                apuesta = randint(0,36)
                print(f'{self.name} apuesta al {apuesta}')

                num = randint(0,36)                
                print(f'Girando la ruleta para {self.name}')
                sleep(5)
                print(f'Ha salido el {num}')

                if num == apuesta:
                    print(f'{self.name} ha ganado la apuesta')
                else:
                    print(f'{self.name} ha perdido :C')
                
                cont = randint(1,2) #si aqui sale 1 el jugador no se va

                if cont == 1:
                    self.continua = False
                else:
                    print(f'{self.name} sigue jugando')

        print(f'{self.name} se va del casino')



            





