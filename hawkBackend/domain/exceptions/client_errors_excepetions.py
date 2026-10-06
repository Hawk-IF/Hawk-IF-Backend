from hawkBackend.domain.exceptions.base_exception import BaseSystemException


class NotFoundException(BaseSystemException):
    def __init__(self, message : str = "Resource not found", *args):
        super().__init__(message, *args)
