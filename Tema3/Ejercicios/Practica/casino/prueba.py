from threading import Thread, Semaphore, Barrier, Condition
from time import sleep
from random import randint

class Croupier(Thread):
    def __init__(self, barrier, condition):
        super().__init__(name="Croupier")
        self.barrier = barrier
        self.condition = condition
        self.resultado = None

    def run(self):
        while True:
            self.barrier.wait()  # Espera a que haya 3 jugadores listos
            with self.condition:
                self.resultado = randint(0, 36)  # Gira la ruleta
                print(f'El croupier gira la ruleta... Ha salido el {self.resultado}')
                self.condition.notify_all()  # Notifica a los jugadores el resultado

class Jugador(Thread):
    s = Semaphore(1)
    def __init__(self, nombre, barrier, condition):
        super().__init__(name=nombre)
        self.barrier = barrier
        self.condition = condition
        self.continua = True

    def run(self):
        sleep(randint(1, 3))
        print(f'{self.name} ha llegado')
        self.barrier.wait()  # Espera a que haya al menos 3 jugadores
        print(f'ESTOY LISTO {self.name}')
        
        while self.continua:
            sleep(randint(1, 5))
            with Jugador.s:  # Accede a la ruleta de forma controlada
                apuesta = randint(0, 36)
                print(f'{self.name} apuesta al {apuesta}')
                
                with self.condition:
                    self.condition.wait()  # Espera el resultado del croupier
                    if apuesta == croupier.resultado:
                        print(f'{self.name} ha ganado la apuesta')
                    else:
                        print(f'{self.name} ha perdido :C')
                
                if randint(1, 2) == 1:
                    self.continua = False
                    print(f'{self.name} se va del casino')

if __name__ == '__main__':
    barrier = Barrier(3)  # El croupier esperará a que haya 3 jugadores
    condition = Condition()
    croupier = Croupier(barrier, condition)
    croupier.start()

    jugadores = [Jugador(f'Jugador {i+1}', barrier, condition) for i in range(6)]
    for j in jugadores:
        j.start()
