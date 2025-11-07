import pytest
from .factories import IncidentFactory


@pytest.fixture
def incident():
    return IncidentFactory()


@pytest.fixture
def incident_list():
    return IncidentFactory.create_batch(100)
