import factory
from .models import MatchingConfig, ClientMatching
from client.factories import ClientFactory


class MatchingConfigFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MatchingConfig

    config = {'foo': 'bar'}


class ClientMatchingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClientMatching

    client = factory.SubFactory(ClientFactory)
