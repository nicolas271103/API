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
            cadastro=Cadastro
        )
    )

@app.route('/cadastro', methods=['POST'])
def create_cadastro():
    cadastro = request.json
    Cadastro.append(cadastro)
    return "Processo Cadastrado com sucesso!!"


@app.route('/update', methods=['PUT'])
def update_cadastro():
    cadastro = request.get_json()
    return "Processo Atualizado com sucesso!!"

@app.route('/cadastros/<int:cadastro_id>', methods=['DELETE'])
def delete_cadastro(cadastro_id):
    cadastro = next((c for c in cadastros if c['id'] == cadastro_id), None)

    if cadastro is None:
        return jsonify({"mensagem": "Cadastro não encontrado"}), 404

    cadastros.remove(cadastro)
    return jsonify({"mensagem": "Cadastro removido com sucesso"})

    cadastro.remove(cadastro)
    # i = 0
    # for id in Cadastro:
    #     if cadastro == Cadastro[i]:
    #         Cadastro.pop(i)
    #         return "Processo Excluido com sucesso!!"
    #     i = i + 1
    #
    # return "Item inexistente!!"

@app.route('/')

app.run(port=8000, host='localhost', debug=True)
