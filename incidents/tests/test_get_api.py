import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_incident_list_returns_all(incident_list):
    client = APIClient()
    url = reverse('incident-list')
    response = client.get(url)

    assert response.status_code == 200
    assert 'results' in response.data
    assert len(response.data['results']) <= 20  # при default_limit = 20
    assert response.data['count'] == len(incident_list)


@pytest.mark.django_db
def test_incident_list_with_limit_offset(incident_list):
    client = APIClient()
    url = reverse('incident-list')
    response = client.get(url + '?limit=10&offset=5')

    assert response.status_code == 200
    assert len(response.data['results']) == 10
    assert response.data['count'] == len(incident_list)


@pytest.mark.django_db
def test_incident_filter_by_status():
    from .factories import IncidentFactory

    IncidentFactory.create_batch(5, status='open')
    IncidentFactory.create_batch(3, status='resolved')
    client = APIClient()
    url = reverse('incident-list')

    response = client.get(url + '?status=open')
    assert response.status_code == 200
    assert all(incident['status'] == 'open' for incident in response.data['results'])
