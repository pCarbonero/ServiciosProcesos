import CrudApiRest

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
        CrudApiRest.peticionGet(api_url)

    elif (opc == 2):
        CrudApiRest.peticionPost(api_url)

    elif (opc == 3):
        CrudApiRest.peticionPatch(api_url)

    elif (opc == 4):
        CrudApiRest.peticionPut(api_url)

    elif (opc == 5):
        CrudApiRest.peticionDel(api_url)

    else:
        print("Opcion no valida")

    opc = mostrarMenu()

print("Gracias, hasta pronto. ")
