from multiprocessing import *
import time

def suma(limite):
    i = 0
    print (f"n = {limite}")
    for num in range (1, limite+1):
        i+=num
        print("Suma de todos los valores hasta el " + str(num)+ " = " + str(i))
        time.sleep(1)

if __name__ == "__main__":
    with Pool(processes=1) as pool:
        limites = [5,3,10]
        results = pool.map(suma, limites)
    print("Han terminado todos los procesos")