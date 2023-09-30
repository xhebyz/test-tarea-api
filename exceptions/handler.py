from exceptions.error import CustomException, DefaultException


class ExceptionHandler:
    @staticmethod
    def handle_exception(error):
        if isinstance(error, CustomException):
            return error.get_response()
        return DefaultException().get_response()
