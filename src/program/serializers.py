from core.serializers import ObjectSerializer
from agency.serializers import AgencyReader
from client.serializers import ClientReader
from survey.serializers import SurveyMiniReader
from .models import Program, AgencyProgramConfig, Enrollment, ProgramEligibility


class ProgramReader(ObjectSerializer):
    class Meta:
        model = Program
        fields = ('id', 'object', 'name', 'description', 'created_at', 'modified_at')


class ProgramWriter(ProgramReader):
    pass


class AgencyProgramConfigReader(ObjectSerializer):
    agency = AgencyReader()
    program = ProgramReader()
    enrollment_entry_survey = SurveyMiniReader()
    enrollment_update_survey = SurveyMiniReader()
    enrollment_exit_survey = SurveyMiniReader()

    class Meta:
        model = AgencyProgramConfig
        fields = ('id', 'object', 'agency', 'program', 'enrollment_entry_survey',
                  'enrollment_update_survey', 'enrollment_exit_survey')


class AgencyProgramConfigWriter(AgencyProgramConfigReader):
    pass


class ProgramEligibilityReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = ProgramEligibility
        fields = ('id', 'object', 'status', 'client', 'program', 'created_at', 'modified_at')


class ProgramEligibilityWriter(ObjectSerializer):
    class Meta:
        model = ProgramEligibility
        fields = ('status', 'client', 'program')


class EnrollmentReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = Enrollment
        fields = ('id', 'object', 'status', 'client', 'program', 'created_at', 'modified_at')


class EnrollmentWriter(ObjectSerializer):
    class Meta:
        model = Enrollment
        fields = ('status', 'client', 'program')
