from flask import *

app = Flask(__name__)


profesores = [
    {"id": 1, "DNI": "25426598P", "Nombre": "Diego", "Apellidos": "Simeone Pozo", "Telefono": 321654987, "Direccion": "C/ Lisboa 55", "CuentaBancaria": 123654789}
]

asignaturas = [
    {"id": 1, "Titulo": "Lengua castellana", "NumHoras": "150", "idProfesor": 1}
]

@app.get('/profesores')
def get_all_profesores():
    return jsonify(profesores)

@app.route('/')
@app.get("/profesores/<int:id>")
def get_countries(id):
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return {"error": "profesor not found"}, 404


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

if __name__ == '__main__':
   app.run(debug=True, host = '0.0.0.0', port = 5050)