from rest_framework import serializers
from core.serializers import ObjectSerializer, CreatedByReader
from .models import Client


class ClientReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'object', 'first_name', 'middle_name', 'last_name', 'dob', 'created_by')


class ClientWriter(ClientReader):
    pass
