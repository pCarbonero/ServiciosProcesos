from funciones import *

def menu():
    print("1. Mostrar todas las publicaciones ")
    print("2. Mostrar una publicacion concreta ")
    print("3. Anadir una nueva publicacion ")
    print("4. Modificar todos los datos de una publicacion ")
    print("5. Modificar un dato concreto de una publicacion")
    print("6. Eliminar una publicacion")
    print("0. Salir de la aplicacion")
    opc = int(input("Elige una opcion "))
    return opc



def main():
    opc = -1
    url = "https://jsonplaceholder.typicode.com"
    
    while opc != 0:
        opc = menu()
        if opc == 1:
            response, status = todasPublicaciones(url)
            if status == 200:
                imprimirJson(response)

        elif opc == 2:
            idP = int(input("Inserta el id de la publicacion: "))
            response, status = unaPublicacion(url, idP)
            if status == 200:
                imprimirUnico(response)
            else:
                print("AAAAAAAAAAAAAAAAAAAAAASDFNKSJDVKJVCOKDHVKAJSDVBKJN")
                
        elif opc == 3:
            idUser = int(input("Id usuario "))
            title = input("Inserta el titulo del post ")
            body = input("Inserta el cuerpo del Post ")

            response, status = addPost(url, idUser, title, body)
            if status == 200 or status == 201:
                imprimirUnico(response)
            else:
                print("AAAAAAAAAAAAAAAAAAAAAASDFNKSJDVKJVCOKDHVKAJSDVBKJN")

        elif opc == 4:
            idPost = int(input("Id publicacion "))
            idUser = int(input("Id usuario "))
            title = input("Inserta el titulo del post ")
            body = input("Inserta el cuerpo del Post ")

            response, status = modFullPost(url, idPost, idUser, title, body)
            if status == 200 or status == 201:
                imprimirUnico(response)

        elif opc == 5:
            idPost = int(input("Id publicacion "))
            print("1. Id usuario ")
            print("2. Titulo ")
            print("3. Cuerpo")
            dato = ""
            opc2 = int(input("Que quieres modificar "))

            if opc2 == 1:
                dato = "userId"
            elif opc2 == 2:
                dato = "title"
            elif opc2 == 3:
                dato = "body"

            mod = input("Inserta el nuevo " + dato)

            response, status = modPost(url, idPost, dato, mod)
            if status == 200 or status == 201:
                imprimirUnico(response)

        elif opc == 6:
            idPost = int(input("Id publicacion "))
            response, status = delPost(url, idPost)
            if status == 200 or status == 204 or status == 201:
                print("BOrrado correctamente")
            else: 
                print("Eerrou")
             


    print("Hasta pronto")
        

if __name__ == "__main__":
    main()
