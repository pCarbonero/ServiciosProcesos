from threading import *
from time import *
from random import *


class Libreria(Thread):
    libros = [False, False, False, False, False, False, False, False, False]
    c = Condition()
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre) 


class Estudiante(Thread):
    def __init__(self, nombre, libreria):
        self.libreria = libreria
        Thread.__init__(self, name = nombre)

    def run(self):
        n1 = randint(0,8)
        n2 = randint(0,8)

        while n2 == n1:
            n2 = randint(0,8)

        with self.libreria.c:
            while self.libreria.libros[n1] == True or self.libreria.libros[n2] == True:
                print(f"{self.name} espera para el libro {n1+1} y {n2+1} 📖🕵️")
                self.libreria.c.wait()
            self.libreria.libros[n1] = True
            self.libreria.libros[n2] = True
        print(f"{self.name} ha cogido {n1+1} y {n2+1} 👌📖")
        sleep(2)
        print(f"{self.name} ha devuelto {n1+1} y {n2+1} 😍📙")

        with self.libreria.c:
            self.libreria.libros[n1] = False
            self.libreria.libros[n2] = False
            self.libreria.c.notify_all()


if __name__ == "__main__":
    l = Libreria("Libreria")
    for i in range(1, 5):
        Estudiante(f"Estudiante {i}", l).start()





 