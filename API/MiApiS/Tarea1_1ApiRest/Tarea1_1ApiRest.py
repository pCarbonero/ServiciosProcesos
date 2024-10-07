from ast import Num
from http.client import SWITCHING_PROTOCOLS
from telnetlib import DO
from unittest import case
from pip._vendor import requests




    
#funciones

def peticionGet():
    #api_url += "/profesores"

    print("1. Profesores ")
    print("2. Asignaturas ")
    info = int(input("Que quieres? "))

    if (info == 1):
        print("1. Todos los profesores ")
        print("2. Un unico profesor ")

        info = int(input("Que tipo de info quieres "))

        if (info == 1):
            api_ur += "/profesores"
            print("Info profes ")

        elif (info == 2):
            idProf = input("Inserta el id del profesor ")
            api_ur += "/profesores/" + idProf   
            print("Info profe " + idProf)
        else:
            print("Opcion no valida")
            
    elif (info == 2):
        print("1. Todas las asignaturas")
        print("2. Una asigatura")
        print("3. Asignaturas de un profe")
        info = int(input("Que tipo de info quieres "))

        if (info == 1):
            api_ur += "/profesores/asignaturas"
            print("Info asignaturas ")

        elif (info == 2):
            idAsig = input("Inserta el id de la asignatura ")
            api_ur += "/profesores/asignaturas" + idAsig
            print("Info asignatura " + idAsig)

        elif (info == 3):
            idProf = input("De que profesor? ")
            api_ur += "/profesores/" + idProf + "/asignaturas"
            print("Asignaturas del profesor " + idProf)
        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida")


    # reponse = requests.get(api_url)
    # print(reponse.json())
    # print(reponse.status_code)

def peticionPost():
    print("1. Profesor ")
    print("2. Asignatura ")
    opc = int(input("Que quieres anyadir? "))

    if (opc == 1):
        idProf = int(input("Id profesor "))
        dni = input("DNI profesor ")
        nombre = input("Nombre del profesor ")
        apellidos = input("Apellidos del profesor ")
        tlf = int(input("Telefono del profesor "))
        cuenta = int(input("Cuenta bancaria del profesor "))

        print(f"NUEVO PROFESOR: {idProf}, {dni}, {nombre}, {apellidos}, {tlf}, {cuenta} ")

    elif (opc == 2):
        idAsig = int(input("Id de la asignatura "))
        titulo = input("Titulo de la asignatura ")
        numHoras = int(input("Horas de la asignatura "))
        idProf = int(input("Id del profesor "))

        print(f"NUEVO PROFESOR: {idAsig}, {titulo}, {numHoras}, {idProf} ")

    else:
        print("Opcion no valida ")


def peticionPatch():
    print("Hacer PATCH")

def peticionPut(api_url):
    oldIdProf = input("Id profesor que quieres modificar ")
    newIdProf = input("Id profesor ")
    dni = int(input("DNI profesor "))
    nombre = input("Nombre del profesor ")
    apellidos = input("Apellidos del profesor ")
    tlf = int(input("Telefono del profesor "))
    cuenta = int(input("Cuenta bancaria del profesor "))
    
    api_url += "/profesores/" + oldIdProf

    print(f"PROFESOR {oldIdProf} MODIFICADO A: {newIdProf}, {dni}, {nombre}, {apellidos}, {tlf}, {cuenta} ")
    

def peticionDel():
    print("1. Profesor ")
    print("2. Asignatura ")
    opc = int(input("Que quieres borrar? "))
    
    if (opc == 1):
        idProf = int(input("Id profesor "))
        api_url += ""

        print(f"Profesor {idProf} borrado ")

    elif (opc == 2):
        idAsig = int(input("Id de la asignatura "))

        print(f"Asignatura {idAsig} borrada ")
    else:
        print("Opcion no valida ")

def mostrarMenu():
    api_url = "http://nada.com"
    print("1. Recibir informacion (GET)")
    print("2. Mandar informcion (POST)")
    print("3. Actualizar informacion (PATCH)")
    print("4. Reemplazar informacion (PUT)")
    print("5. Borrar informacion (DEL)")
    print("0. Salir")
    opc = int(input("Indica que opcion quieres realizar "))
    return opc


opc = mostrarMenu()

while opc != 0:

    api_url = "https://urlfalsa.algo.com"
    if (opc == 1):
        peticionGet()

    elif (opc == 2):
        peticionPost()

    elif (opc == 3):
        peticionPatch()

    elif (opc == 4):
        peticionPut(api_url)

    elif (opc == 5):
        peticionDel()

    elif (opc == 0):
        print("Gracias, hasta pronto")

    else:
        print("Opcion no valida")

    opc = mostrarMenu()

    





