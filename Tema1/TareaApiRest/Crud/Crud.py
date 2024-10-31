from pip._vendor import requests
from telnetlib import DO
from Funciones import *

# def userLogin(url, user, password):
#     response = requests.post(
#     url+"/users/login", json={"username": user, "password": password},
#     headers={"Content-Type": "application/json"})
#     token = response.json().get("token")
#     print(response.json())
#     print("Code estado: ", response.status_code)
#     return token

# def getProfesores(url, token):
#     try:
#         response = requests.get(url+"/profesores", headers={"Authorization": "Bearer " + token})
#         if response.status_code == 200:
#             print(response.json())
#         else:
#             print("Se ha producido un error")
#     except Exception as e:
#         print(e)
  

def login(url):
    status = 0
    while status != 201:
        user = input("Usuario: ")
        password = input("Contrasena: ")
        token, status = userLogin(url, user, password)
        return token

def menu():
    print("1. Obtener información")
    print("0. Salir")
    



def main():
    url = "http://127.0.0.1:5050"   
    token = login(url)
    menu()
    #pedir inicio de sesion
    

    


if __name__ == "__main__":
    main()