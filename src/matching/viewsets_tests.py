from rest_framework.test import APIClient
from program.factories import AgencyWithProgramsFactory
from .factories import MatchingConfigFactory, ClientMatchingFactory


def test_matching_config(client):
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    MatchingConfigFactory(agency=agency)

    user = agency.user_profiles.first().user

    url = '/matching/config/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data['results']) == 1


def test_client_matching(client):
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)
    ClientMatchingFactory(config=config, program=agency.programs.first())

    user = agency.user_profiles.first().user

    url = '/matching/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data['results']) == 1
    assert 'client' in response.data['results'][0]
    assert 'id' in response.data['results'][0]['client']
