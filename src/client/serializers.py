from rest_framework import serializers
from core.serializers import ObjectSerializer
from .models import Client


class ClientReader(ObjectSerializer):
    class Meta:
        model = Client
        fields = ('id', 'object', 'first_name', 'middle_name', 'last_name', 'dob')


class ClientWriter(ClientReader):
    pass
