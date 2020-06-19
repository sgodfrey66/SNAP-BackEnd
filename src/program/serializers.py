from core.serializers import ObjectSerializer
from agency.serializers import AgencyReader
from client.serializers import ClientReader
from survey.serializers import SurveyMiniReader
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
    enrollment_entry_survey = SurveyMiniReader()
    enrollment_update_survey = SurveyMiniReader()
    enrollment_exit_survey = SurveyMiniReader()

    class Meta:
        model = AgencyProgramConfig
        fields = ('id', 'object', 'agency', 'program', 'enrollment_entry_survey',
                  'enrollment_update_survey', 'enrollment_exit_survey')


class AgencyProgramConfigWriter(AgencyProgramConfigReader):
    pass


class EligibilityReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = Eligibility
        fields = ('id', 'object', 'status', 'client', 'program')


class EligibilityWriter(EligibilityReader):
    pass


class EnrollmentReader(ObjectSerializer):
    client = ClientReader()
    program = ProgramReader()

    class Meta:
        model = Enrollment
        fields = ('id', 'object', 'status', 'client', 'program')


class EnrollmentWriter(EnrollmentReader):
    pass
