from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
    },
    {   
        'id': 1,
        'nome': 'Galeao',
        'habilidades': ['Python', 'Django']
    }
]

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados) 
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Excluído'})


@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'GET':
        return jsonify(desenvolvedores)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Dados inseridos com sucesso'})

if __name__ == "__main__":
    app.run(debug=True)