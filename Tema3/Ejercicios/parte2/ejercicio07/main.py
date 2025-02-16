from productor import *
from consumidor import *

if __name__ == '__main__':
    for i in range(5):
        p = Productor(f"Productor {i+1}")
        c = Consumidor(f"Consumidor {i+1}")
        p.start()
        c.start()

    