__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'

import re
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from components.models import Cancion

app = Flask(__name__)
CORS(app)
app.config[
    "SECRET_KEY"
] = "1dafafghsdsf5378167uevsbg423)(dfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
app.secret_key = "test_secret"


@app.route("/get_all", methods=["GET"])
def get_all():
    """

    Returns:
        json: estructura con la información de los tecnicos
    """
    canciones = Cancion.get_all()
    app.logger.info(canciones)
    response = []
    for cancion in canciones:
        
        response.append({
        "id":cancion[0],
        "nombre":cancion[1],
        "duracion":cancion[2],
        "artista":cancion[3],
        "album":cancion[4],
        "calificaion":cancion[5]
    })
    
    return make_response(jsonify(response))

@app.route("/delete", methods=["DELETE"])
def delete():
    """
    metodo para eliminar una canción 
    cancion : {
        id:id,
    }
    Returns:
        json: retorna el estado de la  solicitud
    """
    cancion = request.json["cancion"]
    app.logger.info(cancion)
    status = Cancion.delete(cancion)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 200)
    return make_response(jsonify({"response": "ok"}), 200)
    
@app.route("/add_new", methods=["POST"])
def add_new():
    """
    metodo para agregar una canción 
    cancion : {
        id:id,
        nombre:nombre(str),
        duracion:salario(str),
        artista:sucursal_id(str),
        album:album(str),
        calificaion:calificaion(int)
    }
    Returns:
        json: retorna el estado de la  solicitud
    """
    cancion = request.json["cancion"]
    app.logger.info(cancion)
    status = Cancion.instert(cancion)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 200)
    return make_response(jsonify({"response": "ok"}), 200)


@app.route("/update", methods=["PUT"])
def update():
    """
    metodo para actualizar una canción 
    cancion : {
        id:id,
        nombre:nombre(str),
        duracion:salario(str),
        artista:sucursal_id(str),
        album:album(str),
        calificaion:calificaion(int)
    }
    Returns:
        json: retorna el estado de la  solicitud
    """
    cancion = request.json["cancion"]
    app.logger.info(cancion)
    status = Cancion.update(cancion)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 200)
    return make_response(jsonify({"response": "ok"}), 200)
if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)
