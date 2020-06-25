from rest_framework.test import APIClient
from survey.factories import SurveyFactory
from .factories import AgencyWithProgramsFactory
from client.models import Client
from .models import Program


def test_retrieve_programs():
    # create test agency
    agency1 = AgencyWithProgramsFactory(users=1, num_programs=3)
    # create another agency
    AgencyWithProgramsFactory(users=1, num_programs=2)

    user = agency1.user_profiles.first().user
    url = '/programs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert Program.objects.count() == 5
    assert response.status_code == 200
    assert len(response.data['results']) == 3


def test_agency_user_cannot_create_program():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)

    user = agency.user_profiles.first().user
    url = '/programs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'name': 'new program'
    })

    assert response.status_code == 403
    assert Program.objects.count() == 1


def test_list_agency_configs():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    AgencyWithProgramsFactory(users=1, num_programs=1)

    user = agency.user_profiles.first().user
    url = '/programs/agency_configs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200

    results = response.data['results']

    assert len(results) == 1
    assert results[0]['agency']['id'] == str(agency.id)
    assert results[0]['program']['id'] == str(agency.agencyprogramconfig_set.first().program.id)
    assert results[0]['enrollment_entry_survey'] is None
    assert results[0]['enrollment_update_survey'] is None
    assert results[0]['enrollment_exit_survey'] is None


def test_list_program_surveys():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency.user_profiles.first().user

    entry_survey = SurveyFactory(name='entry', created_by=user)
    update_survey = SurveyFactory(name='update', created_by=user)
    exit_survey = SurveyFactory(name='exit', created_by=user)

    program = agency.programs.first()
    program.enrollment_entry_survey = entry_survey
    program.enrollment_update_survey = update_survey
    program.enrollment_exit_survey = exit_survey
    program.save()

    url = '/programs/agency_configs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200

    result = response.data['results'][0]

    assert result['enrollment_entry_survey']['name'] == 'entry'
    assert result['enrollment_update_survey']['name'] == 'update'
    assert result['enrollment_exit_survey']['name'] == 'exit'


def test_list_agency_config_surveys():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency.user_profiles.first().user

    entry_survey = SurveyFactory(name='entry', created_by=user)
    update_survey = SurveyFactory(name='update', created_by=user)
    exit_survey = SurveyFactory(name='exit', created_by=user)

    config = agency.agencyprogramconfig_set.first()
    config.agency_enrollment_entry_survey = entry_survey
    config.agency_enrollment_update_survey = update_survey
    config.agency_enrollment_exit_survey = exit_survey
    config.save()

    url = '/programs/agency_configs/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200

    result = response.data['results'][0]

    assert result['enrollment_entry_survey']['name'] == 'entry'
    assert result['enrollment_update_survey']['name'] == 'update'
    assert result['enrollment_exit_survey']['name'] == 'exit'


def test_list_eligibility():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency.user_profiles.first().user

    url = '/programs/eligibility/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200


def test_create_eligibility():
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    user = agency.user_profiles.first().user

    url = '/programs/eligibility/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.post(url, {
        'program': agency.programs.first().id,
        'client': Client.objects.first().id,
        'status': 'ELIGIBLE',
    }, format='json')
    assert response.status_code == 201


def test_create_eligibility_for_invalid_client():
    AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    agency = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    user = agency.user_profiles.first().user

    url = '/programs/eligibility/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    client = Client.objects.exclude(created_by=user).first()

    response = api_client.post(url, {
        'program': agency.programs.first().id,
        'client': client.id,
        'status': 'ELIGIBLE',
    }, format='json')
    assert response.status_code == 400


def test_create_eligibility_for_invalid_program():
    agency1 = AgencyWithProgramsFactory(users=1, clients=1, num_programs=1)
    agency2 = AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency1.user_profiles.first().user

    url = '/programs/eligibility/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    client = Client.objects.exclude(created_by=agency2.user_profiles.first().user).first()

    response = api_client.post(url, {
        'program': agency2.programs.first().id,
        'client': client.id,
        'status': 'ELIGIBLE',
    }, format='json')
    assert response.status_code == 400


def test_list_enrollments():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency.user_profiles.first().user

    url = '/programs/enrollments/'
    api_client = APIClient()
    api_client.force_authenticate(user)

    response = api_client.get(url)

    assert response.status_code == 200
