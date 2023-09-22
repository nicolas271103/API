import random
from flask import Flask, jsonify, make_response, request
from newcadastro import Cadastro

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/lista_cadastrados', methods=['GET'])
def index():
    return make_response (
        jsonify(
            mensagem='Lista de cadastros.',
            dados=Cadastro
        )
    )

@app.route('/cadastro', methods=['POST'])
def create_cadastro():
    cadastro = request.json
    return "200ok"


app.run(port=8000, host='localhost', debug=True)
