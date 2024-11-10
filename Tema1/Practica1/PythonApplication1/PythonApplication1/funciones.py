from ast import Str
from pip._vendor import requests
from pip._vendor.urllib3.exceptions import RequestError

def imprimirJson(listaObjetos):
    for objeto in listaObjetos:
        print("-----------------")
        print(objeto) 
        print("-----------------\n")

def imprimirUnico(objeto):
    print("-----------------")
    print(objeto) 
    print("-----------------\n")


def todasPublicaciones(url):
    response = requests.get(url + "/posts")
    print(response.status_code)
    return response.json(), response.status_code

def unaPublicacion(url, idP):
    response = requests.get(url + "/posts/" + str(idP))
    print(response.json())
    print(response.status_code)
    return response.json(), response.status_code

def addPost(url, userId, title, body):
    post = {"userId": userId, "title": title, "body": body}
    response = requests.post(url + "/posts", json=post)

    # print(response.json()["id"])

    return response.json(), response.status_code

def modFullPost(url, postId, userId, title, body):
    put = {"userId": userId, "title": title, "body": body}
    response = requests.put(url + "/posts/" + str(postId), json=put)

    return response.json(), response.status_code

def modPost(url, postId, dato, mod):
    patch = {dato: mod}
    response = requests.put(url + "/posts/" + str(postId), json=patch)

    return response.json(), response.status_code

def delPost(url, postId):
    response = requests.delete(url + "/posts/" + str(postId))
    return response.json(), response.status_code




# def imprimirJson(listaObjetos):
#     if isinstance(listaObjetos, list):  # Verifica si es una lista
#         for objeto in listaObjetos:
#             print("-----------------")
#             print(objeto)
#             print("-----------------\n")
#     else:  # Si no es una lista, asume que es un solo objeto
#         print("-----------------")
#         print(listaObjetos)
#         print("-----------------\n")