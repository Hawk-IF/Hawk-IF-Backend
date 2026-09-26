import pytest
from random import SystemRandom

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return SystemRandom().randint(0, 999999)   