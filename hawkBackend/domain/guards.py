from datetime import datetime
from uuid import UUID

from hawkBackend.domain.field_validator import FieldValidator
from hawkBackend.domain.validations import (
    CorrectTypeOrNoneValidator,
    NotFutureDateValidator,
    TypeValidator,
)


class BaseGuard:
    errors : dict["str",list["str"]]

    def __init__(self):
        self.errors = {}

    def add_error(self,field : str,errors : list[str]):
        existing_errors = self.errors.get(field , [])
        self.errors[field] = existing_errors + errors

    def realize_validate(self, validate_result : list[str] , field_name : str)->None:
        if len(validate_result):
            self.add_error(field_name , validate_result)

    def validate_created_by(self , value) -> "BaseGuard":
        field_name = "created_by"
        validator = FieldValidator(
            rules=[
                CorrectTypeOrNoneValidator(field_name,UUID)
            ]
        )
        self.realize_validate(validator.validate(value),field_name)
        return self

    def validate_updated_by(self , value) -> "BaseGuard":
        field_name = "updated_by"
        validator = FieldValidator(
            rules=[
                CorrectTypeOrNoneValidator(field_name,UUID)
            ]
        )
        self.realize_validate(validator.validate(value),field_name)
        return self

    def validate_is_active(self , value) -> "BaseGuard":
        field_name = "is_active"
        validator = FieldValidator(
            rules=[
                TypeValidator(field_name,bool)
            ]
        )
        self.realize_validate(validator.validate(value),field_name)
        return self

    def validate_updated_at(self , value) -> "BaseGuard":
        field_name = "updated_at"
        validator = FieldValidator(
            rules=[
                TypeValidator(field_name,datetime),
                NotFutureDateValidator(field_name)
            ]
        )
        self.realize_validate(validator.validate(value),field_name)
        return self
