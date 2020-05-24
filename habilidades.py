from flask_restful import Resource
from flask import request
import json


habilidades = ['PHP', 'PYTHON', 'JAVA', 'RUBY', 'DART', 'JAVASCRIPT']


class ListaHabilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        data = json.loads(request.data)
        habilidades.append(data)
        return data


class Habilidades(Resource):
    def put(self, id):
        try:
            data = json.loads(request.data)
            habilidades[id] = data
            mensagem = 'Habilidade atualizada com sucesso'
            response = {'status': 'sucesso', 'mensagem': mensagem}
        except IndexError:
            mensagem = 'Não existe uma habilidade com indice {}'.format(id)
            response = {'status': 'sucesso', 'mensagem': mensagem}
        return response

    def get(self, id):
        try:
            data = habilidades[id]
            response = data
        except IndexError:
            mensagem = 'Não existe uma habilidade com indice {}'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def delete(self, id):
        try:
            habilidades.pop(id)
            mensagem = 'Habilidade {} removida'.format(id)
            response = {'status': 'sucesso', 'mensagem': mensagem}
        except IndexError:
            mensagem = 'Não existe uma habilidade com indice {}'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        return response


class Validacao:
    def _valida_habilidades(self, items):
        for habilidade in items:
            if habilidade not in habilidades:
                mensagem = 'A habilidade {} não está cadastrada'.format(habilidade)
                raise HabilidadeNotFoundException(mensagem, 'habilidade não cadastrada')


class HabilidadeNotFoundException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
