import pytest
from typing import Any
from datetime import datetime , timedelta , timezone

from hawkBackend.domain.validations import NotBlankValidation , TypeValidator , NotNullValidation ,ValidationProtocol , CorrectTypeOrNoneValidator , NotFutureDateValidator

class BaseValidationsTests:
    validator : ValidationProtocol
    validator_field : str
    incorrect_value : str
    correct_values : list[Any]
    
    def get_validator_and_message(self):
        validator = self.validator(self.validator_field)
        message = validator.erro_message
        return validator , message
    
    def test_if_correct_value_pass_in_validation(self):
        validator , message = self.get_validator_and_message()
        for value in self.correct_values:  
            result = validator.validate(value)
        
            assert result is None
        
    def test_if_incorrect_value_receive_an_error_message(self):
        validator ,message = self.get_validator_and_message()
        result = validator.validate(self.incorrect_value)
        
        assert result is not None

class TestNotBlankValidation(BaseValidationsTests):
    
    validator = NotBlankValidation
    validator_field = "not_blank_field"
    correct_values = ["Not Blank Value"]
    incorrect_value = ""
        
    def test_if_validator_return_an_erro_message_with_space_string(self):
        validator ,message = self.get_validator_and_message()
        
        result = validator.validate(" ")
        
        assert result is not None        
        
class TestNotNullValidator(BaseValidationsTests):
    validator = NotNullValidation
    validator_field = "not_null_field"
    correct_values = ["Not Null value"]
    incorrect_value = None
    
class TestTypeValidator(BaseValidationsTests):
    validator = TypeValidator
    validator_field = "not_incorrect_type_field"
    correct_values = ["type str"]
    incorrect_value = 12
    correct_type = str

    def test_if_correct_value_pass_in_validation(self):
        validator , message = self.get_validator_and_message()
        for value in self.correct_values:
            result = validator.validate(value,self.correct_type)
        
            assert result is None
            
    def test_if_incorrect_value_receive_an_error_message(self):
        validator ,message = self.get_validator_and_message()
        result = validator.validate(self.incorrect_value,self.correct_type)
        
        assert result is not None
        
class TestCorrectTypeOrNoneValidator(
    TestTypeValidator
):
    
    validator = CorrectTypeOrNoneValidator
    validator_field = "not_incorrect_type_field"
    correct_values = ["type str",None]
    incorrect_value = 12
    correct_type = str
    
class TestNotFutureDateValidator(
    BaseValidationsTests
):
    validator_field = "correct_data_field"
    validator  = NotFutureDateValidator
    
    incorrect_value = datetime.now(timezone.utc) + timedelta(days=1)
    correct_values = [
        datetime.now(timezone.utc),
        datetime.now(timezone.utc) - timedelta(1),
    ]