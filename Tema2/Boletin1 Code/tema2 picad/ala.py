from multiprocessing import *

def incrementar(valor, lock):
    for _ in range(10000):
        with lock:
            valor.value += 1


if __name__ == "__main__":
    contador = Value('i', 0)
    lock = Lock()
    procesos = [Process(target=incrementar, args=(contador,lock)) for _ in range(4)]

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    print(f"Valor final del contador: {contador.value}")    