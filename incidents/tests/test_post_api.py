import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from incidents.models import Incident


@pytest.mark.django_db
def test_create_incident_success():
    client = APIClient()
    url = reverse('incident-list')

    payload = {
        "description": "Проблема с самокатом на входе в ТЦ",
        "status": "open",
        "source": "operator"
    }

    response = client.post(url, data=payload, format='json')

    assert response.status_code == 201
    data = response.data
    assert data['id'] is not None
    assert data['description'] == "Проблема с самокатом на входе в ТЦ"
    assert data['status'] == "open"
    assert data['source'] == "operator"
    assert Incident.objects.filter(id=data['id']).exists()


@pytest.mark.django_db
def test_create_incident_invalid_status():
    client = APIClient()
    url = reverse('incident-list')

    payload = {
        "description": "Неверный статус",
        "status": "bad_status",
        "source": "operator"
    }

    response = client.post(url, data=payload, format='json')

    assert response.status_code == 400
    assert 'status' in response.data


@pytest.mark.django_db
def test_create_incident_missing_description():
    client = APIClient()
    url = reverse('incident-list')

    payload = {
        "status": "open",
        "source": "operator"
    }

    response = client.post(url, data=payload, format='json')

    assert response.status_code == 400
    assert 'description' in response.data
