from casino import *
from threading import *


if __name__ == '__main__':
    b = Barrier(3)
    for i in range(6):
        h = Casino(f'Jugador {i+1}', b)
        h.start()