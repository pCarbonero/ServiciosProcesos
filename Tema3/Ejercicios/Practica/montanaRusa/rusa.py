from threading import *
from time import *
from random import *

class Visitante(Thread):
    montañaRusa = Semaphore(5)
    barrera = Barrier(5)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        #sleep(randint(1,5))
        print(f"Visitante {self.name} llega al parque")
        sleep(randint(1, 3))

        print(f"🧑‍ Visitante {self.name} está esperando para entrar a la atracción")
        Visitante.montañaRusa.acquire()

        print(f"🎟️ Visitante {self.name} entra a la atracción. Espacios disponibles: {self.montañaRusa._value}")

        Visitante.barrera.wait()


        if Visitante.barrera.wait() == 0:
            print("🎢 La montaña rusa está llena. ¡Iniciando el recorrido!")
            sleep(4)
            print("🎢 La montaña rusa ha terminado el recorrido!")

        Visitante.barrera.wait()

        print(f"📤 Visitante {self.name} se baja de la atracción.")
        Visitante.montañaRusa.release()

if __name__ == '__main__':
    for i in range(10):
        h = Visitante(f'Jugador {i+1}')
        h.start()