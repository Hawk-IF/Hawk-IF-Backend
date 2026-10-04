import pytest
from uuid import uuid4

from hawkBackend.domain.guards import BaseGuard

class TestBaseGuard:
    
    @pytest.mark.parametrize(
        "created_by , updated_by",
        (None , uuid4()),
        (None , uuid4()),
    )
    def tests_guard_validates_not_return_error_with_correct_data(self , created_by , updated_by):
        is_active = True
        
        errors = BaseGuard()\
            .validate_created_by(created_by)\
            .validate_updated_by(updated_by)\
            .validate_is_active(is_active)\
            .errors
        
        assert len(errors) == 0
        
    @pytest.mark.parametrize(
            "created_by , updated_by , is_active",
            (12 , "teste"),
            (345 , "play"),
            ("false",90)
    )
    def tests_guard_validates_return_error_message(self , created_by , updated_by , is_active):
        errors = BaseGuard()\
            .validate_created_by(created_by)\
            .validate_updated_by(updated_by)\
            .validate_is_active(is_active)\
            .errors
        
        assert len(errors) == 3
        assert isinstance(errors.get("create_by"),list) 
        assert isinstance(errors.get("updated_by"),list)
        assert isinstance(errors.get("is_active"),list)
        
    