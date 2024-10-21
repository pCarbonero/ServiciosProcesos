from flask import *
import flask
from flask.typing import URLValuePreprocessorCallable
from profesores.routes import devolverProf, profesoresBP
from asignaturas.routes import asignaturasBP, devolverAsig
from users.routes import usersBP
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "clave_secreta"
jwt = JWTManager(app)

app.register_blueprint(usersBP, url_prefix='/users')


#get all
@app.get('/')
def get_all_():
    return jsonify(devolverProf(), devolverAsig())

app.register_blueprint(profesoresBP, url_prefix = '/profesores')
app.register_blueprint(asignaturasBP, url_prefix = '/asignaturas')