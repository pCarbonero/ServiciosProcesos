from telnetlib import DO
from pip._vendor import requests


def profesoresGet(api_url):       

    print("1. Todos los profesores ")
    print("2. Un unico profesor ")
    info = int(input("Que tipo de info quieres "))

    if (info == 1):
        reponse = requests.get(api_url + "/profesores")
        print(reponse.json())

    elif (info == 2):
        idProf = input("Inserta el id del profesor ")
        reponse = requests.get(api_url + "/profesores/" + idProf)
        print(reponse.json())
    else:
        print("Opcion no valida")


        # reponse = requests.get(api_url)
        # print(reponse.json())
        # print(reponse.status_code)