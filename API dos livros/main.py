from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Harry Potter'
    },
    {
        'id': 2,
        'título': 'Senhor dos anéis'
    },
    {
        'id': 3,
        'título': 'Atitude mental positiva'
    }
]

#Obtem todos os livros
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Obtem o livro por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Altera um livro existente por id
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Cria um livro
@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Exclui um livro por id
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)