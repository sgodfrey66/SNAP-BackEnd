from core.serializers import ObjectSerializer, CreatedByReader
from client.serializers import ClientReader
from .models import MatchingConfig, ClientMatching


class MatchingConfigReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = MatchingConfig
        fields = ('id', 'object', 'config', 'created_at', 'modified_at', 'created_by')


class MatchingConfigWriter(MatchingConfigReader):
    pass


class ClientMatchingReader(ObjectSerializer):
    client = ClientReader()

    class Meta:
        model = ClientMatching
        fields = ('id', 'object', 'client', 'created_at', 'modified_at', 'created_by')


class ClientMatchingWriter(ClientMatchingReader):
    pass
