import pytest
from uuid import uuid4
from faker import Faker
from random import SystemRandom

from hawkBackend.domain.base_entity import BaseEntity

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return SystemRandom().randint(0, 999999)   

@pytest.fixture
def base_entity_mock(faker : Faker , request):
    overrides = request.param if hasattr(request, "param") else {}

    return BaseEntity.create(
        is_active=overrides.get("is_active", faker.boolean()),
        created_by=overrides.get("created_by", uuid4()),
        updated_by=overrides.get("updated_by", uuid4()),
    )