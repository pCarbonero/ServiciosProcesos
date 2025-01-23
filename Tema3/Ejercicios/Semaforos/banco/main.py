from banco import *

if __name__ == "__main__":
    for i in range(1, 11):
        Banco(f"Persona {i}").start()