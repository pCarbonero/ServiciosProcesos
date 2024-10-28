from pip._vendor import requests
from telnetlib import DO

def userLogin(url, user, password):
    response = requests.post(
    url+"/users/login", json={"username": user, "password": password},
    headers={"Content-Type": "application/json"})
    token = response.json().get("token")
    print(response.json())
    print("Code estado: ", response.status_code)
    return token

def getProfesores(url, token):
    try:
        response = requests.get(url+"/profesores", headers={"Authorization": "Bearer " + token})
        if response.status_code == 200:
            print(response.json())
        else:
            print("Se ha producido un error")
    except Exception as e:
        print(e)
   



user = input("Usuario: ")
password = input("Contrasena: ")
url = "http://127.0.0.1:5050"

token = userLogin(url, user, password)

getProfesores(url, token)