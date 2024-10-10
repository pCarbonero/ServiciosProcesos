import CrudApiRest

def mostrarMenu():
    print("1. Recibir informacion (GET)")
    print("2. Mandar informcion (POST)")
    print("3. Actualizar informacion (PATCH)")
    print("4. Reemplazar informacion (PUT)")
    print("5. Borrar informacion (DEL)")
    print("0. Salir")
    opc = int(input("Indica que opcion quieres realizar "))
    return opc

def elegirTipo():
    tipo = ""

    print("1. Profesores")
    print("2. Asignaturas")
    opc = int(input("Indica el tipo de informacion que quieres manejar "))

    if (opc == 1):
        tipo = "profesores"
    else:
        tipo = "asignaturas"
    return tipo


opc = mostrarMenu()

while opc != 0:

    api_url = "http://127.0.0.1:5050"

    tipo = elegirTipo()


    if (opc == 1):
        CrudApiRest.peticionGet(api_url, tipo)

    elif (opc == 2):
        CrudApiRest.peticionPost(api_url, tipo)

    elif (opc == 3):
        CrudApiRest.peticionPatch(api_url)

    elif (opc == 4):
        CrudApiRest.peticionPut(api_url, tipo)

    elif (opc == 5):
        CrudApiRest.peticionDel(api_url)

    else:
        print("Opcion no valida")

    opc = mostrarMenu()

print("Gracias, hasta pronto. ")
