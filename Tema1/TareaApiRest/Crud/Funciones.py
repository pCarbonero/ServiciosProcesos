from pip._vendor import requests
from telnetlib import DO

def userLogin(url, user, password):
    response = requests.post(
    url+"/users/login", json={"username": user, "password": password},
    headers={"Content-Type": "application/json"})
    token = response.json().get("token")
    #print(response.json())
    #print("Code estado: ", response.status_code)
    return token, response.status_code

def getProfesores(url, token):
    try:
        response = requests.get(url+"/profesores", headers={"Authorization": "Bearer " + token})
        if response.status_code == 200:
            print(response.json())
        else:
            print("Se ha producido un error")
    except Exception as e:
        print(e)