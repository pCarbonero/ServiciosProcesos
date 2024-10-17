from urllib import request
from flask import *

asignaturasBP = Blueprint('asignaturas', __name__)

asignaturas = [
    {"id": 1, "Titulo": "Lengua castellana", "NumHoras": "150", "idProfesor": 1},
    {"id": 2, "Titulo": "Historia de Espanya", "NumHoras": "120", "idProfesor": 2},
    {"id": 3, "Titulo": "Modelado 3D", "NumHoras": "140", "idProfesor": 3}
]


def devolverAsig():
    return asignaturas




@asignaturasBP.get('/')
def get_all_asignaturas():
    return jsonify(asignaturas)

@asignaturasBP.get("/<int:id>")
def get_asignaturas(id):
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return {"error": "asignatura no encontrada"}, 404

def _find_next_idAsig():
    return max(asignatura["id"] for asignatura in asignaturas)+1

@asignaturasBP.post("/")
def add_asignatura():
    if request.is_json:
        asignatura = request.get_json()
        asignatura["id"] = _find_next_idAsig()
        asignaturas.append(asignatura)
        return asignatura, 201
    return {"error": "Request must be JSON"}, 415

@asignaturasBP.put("/<int:id>")
@asignaturasBP.patch("/<int:id>")
def modify_asignatura(id):
    if request.is_json:
        newAsignatura = request.get_json()

        for asignatura in asignaturas:
            if asignatura["id"] == id:
                for elemento in newAsignatura:
                    asignatura[elemento] = newAsignatura[elemento]
                return asignatura, 200

@asignaturasBP.delete("/<int:id>")
def del_asignatura(id):
    for asignatura in asignaturas:
        if asignatura["id"] == id:
            asignaturas.remove(asignatura)
            return "{}", 200
    return {"error": "asignatura no encontrada"}, 404