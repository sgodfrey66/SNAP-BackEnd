from core.serializers import ObjectSerializer, CreatedByReader
from agency.serializers import AgencyReader
from client.serializers import ClientReader
from .models import Eligibility, AgencyEligibilityConfig, ClientEligibility


class EligibilityReader(ObjectSerializer):
    class Meta:
        model = Eligibility
        fields = ('id', 'object', 'name', 'created_at', 'modified_at')


class EligibilityWriter(EligibilityReader):
    pass


class AgencyEligibilityConfigReader(ObjectSerializer):
    eligibility = EligibilityReader()
    agency = AgencyReader()

    class Meta:
        model = AgencyEligibilityConfig
        fields = ('id', 'object', 'agency', 'eligibility', 'created_at', 'modified_at')


class AgencyEligibilityConfigWriter(ObjectSerializer):
    class Meta:
        model = AgencyEligibilityConfig
        fields = ('object', 'agency', 'eligibility')


class ClientEligibilityReader(ObjectSerializer):
    eligibility = EligibilityReader()
    client = ClientReader()
    created_by = CreatedByReader(read_only=True)

    class Meta:
        model = ClientEligibility
        fields = ('id', 'object', 'client', 'eligibility', 'status', 'created_at', 'modified_at', 'created_by')


class ClientEligibilityWriter(ObjectSerializer):
    class Meta:
        model = ClientEligibility
        fields = ('client', 'eligibility', 'status')
