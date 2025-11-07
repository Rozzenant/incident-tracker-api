import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from incidents.models import Incident


@pytest.mark.django_db
def test_patch_incident_status_success():
    client = APIClient()
    incident = Incident.objects.create(
        description="Test incident", status="open", source="operator"
    )
    url = reverse('incident-update-status', kwargs={'id': incident.id})
    payload = {"status": "resolved"}

    response = client.patch(url, data=payload, format='json')

    assert response.status_code == 200
    incident.refresh_from_db()
    assert incident.status == "resolved"


@pytest.mark.django_db
def test_patch_incident_not_found():
    client = APIClient()
    url = reverse('incident-update-status', kwargs={'id': 99999})
    payload = {"status": "resolved"}

    response = client.patch(url, data=payload, format='json')

    assert response.status_code == 404


@pytest.mark.django_db
def test_patch_invalid_status_value():
    client = APIClient()
    incident = Incident.objects.create(
        description="Invalid status test", status="open", source="operator"
    )
    url = reverse('incident-update-status', kwargs={'id': incident.id})
    payload = {"status": "invalid_status"}

    response = client.patch(url, data=payload, format='json')

    assert response.status_code == 400
    assert 'status' in response.data


@pytest.mark.django_db
def test_patch_missing_status_field():
    client = APIClient()
    incident = Incident.objects.create(
        description="Missing status test", status="open", source="operator"
    )
    url = reverse('incident-update-status', kwargs={'id': incident.id})
    payload = {}

    response = client.patch(url, data=payload, format='json')

    assert response.status_code == 400
    assert 'status' in response.data


@pytest.mark.django_db
def test_patch_method_put_disallowed():
    client = APIClient()
    incident = Incident.objects.create(
        description="PUT not allowed test", status="open", source="operator"
    )
    url = reverse('incident-update-status', kwargs={'id': incident.id})
    payload = {"status": "resolved"}

    response = client.put(url, data=payload, format='json')

    assert response.status_code == 405
