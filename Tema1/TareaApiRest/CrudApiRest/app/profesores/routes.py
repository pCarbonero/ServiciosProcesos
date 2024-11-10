from urllib import request
from flask import *

from app.ficheros import *



profesoresBP = Blueprint('profesores', __name__)

ficheroProfesores = "../CrudApiRest/app/profesores/profesores.json"


@profesoresBP.get('/')
def get_all_profesores():
    profesores = leerFichero(ficheroProfesores)
    return jsonify(profesores)

@profesoresBP.get("/<int:id>")
def get_profesores(id):
    profesores = leerFichero(ficheroProfesores)
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return {"error": "profesor not found"}, 404

@profesoresBP.get("/<int:id>/asignaturas") #este método Get
def get_asignaturasDeUnProfesor(id):
    asignaturas = leerFichero("../CrudApiRest/app/asignaturas/asignaturas.json")
    asignaturas_profesor = [asignatura for asignatura in asignaturas if asignatura.get('idProfesor') == id]
    if asignaturas_profesor:
        return jsonify(asignaturas_profesor), 200
    return {"error": "No se encontraron asignaturas para el profesor con el ID proporcionado"}, 404


def _find_next_idProf():
    profesores = leerFichero(ficheroProfesores)
    return max(profesor["id"] for profesor in profesores)+1



@profesoresBP.post("/")
def add_profesor():
    profesores = leerFichero(ficheroProfesores)
    if request.is_json:
        profesor = request.get_json()
        profesor["id"] = _find_next_idProf()
        profesores.append(profesor)
        escribirFichero(ficheroProfesores, profesores)
        return profesor, 201
    return {"error": "Request must be JSON"}, 415


@profesoresBP.put("/<int:id>")
@profesoresBP.patch("/<int:id>")
def modify_profesor(id):
    profesores = leerFichero(ficheroProfesores)
    if request.is_json:
        newProfesor = request.get_json()

        for profesor in profesores:
            if profesor["id"] == id:
                for elemento in newProfesor:
                    profesor[elemento] = newProfesor[elemento]
                return profesor, 200

@profesoresBP.delete("/<int:id>")
def del_profesor(id):
    profesores = leerFichero(ficheroProfesores)
    for profesor in profesores:
        if profesor["id"] == id:
            profesores.remove(profesor)
            return "{}", 200
    return {"error": "profesor no encontrado"}, 404