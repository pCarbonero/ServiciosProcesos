from multiprocessing import *
import time


# que? sin pool? waaat con qeue  
def suma(numero):
    i = 0
    print (f"n = {numero}")
    for num in range (1, numero+1):
        i+=num
        print("Suma de todos los valores hasta el " + str(num)+ " = " + str(i))
        time.sleep(1)

if __name__ == "__main__":
    with Pool(processes=1) as pool:
        numeros = [5,3,10]
        results = pool.map(suma, numeros)
    print("Han terminado todos los procesos")