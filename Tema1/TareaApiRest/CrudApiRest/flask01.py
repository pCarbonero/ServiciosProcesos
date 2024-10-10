from urllib import request
from flask import *

app = Flask(__name__)


profesores = [
    {"id": 1, "DNI": "25426598P", "Nombre": "Diego", "Apellidos": "Simeone Pozo", "Telefono": 321654987, "Direccion": "C/ Lisboa 55", "CuentaBancaria": 123654789},
    {"id": 2, "DNI": "33326598P", "Nombre": "Jose Maria", "Apellidos": "Gracia Marquez", "Telefono": 194536590, "Direccion": "C/ Marques de Nervion 34", "CuentaBancaria": 333546877}
]

asignaturas = [
    {"id": 1, "Titulo": "Lengua castellana", "NumHoras": "150", "idProfesor": 1},
    {"id": 2, "Titulo": "Historia de Espanya", "NumHoras": "120", "idProfesor": 2}
]


#region get
@app.get('/profesores')
def get_all_profesores():
    return jsonify(profesores)

@app.route('/')
@app.get("/profesores/<int:id>")
def get_profesores(id):
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return {"error": "profesor not found"}, 404

@app.get('/asignaturas')
def get_all_asignaturas():
    return jsonify(asignaturas)

@app.route('/')
@app.get("/asignaturas/<int:id>")
def get_asignaturas(id):
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return {"error": "profesor not found"}, 404

#endregion  


def _find_next_id():
    return max(profesor["id"] for profesor in profesores)+1



@app.post("/profesores")
def add_profesor():
    if request.is_json:
        profesor = request.get_json()
        profesor["id"] = _find_next_id()
        profesores.append(profesor)
        return profesor, 201
    return {"error": "Request must be JSON"}, 415


@app.put("/profesores/<int:id>")
def modify_profesor(id):
    if request.is_json:
        newProfesor = request.get_json()

        for profesor in profesores:
            if profesor["id"] == id:
                for elemento in newProfesor:
                    profesor[elemento] = newProfesor[elemento]
                return profesor, 200

@app.delete("/profesores/<int:id>")
def del_profesor(id):
    for profesor in profesores:
        if profesor["id"] == id:
            profesores.remove(profesor)
            return "{}", 200
    return {"error": "profesor no encontrado"}, 404

if __name__ == '__main__':
   app.run(debug=True, host = '0.0.0.0', port = 5050)