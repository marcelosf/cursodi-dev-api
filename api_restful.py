from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'Registro Excluído'})


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        data = json.loads(request.data)
        posicao = len(desenvolvedores)
        data['id'] = posicao
        desenvolvedores.append(data)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')


if __name__ == "__main__":
    app.run(debug=True)
