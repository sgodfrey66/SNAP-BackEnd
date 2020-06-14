from rest_framework.test import APIClient
from .factories import AgencyWithPrograms
from .models import Program


def test_retrieve_programs():
    # create test agency
    agency1 = AgencyWithPrograms(users=1, num_programs=3)
    # create another agency
    AgencyWithPrograms(users=1, num_programs=2)

    user = agency1.user_profiles.first().user
    url = '/programs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert Program.objects.count() == 5
    assert response.status_code == 200
    assert len(response.data['results']) == 3


def test_agency_user_cannot_create_program():
    agency = AgencyWithPrograms(users=1, num_programs=1)

    user = agency.user_profiles.first().user
    url = '/programs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'name': 'new program'
    })

    assert response.status_code == 403
    assert Program.objects.count() == 1
