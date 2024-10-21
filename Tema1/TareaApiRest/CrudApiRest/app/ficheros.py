import json

def leerFichero(ruta):
    archivo = open(ruta, "r")
    objeto = json.load(archivo)
    archivo.close()
    return objeto


def escribirFichero(ruta, objeto):
    archivo = open(ruta, "w")
    json.dump(objeto, archivo)
    archivo.close()