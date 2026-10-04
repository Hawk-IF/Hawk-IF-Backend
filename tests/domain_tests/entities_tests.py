import pytest
from uuid import uuid4
from datetime import datetime , timezone

from hawkBackend.domain.base_entity import BaseEntity

from hawkBackend.domain.exceptions.validate_exceptions import ValidateException

class TestBaseEntity:
    
    @pytest.mark.parametrize(
        "created_by , updated_by , is_active",
        [
            (None , None  , True),
            (uuid4() , uuid4() , False),
        ]
    )
    def test_create_method_with_correct_data(self, created_by , updated_by , is_active):
        instance = BaseEntity.create(
            created_by=created_by,
            updated_by=updated_by,
            is_active=is_active
        )
        
        assert instance.created_at.replace(microsecond=0) == datetime.now(timezone.utc).replace(microsecond=0)
        
    
    @pytest.mark.parametrize(
            "created_by , updated_by , is_active",
            [
                ("teste" , True  , "false"),
                (False , 12 , "a"),
            ]
        )
    def test_create_method_with_incorrect_data(self, created_by , updated_by , is_active):
        with pytest.raises(ValidateException) as exception:
            instance = BaseEntity.create(
                created_by=created_by,
                updated_by=updated_by,
                is_active=is_active
            )
            assert instance.created_at == None
        
        assert len(exception.value.errors) == 3
        assert exception.value.errors.get("created_by",False)
        assert exception.value.errors.get("updated_by",False)
        assert exception.value.errors.get("is_active",False)
        
        
    
    def test_reconstruct_method(self):
        pass
    
    
    def test_updated_method_with_correct_data(self , base_entity_mock :  BaseEntity):
        update_by = uuid4()
        is_active = True
        base_entity_mock.update(
            is_active=is_active,
            updated_by=update_by
        )
        
        assert base_entity_mock.updated_by == update_by
        assert base_entity_mock.is_active == is_active
        assert base_entity_mock.updated_at.replace(microsecond=0) == datetime.now(timezone.utc).replace(microsecond=0)
        
    def test_updated_method_with_incorrect_data(self , base_entity_mock :  BaseEntity):
        update_by = "user 1"
        is_active = 12
        
        with pytest.raises(ValidateException) as exception:
            base_entity_mock.update(
                is_active=is_active,
                updated_by=update_by
            )
        
        assert base_entity_mock.updated_by != update_by
        assert base_entity_mock.is_active != is_active
        
        assert len(exception.value.errors) == 2
        assert exception.value.errors.get("is_active",False)
        assert exception.value.errors.get("updated_by",False)