import pytest
from typing import Any

from hawkBackend.domain.validations import NotBlankValidation , TypeValidator , NotNullValidation ,ValidationProtocol

class BaseValidationsTests:
    validator : ValidationProtocol
    validator_field : str
    incorrect_value : str
    correct_value : Any
    
    def get_validator_and_message(self):
        validator = self.validator(self.validator_field)
        message = validator.erro_message
        return validator , message
    
    def test_if_correct_value_pass_in_validation(self):
        validator , message = self.get_validator_and_message()
        result = validator.validate(self.correct_value)
        
        assert result is None
        
    def test_if_incorrect_value_receive_an_error_message(self):
        validator ,message = self.get_validator_and_message()
        result = validator.validate(self.incorrect_value)
        
        assert result is not None

class TestNotBlankValidation(BaseValidationsTests):
    
    validator = NotBlankValidation
    validator_field = "not_blank_field"
    correct_value = "Not Blank Value"
    incorrect_value = ""
        
    def test_if_validator_return_an_erro_message_with_space_string(self):
        validator ,message = self.get_validator_and_message()
        
        result = validator.validate(" ")
        
        assert result is not None        
        
class TestNotNullValidator(BaseValidationsTests):
    validator = NotNullValidation
    validator_field = "not_null_field"
    correct_value = "Not Null value"
    incorrect_value = None
    
class TestTypeValidator(BaseValidationsTests):
    validator = TypeValidator
    validator_field = "not_incorrect_type_field"
    correct_value = "type str"
    incorrect_value = 12
    correct_type = str

    def test_if_correct_value_pass_in_validation(self):
        validator , message = self.get_validator_and_message()
        result = validator.validate(self.correct_value,self.correct_type)
        
        assert result is None
            
    def test_if_incorrect_value_receive_an_error_message(self):
        validator ,message = self.get_validator_and_message()
        result = validator.validate(self.incorrect_value,self.correct_type)
        
        assert result is not None