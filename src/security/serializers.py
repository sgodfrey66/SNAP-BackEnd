from .models import SecurityGroupUserAgency
from core.serializers import ObjectSerializer, CreatedByReader


class SecurityGroupUserAgencyReader(ObjectSerializer):
    class Meta:
        model = SecurityGroupUserAgency
        fields = '__all__'

class SecurityGroupUserAgencyWriter(SecurityGroupUserAgencyReader):
    pass
