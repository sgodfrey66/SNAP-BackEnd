from core.serializers import ObjectSerializer, CreatedByReader
from client.serializers import ClientReader
from program.serializers import ProgramReader
from .models import MatchingConfig, ClientMatching, ClientMatchingNote, ClientMatchingHistory


class MatchingConfigReader(ObjectSerializer):
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = MatchingConfig
        fields = ('id', 'object', 'name', 'config', 'created_at', 'modified_at', 'created_by')


class MatchingConfigWriter(MatchingConfigReader):
    pass


class ClientMatchingReader(ObjectSerializer):
    class HistoryReader(ObjectSerializer):
        created_by = CreatedByReader(read_only=True)

        class Meta:
            model = ClientMatchingHistory
            fields = ('id', 'object', 'step', 'outcome', 'created_by', 'created_at')

    class NotesReader(ObjectSerializer):
        created_by = CreatedByReader(read_only=True)

        class Meta:
            model = ClientMatchingNote
            fields = ('id', 'object', 'step', 'note', 'created_by', 'created_at')

    config = MatchingConfigReader()
    client = ClientReader()
    program = ProgramReader()
    notes = NotesReader(many=True, read_only=True)
    history = HistoryReader(many=True, read_only=True)
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = ClientMatching
        fields = ('id', 'object', 'config', 'client', 'program', 'step', 'outcome', 'start_date',
                  'end_date', 'history', 'notes', 'created_at', 'modified_at', 'created_by')


class ClientMatchingWriter(ObjectSerializer):
    class Meta:
        model = ClientMatching
        fields = ('config', 'client', 'program', 'start_date', )
