from clases import *


if __name__ == "__main__":
    l = Libreria("Libreria")
    for i in range(1, 5):
        Estudiante(f"Estudiante {i}", l).start()