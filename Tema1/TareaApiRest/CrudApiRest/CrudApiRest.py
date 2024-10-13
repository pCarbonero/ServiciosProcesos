from telnetlib import DO
from pip._vendor import requests


def peticionGet(api_url, tipo):

    print("1. Recibir todos los datos ")
    print("2. Recibir un unico dato ")
    info = int(input("Que tipo de info quieres "))

    if info == 1:
        reponse = requests.get(api_url + "/" + tipo)
        print(reponse.json())
        print("Code estado: ", reponse.status_code)

    elif info == 2:
        idD = input("Inserta el id del elemento ")
        reponse = requests.get(api_url + "/" + tipo + "/" + idD)
        print(reponse.json())
        print("Code estado: ", reponse.status_code)
    else:
        print("Opcion no valida")


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
        titulo = input("Titulo de la asignatura ")
        numHoras = int(input("Horas de la asignatura "))
        idProf = int(input("Id del profesor "))

        todo = {
            "Titulo": titulo,
            "NumHoras": numHoras,
            "idProfesor": idProf,
        }
        reponse = requests.post(api_url+"/"+tipo, json=todo)
        print(reponse.json())
        print("Code estado: ", reponse.status_code)

    else:
        print("Opcion no valida ")


def peticionPatch(api_url, tipo):
    idE = input("Que id quieres modificar ")
    

    if tipo == "profesores":
        print("1. Nombre")
        print("2. Apellidos")
        print("3. DNI")
        print("4. Direccion")
        print("5. Telefono")
        print("6. Cuenta Bancaria")
        opc = int(input("Que quieres modificar? "))

        if opc == 1:
            mod = input("Nuevo nombre ")
            todo = {"Nombre": mod}
        elif opc == 2:
            mod = input("Nuevos apellidos ")
            todo = {"Apellidos": mod}
        elif opc == 3:
            mod = input("Nuevo DNI ")
            todo = {"DNI": mod}
        elif opc == 4:
            mod = input("Nueva direccion ")
            todo = {"Direccion": mod}
        elif opc == 5:
            mod = int(input("Nuevo telefono "))
            todo = {"Telefono": mod}
        elif opc == 6:
            mod = int(input("Nueva cuenta bancaria "))
            todo = {"CuentaBancaria": mod}
        else:
            print("Opcion no valida")

    elif tipo == "asignaturas":
        print("1. Titulo ")
        print("2. Numero de horas ")
        print("3. Id profesor ")
        opc = int(input("Que quieres modificar? "))

        if opc == 1:
            mod = input("Nuevo titulo ")
            todo = {"Titulo": mod}
        elif opc == 2:
            mod = input("Nuevo numero de horas ")
            todo = {"NumHoras": mod}
        elif opc == 3:
            mod = int(input("Nuevo id profesor "))
            todo = {"DNI": mod}
        else:
            print("Opcion no valida")

    reponse = requests.patch(api_url+"/"+tipo+"/"+idE, json=todo)



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
        print(reponse.json())
        print("Code estado: ", reponse.status_code)

    elif tipo == "asignaturas":
        idAsig = input("Id de la asignatura ")
        titulo = input("Titulo de la asignatura ")
        numHoras = int(input("Horas de la asignatura "))
        idProf = int(input("Id del profesor "))

        todo = {
            "Titulo": titulo,
            "NumHoras": numHoras,
            "idProfesor": idProf,
        }
        reponse = requests.put(api_url+"/"+tipo+"/"+idAsig, json=todo)
        print(reponse.json())
        print("Code estado: ", reponse.status_code)

    else:
        print("Opcion no valida ")


def peticionDel(api_url,tipo):
    idE = input("Id del elemento que quieres borrar ")

    reponse = requests.delete(api_url+"/"+tipo+"/"+idE)
    print(reponse.json())
    print("Code estado: ", reponse.status_code)
