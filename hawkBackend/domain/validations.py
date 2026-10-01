from abc import ABC, abstractmethod
from typing import Any


class ValidationProtocol(
    ABC
):
    field : str
    erro_message : str

    def __init__(self , field : str):
        self.field = field
        self.create_erro_message()

    def create_erro_message(self ,*args , **kwargs)-> None:
        self.erro_message = f"{self.field} {self.erro_message}"

    @abstractmethod
    def validate(self , *args , **kwargs)->None | str:
        pass

class NotBlankValidation(
    ValidationProtocol
):
    erro_message = "can't be blank"

    def validate(self , value : str):
        if not len(value.replace(" ","")):
            return self.erro_message

class NotNullValidation(
    ValidationProtocol
):
    erro_message = "can't be null"

    def validate[T](self , value : T):
        if value is None:
            return self.erro_message

class TypeValidator(
    ValidationProtocol
):
    def __init__(self, field):
        self.field = field
        self.erro_message = f"{field} has incorrect type"

    def validate[T](self , value : T , value_type : Any = None):
        type = value_type
        self.erro_message = self.create_erro_message(type)
        if not isinstance(value , type):
            return self.erro_message

    def create_erro_message(self , type : Any):
        return f"{self.field} must be of type {type}"
