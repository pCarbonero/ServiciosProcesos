from filosofos import Filosofo, Palillos

if __name__ == '__main__':
    p = Palillos("Palillos")
    for i in range(5):
        f = Filosofo(f"Filosofo {i}", i, p)
        f.start()