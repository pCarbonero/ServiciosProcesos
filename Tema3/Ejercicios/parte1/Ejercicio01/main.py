from hilosTrabajadores import Trabajador

if __name__ == "__main__":

    nombres = ["Pablo", "Sara", "Marco", "Raul", "Lorenzo"]
    
    for i in range(5):
        t = Trabajador(nombres[i])
        t.start()