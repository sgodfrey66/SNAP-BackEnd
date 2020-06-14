from core.serializers import ObjectSerializer
from .models import Program


class ProgramReader(ObjectSerializer):
    class Meta:
        model = Program
        fields = ('id', 'object', 'name', 'description', 'created_at', 'modified_at')


class ProgramWriter(ProgramReader):
    pass
