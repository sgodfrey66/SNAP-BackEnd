from rest_framework.test import APIClient
from __tests__.factories import setup_2_agencies

# e2e tests


def test_get_clients_by_anonymous():
    agency1, agency2, user1, user2, client1, client2 = setup_2_agencies()

    url = '/clients/'
    api_client = APIClient()

    # self.client.credentials(
    #     HTTP_X_HMIS_TRUSTEDAPP_ID='appid',
    #     HTTP_AUTHORIZATION='HMISUserAuth session_token=abcd',
    # )
    # client.login(username='user1', password='pass')

    response = api_client.get(url)
    assert response.status_code == 401


def test_get_clients_by_agency_user(client):
    agency1, agency2, user1, user2, client1, client2 = setup_2_agencies()
    url = '/clients/'
    api_client = APIClient()
    api_client.force_authenticate(user1)

    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['object'] == 'Client'
    assert response.data[0]['first_name'] == 'John'
