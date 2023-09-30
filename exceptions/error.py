from flask import jsonify


class CustomException(Exception):

    def __init__(self, code, message=None):
        if (message):
            self.message = message
        else:
            self.message = str(self.args)

        self.code = code

    def get_response(self):
        return jsonify({"message": self.message}), self.code

    def get_message(self):
        if isinstance(self.message, dict):
            return f'ERROR: {", ".join(self.message)}'
        return self.message


class DefaultException(CustomException):
    def __init__(self):
        self.code = 500
        self.message = {'error': 'Ocurrió un error inesperado en el servidor.'}


class InvalidUserException(CustomException):
    def __init__(self):
        self.code = 403
        self.message = {'error': 'Usuario o contraseña invalida.'}


class NotFoundException(CustomException):

    def __init__(self):
        self.code = 404
        self.message = {"error": "Objeto no encontrado"}


class MethodError(CustomException):
    def __init__(self):
        self.code = 405
        self.message = {"error": "Error de metodo no sportado"}
