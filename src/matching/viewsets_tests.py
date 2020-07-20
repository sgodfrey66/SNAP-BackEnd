import datetime
from rest_framework.test import APIClient
from program.factories import AgencyWithProgramsFactory
from client.models import Client
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


def test_list_client_matching(client):
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


def test_create_client_matching():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)

    print(agency.programs.all())

    user = agency.user_profiles.first().user

    url = '/matching/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'config': config.id,
        'program': agency.programs.first().id,
        'client': Client.objects.first().id,
    }, format='json')
    assert response.status_code == 201


def test_patch_client_matching():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)
    matching = ClientMatchingFactory(config=config, program=agency.programs.first(),
                                     client=Client.objects.first(), start_date='2020-01-01')

    user = agency.user_profiles.first().user

    url = f'/matching/{matching.id}/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.patch(url, {
        'end_date': '2020-02-02',
    }, format='json')
    assert response.status_code == 200
    matching.refresh_from_db()
    assert matching.end_date == datetime.date(2020, 2, 2)


def test_create_client_matching_for_invalid_client():
    AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)
    user = agency.user_profiles.first().user

    api_client = APIClient()
    api_client.force_authenticate(user)

    client = Client.objects.exclude(created_by=user).first()

    response = api_client.post('/matching/', {
        'config': config.id,
        'program': agency.programs.first().id,
        'client': client.id,
    }, format='json')
    assert response.status_code == 400


def test_create_client_matching_for_invalid_program():
    agency1 = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    agency2 = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency1)

    user = agency1.user_profiles.first().user

    url = '/matching/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'config': config.id,
        'program': agency2.programs.first().id,
        'client': Client.objects.first().id,
    }, format='json')
    assert response.status_code == 400


def test_create_note_for_existing_matching():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)

    matching = ClientMatchingFactory(
        config=config,
        program=agency.programs.first(),
        client=Client.objects.first(),
    )

    user = agency.user_profiles.first().user

    url = f'/matching/{matching.id}/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.patch(url, {
        'notes': [
            {
                'note': 'abcd'
            },
        ]
    }, format='json')

    assert response.status_code == 200

    matching.refresh_from_db()
    assert matching.notes.count() == 1
    assert matching.notes.first().note == 'abcd'


def test_create_history_for_existing_matching():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)

    matching = ClientMatchingFactory(
        config=config,
        program=agency.programs.first(),
        client=Client.objects.first(),
    )

    user = agency.user_profiles.first().user

    url = f'/matching/{matching.id}/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.patch(url, {
        'history': [
            {
                'step': '1',
                'outcome': 'success',
            },
        ]
    }, format='json')

    assert response.status_code == 200

    matching.refresh_from_db()
    assert matching.history.count() == 1
    assert matching.history.first().step == '1'
    assert matching.history.first().outcome == 'success'


def test_client_matchin_history_viewset_list():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)

    matching = ClientMatchingFactory(
        config=config,
        program=agency.programs.first(),
        client=Client.objects.first(),
    )

    user = agency.user_profiles.first().user

    url = f'/matching/{matching.id}/history/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    print(response.data)

    assert response.status_code == 200


def test_client_matchin_history_viewset_create():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    config = MatchingConfigFactory(agency=agency)

    matching = ClientMatchingFactory(
        config=config,
        program=agency.programs.first(),
        client=Client.objects.first(),
    )

    user = agency.user_profiles.first().user

    url = f'/matching/{matching.id}/history/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'step': 1,
        'outcome': 'ok',
    }, format='json')

    print(response.data)

    assert response.status_code == 201
