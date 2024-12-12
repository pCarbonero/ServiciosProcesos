from multiprocessing import *
import time

def modificarVariable(num):
    suma = 0
    for i in range(1000):
        suma += 1
    return suma


if __name__ == "__main__":
    variable = 0
    with Pool(processes=4) as pool:
        limites = [1,1,1,1]
        results = pool.map(modificarVariable, limites)
    
    variable = sum(results)
    print(variable)