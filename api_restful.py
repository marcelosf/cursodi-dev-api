from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import ListaHabilidades, Habilidades, Validacao
from habilidades import HabilidadeNotFoundException


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
            self._valida_dados(response)
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
            validacao = Validacao()
            validacao._valida_habilidades(dados['habilidades'])
            desenvolvedores[id] = dados
            response = dados
        except HabilidadeNotFoundException as e:
            mensagem = str(e)
            response = {'status': 'erro', 'mensagem': mensagem}
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
        try:
            dados = json.loads(request.data)
            validacao = Validacao()
            validacao._valida_habilidades(dados['habilidades'])
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            response = desenvolvedores[posicao]
        except HabilidadeNotFoundException as e:
            mensagem = str(e)
            response = {'status': 'error', 'mensagem': mensagem}
        return response


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')


if __name__ == "__main__":
    app.run(debug=True)
