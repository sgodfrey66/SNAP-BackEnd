from django.contrib.auth.models import User
from __tests__.factories import setup_2_agencies
from .models import Client


def test_ClientManager_for_user_returns_clients_from_user_agency():
    agency1, agency2, user1, user2, client1, client2 = setup_2_agencies()

    assert list(Client.objects.for_user(user1)) == [client1]
    assert list(Client.objects.for_user(user2)) == [client2]
