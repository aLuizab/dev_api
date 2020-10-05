from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id': 0,
     'nome': 'Ana',
     'habilidades': ['Python', 'Flask']
     },
    {'id': 1,
     'nome': 'Luiza',
     'habilidades': ['Python', 'Linux']}

]
#devolve um dev pelo ID, também altera
@app.route('/dev/<int:id>', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

#lista todos os devs e permite registrar um novo dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__=='__main__':
    app.run(debug=True)