from telnetlib import DO
from pip._vendor import requests


def peticionGet(api_url, tipo):

    print("1. Recibir todos los datos ")
    print("2. Recibir un unico dato ")
    info = int(input("Que tipo de info quieres "))

    if info == 1:
        reponse = requests.get(api_url + "/" + tipo)
        print(reponse.json())

    elif info == 2:
        idD = input("Inserta el id del elemento ")
        reponse = requests.get(api_url + "/" + tipo + "/" + idD)
        print(reponse.json())
    else:
        print("Opcion no valida")


# reponse = requests.get(api_url)
# print(reponse.json())
# print(reponse.status_code)


def peticionPost(api_url, tipo):
    if tipo == "profesores":
        dni = input("DNI profesor ")
        nombre = input("Nombre del profesor ")
        apellidos = input("Apellidos del profesor ")
        tlf = int(input("Telefono del profesor "))
        calle = input("Direccion del profesor ")
        cuenta = int(input("Cuenta bancaria del profesor "))

        todo = {
            "DNI": dni,
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Telefono": tlf,
            "Direccion": calle,
            "CuentaBancaria": cuenta,
        }
        reponse = requests.post(api_url+"/"+tipo, json=todo)
        print(reponse.json())
        print("Code estado: ", reponse.status_code)

    elif tipo == "asignaturas":
        idAsig = int(input("Id de la asignatura "))
        titulo = input("Titulo de la asignatura ")
        numHoras = int(input("Horas de la asignatura "))
        idProf = int(input("Id del profesor "))

        todo = {
            "id": idAsig,
            "Titulo": titulo,
            "NumHoras": numHoras,
            "idProfesor": idProf,
        }
        reponse = requests.post(api_url+"/"+tipo, json=todo)

    else:
        print("Opcion no valida ")


def peticionPatch(api_url):
    print("Hacer PATCH")


def peticionPut(api_url, tipo):
    if tipo == "profesores":
        idProf = input("Id profesor ")
        dni = input("DNI profesor ")
        nombre = input("Nombre del profesor ")
        apellidos = input("Apellidos del profesor ")
        tlf = int(input("Telefono del profesor "))
        calle = input("Direccion del profesor ")
        cuenta = int(input("Cuenta bancaria del profesor "))

        todo = {
            "DNI": dni,
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Telefono": tlf,
            "Direccion": calle,
            "CuentaBancaria": cuenta,
        }
        reponse = requests.put(api_url+"/"+tipo+"/"+idProf, json=todo)

    elif tipo == "asignaturas":
        idAsig = int(input("Id de la asignatura "))
        titulo = input("Titulo de la asignatura ")
        numHoras = int(input("Horas de la asignatura "))
        idProf = int(input("Id del profesor "))

        todo = {
            "id": idAsig,
            "Titulo": titulo,
            "NumHoras": numHoras,
            "idProfesor": idProf,
        }
        reponse = requests.put(api_url, json=todo)

    else:
        print("Opcion no valida ")


def peticionDel(api_url):
    print("1. Profesor ")
    print("2. Asignatura ")
    opc = int(input("Que quieres borrar? "))

    if opc == 1:
        idProf = int(input("Id profesor "))
        api_url += ""

        print(f"Profesor {idProf} borrado ")

    elif opc == 2:
        idAsig = int(input("Id de la asignatura "))

        print(f"Asignatura {idAsig} borrada ")
    else:
        print("Opcion no valida ")
