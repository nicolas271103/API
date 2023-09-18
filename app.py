import random

from flask import Flask, jsonify

app = Flask(__name__)

curriculos = [
    {
        "id": random.random(),
        "responsavel": "Pedro"
    },
]


@app.route('/curriculos')
def index():
    return jsonify(curriculos)


app.run(port=8000, host='localhost', debug=True)
