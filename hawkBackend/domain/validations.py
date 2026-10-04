from abc import ABC, abstractmethod
from datetime import datetime, timezone
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
    def __init__(self, field , type : Any = None):
        self.field = field
        self.type = type
        self.erro_message = self.create_erro_message()

    def create_erro_message(self, *args, **kwargs):
        return f"{self.field} must be of type: {self.type}"

    def validate[T](self , value : T , value_type : Any | None = None):
        validate_type = value_type or self.type
        if not isinstance(value , validate_type):
            return self.erro_message

class CorrectTypeOrNoneValidator(
    TypeValidator
):
    def validate(self, value, value_type = None):
        if value is None:
            return None
        return super().validate(value, value_type)

    def create_erro_message(self):
        return super().create_erro_message().join(" or none")

class NotFutureDateValidator(
    ValidationProtocol
):
    erro_message = "can't be a future date"

    def validate(self, value : datetime):
        now = datetime.now(timezone.utc)
        if value > now:
            return self.erro_message
