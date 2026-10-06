from hawkBackend.domain.exceptions.base_exception import BaseSystemException


class NotPermissionException(BaseSystemException):
    def __init__(self,message : str = "You don't have permission to do this" , necessary_permissions : list[str] = [] ,*args):
        super().__init__(message,*args)
        self.necessary_permissions = necessary_permissions

class UnAuthorizeException(Exception):
    def __init__(self, message : str = "You must be logged to do this",*args):
        super().__init__(message , *args)
