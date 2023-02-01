__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'

import re
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config[
    "SECRET_KEY"
] = "1dafafghsdsf5378167uevsbg423)(dfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
app.secret_key = "test_secret"


@app.route("/get_tecnicos", methods=["GET"])
def get_tecnicos():
    """solicitud para obtener la información de todos los tecnicos

    Returns:
        json: estructura con la información de los tecnicos
    """
    tecnicos = Tecnico.get_all()
    response = []
    for tecnico in tecnicos:
        response.append(dict(tecnico))
    return make_response(jsonify(response))



if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)
