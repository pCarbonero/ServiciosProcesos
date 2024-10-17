from flask import *
import flask
from profesores.routes import devolverProf, profesoresBP
from asignaturas.routes import asignaturasBP, devolverAsig

app = Flask(__name__)

#get all
@app.get('/')
def get_all_():
    return jsonify(devolverProf(), devolverAsig())

app.register_blueprint(profesoresBP, url_prefix = '/profesores')
app.register_blueprint(asignaturasBP, url_prefix = '/asignaturas')