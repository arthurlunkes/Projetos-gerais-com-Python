from flask import Flask, jsonify
from conexao_bd import consultar

app = Flask(__name__)

sql = '''SELECT * FROM CURSO'''

#Obtem todos os usuários
@app.route('/usuarios',methods=['GET'])
def obter_usuarios():
    return jsonify(consultar(sql=sql))

#rodar servidor
app.run(port=5000,host='localhost',debug=True)