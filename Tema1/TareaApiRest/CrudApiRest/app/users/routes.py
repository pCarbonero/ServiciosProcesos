from tokenize import generate_tokens
import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import *
from app.ficheros import escribirFichero, leerFichero

ficheroUsers = "../CrudApiRest/app/users/users.json"

usersBP = Blueprint('users', __name__)

dict = {"username": 'manolo', "password": '1234'}

@usersBP.post('/')
def registerUser():
    users = leerFichero(ficheroUsers)
    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()
        user['password'] = hashPassword
        users.append(user)
        escribirFichero(ficheroUsers,users)
        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415

@usersBP.get('/')
def loginUser():
    misUsers = leerFichero(ficheroUsers)
    if request.is_json:
        userGet = request.get_json()
        for usuario in misUsers:
            if usuario["username"] == userGet["username"]:
                   password = userGet["password"].encode('utf-8')                 
                   if usuario["password"] == password:
                       token = create_access_token(identity = userGet["username"])
                       return {"token": token}, 201                         
        return {"error": "Contrasena y/o usuario incorrectos"}, 401
    else:
        return {"error": "Request must be JSON"}, 415
