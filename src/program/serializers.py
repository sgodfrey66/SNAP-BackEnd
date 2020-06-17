from core.serializers import ObjectSerializer
from agency.serializers import AgencyReader
from client.serializers import ClientReader
from .models import Program, AgencyProgramConfig, Enrollment, Eligibility


class ProgramReader(ObjectSerializer):
    class Meta:
        model = Program
        fields = ('id', 'object', 'name', 'description', 'created_at', 'modified_at')


class ProgramWriter(ProgramReader):
    pass


class AgencyProgramConfigReader(ObjectSerializer):
    agency = AgencyReader()
    program = ProgramReader()

    class Meta:
        model = AgencyProgramConfig
        fields = ('id', 'object', 'agency', 'program')


class AgencyProgramConfigWriter(AgencyProgramConfigReader):
    pass


class EligibilityReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = Eligibility
        fields = ('id', 'object', 'status', 'client', 'program')


class EligibilityWriter(AgencyProgramConfigReader):
    pass


class EnrollmentReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = Enrollment
        fields = ('id', 'object', 'status', 'client', 'program')


class EnrollmentWriter(AgencyProgramConfigReader):
    pass
