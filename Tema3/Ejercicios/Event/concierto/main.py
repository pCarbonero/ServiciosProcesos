from time import *
from threading import *
from random import *
from Empresa import *
from Comprador import *


if __name__ == "__main__":
    empresa = Empresa("Empresa", Event())
    empresa.start()
    for i in range(10):
        Comprador(f"Persona {i+1}", empresa).start()