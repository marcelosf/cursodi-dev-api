from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import ListaHabilidades, Habilidades


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
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            response = dados
        except IndexError:
            mensagem = 'Não existe um desenvolvedor com id {}'.format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return response

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            response = ({'status': 'sucesso', 'mensagem': 'Registro Excluído'})
        except IndexError:
            mensagem = 'Não existe um desenvolvedor com id {}'.format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return response


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
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')


if __name__ == "__main__":
    app.run(debug=True)
