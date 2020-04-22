from rest_framework import serializers
from .models import Client


class ClientReader(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'dob')


class ClientWriter(ClientReader):
    pass
