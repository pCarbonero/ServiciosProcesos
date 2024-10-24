from flask import *
import flask
from flask.typing import URLValuePreprocessorCallable
from app.profesores.routes import profesoresBP
from app.asignaturas.routes import asignaturasBP
from app.users.routes import usersBP
from flask_jwt_extended import JWTManager
from app.ficheros import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "clave_secreta"
jwt = JWTManager(app)

app.register_blueprint(profesoresBP, url_prefix='/profesores')
app.register_blueprint(asignaturasBP, url_prefix='/asignaturas')
app.register_blueprint(usersBP, url_prefix='/users')


# #get all
@app.get('/')
def get_all_():
    return jsonify(leerFichero("app/profesores/profesores.json"), leerFichero("app/asignaturas/asignaturas.json"),
                   leerFichero("app/users/users.json"))
