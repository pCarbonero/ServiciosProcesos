from urllib import request
from flask import *

from app import asignaturas
from asignaturas.routes import *

profesoresBP = Blueprint('profesores', __name__)


profesores = [
    {"id": 1, "DNI": "25426598P", "Nombre": "Diego", "Apellidos": "Simeone Pozo", "Telefono": 321654987, "Direccion": "C/ Lisboa 55", "CuentaBancaria": 123654789},
    {"id": 2, "DNI": "33326598B", "Nombre": "Jose Maria", "Apellidos": "Gracia Marquez", "Telefono": 194536590, "Direccion": "C/ Marques de Nervion 34", "CuentaBancaria": 333546877},
    {"id": 3, "DNI": "12546397M", "Nombre": "Marcos", "Apellidos": "Busatori", "Telefono": 256987413, "Direccion": "C/ Malomontano 1", "CuentaBancaria": 986532147}
]


def devolverProf():
    return profesores

@profesoresBP.get('/')
def get_all_profesores():
    return jsonify(profesores)

@profesoresBP.get("/<int:id>")
def get_profesores(id):
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return {"error": "profesor not found"}, 404

@profesoresBP.get('/<int:id>/asignaturas')
def get_asigProfesor(id):
    list = []
    asig = asignaturas.devolverAsig()

    for asignatura in asignaturas:
        if asignatura['id'] == id:
            list.append(asignatura)
    if len(list) > 0:
        return list,200
    else:
        return {"error": "nosduwe"}, 404







def _find_next_idProf():
    return max(profesor["id"] for profesor in profesores)+1



@profesoresBP.post("/")
def add_profesor():
    if request.is_json:
        profesor = request.get_json()
        profesor["id"] = _find_next_idProf()
        profesores.append(profesor)
        return profesor, 201
    return {"error": "Request must be JSON"}, 415


@profesoresBP.put("/<int:id>")
@profesoresBP.patch("/<int:id>")
def modify_profesor(id):
    if request.is_json:
        newProfesor = request.get_json()

        for profesor in profesores:
            if profesor["id"] == id:
                for elemento in newProfesor:
                    profesor[elemento] = newProfesor[elemento]
                return profesor, 200

@profesoresBP.delete("/<int:id>")
def del_profesor(id):
    for profesor in profesores:
        if profesor["id"] == id:
            profesores.remove(profesor)
            return "{}", 200
    return {"error": "profesor no encontrado"}, 404