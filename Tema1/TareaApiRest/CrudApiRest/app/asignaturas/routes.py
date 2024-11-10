from urllib import request
from flask import *

from app.ficheros import escribirFichero, leerFichero

asignaturasBP = Blueprint('asignaturas', __name__)

ficheroAsignaturas = "../CrudApiRest/app/asignaturas/asignaturas.json"

@asignaturasBP.get('/')
def get_all_asignaturas():
    asignaturas = leerFichero(ficheroAsignaturas)
    return jsonify(asignaturas)

@asignaturasBP.get("/<int:id>")
def get_asignaturas(id):
    asignaturas = leerFichero(ficheroAsignaturas)
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return {"error": "asignatura no encontrada"}, 404

# @asignaturasBP.get("/profesores/<int:id>") #este método Get
# def get_asignaturasDeUnProfesor(id):
#     asignaturas = leerFichero(ficheroAsignaturas)
#     asignaturas_profesor = [asignatura for asignatura in asignaturas if asignatura.get('idProfesor') == id]
#     if asignaturas_profesor:
#         return jsonify(asignaturas_profesor), 200
#     return {"error": "No se encontraron asignaturas para el profesor con el ID proporcionado"}, 404

def _find_next_idAsig():
    asignaturas = leerFichero(ficheroAsignaturas)
    return max(asignatura["id"] for asignatura in asignaturas)+1

@asignaturasBP.post("/")
def add_asignatura():
    asignaturas = leerFichero(ficheroAsignaturas)
    if request.is_json:
        asignatura = request.get_json()
        asignatura["id"] = _find_next_idAsig()
        asignaturas.append(asignatura)
        escribirFichero(ficheroAsignaturas, asignaturas)
        return asignatura, 201
    return {"error": "Request must be JSON"}, 415

@asignaturasBP.put("/<int:id>")
@asignaturasBP.patch("/<int:id>")
def modify_asignatura(id):
    asignaturas = leerFichero(ficheroAsignaturas)
    if request.is_json:
        newAsignatura = request.get_json()

        for asignatura in asignaturas:
            if asignatura["id"] == id:
                for elemento in newAsignatura:
                    asignatura[elemento] = newAsignatura[elemento]
                return asignatura, 200

@asignaturasBP.delete("/<int:id>")
def del_asignatura(id):
    asignaturas = leerFichero(ficheroAsignaturas)
    for asignatura in asignaturas:
        if asignatura["id"] == id:
            asignaturas.remove(asignatura)
            return "{}", 200
    return {"error": "asignatura no encontrada"}, 404