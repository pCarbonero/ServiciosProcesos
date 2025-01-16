from multiprocessing import Queue
from time import *
from threading import *

def cajaRegistradora():
    for i in range(5):  # Simula servir café para 5 clientes
        print(f"Camarero: Sirviendo café {i + 1}")
        sleep(1)  # Tiempo necesario para servir un café
    print("Camarero: Terminó de servir todos los cafés")

def cajaRegistradora2():
    for i in range(5):  # Simula servir café para 5 clientes
        print(f"Camarero: Sirviendo café {i + 1}")
        sleep(1)  # Tiempo necesario para servir un café
    print("Camarero: Terminó de servir todos los cafés")



if __name__ == "__main__":
    cola = Queue()
    clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
    hilo1 = Thread(target=cajaRegistradora)
    cajas = []

    for i in range(5):
        hilo1 = Thread(target=cajaRegistradora)

    