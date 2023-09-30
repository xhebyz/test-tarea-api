from flask import jsonify
class CustomException(Exception):

    def __init__(self, code, message=None):
        if (message):
            self.message = message
        else:
            self.message = self.args.__dict__

        self.code = code

    def get_response(self):
        return jsonify(self.message), self.code


class DefaultException(CustomException):
    def __init__(self):
        self.code = 500
        self.message = {'error': 'Ocurrió un error inesperado en el servidor.'}


class NotFoundException(CustomException):

    def __init__(self):
        self.code = 404
        self.message = {"error": "Objeto no encontrado"}


class MethodError(CustomException):
    def __init__(self):
        self.code = 405
        self.message = {"error": "Error de metodo no sportado"}
