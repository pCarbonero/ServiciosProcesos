# -*- coding: utf-8 -*-
from http.client import SWITCHING_PROTOCOLS
from telnetlib import DO
from unittest import case
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"


#funciones

def peticionGet():
    print("Hacer GET")
    # reponse = requests.get(api_url)
    # print(reponse.json())
    # print(reponse.status_code)

def peticionPost():
    print("Hacer POST")

def peticionPatch():
    print("Hacer PATCH")

def peticionPut():
    print("Hacer PUT")

def peticionDel():
    print("Hacer DEL")




print("1. Recibir informacion (GET)")
print("2. Mandar informcion (POST)")
print("3. Actualizar informacion (PATCH)")
print("4. Reemplazar informacion (PUT)")
print("5. Borrar informacion (DEL)")
print("0. Salir")
opc = int(input("Indica que opcion quieres realizar "))




while opc != 0:
    if (opc == 1):
        peticionGet()

    elif (opc == 2):
        peticionPost()

    elif (opc == 3):
        peticionPatch()

    elif (opc == 4):
        peticionPut()

    elif (opc == 5):
        peticionDel()

    else:
        print("Opcion no valida")

    opc = int(input("Indica que opcion quieres realizar "))

print("Gracias, hasta pronto")



