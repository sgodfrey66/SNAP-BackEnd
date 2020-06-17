from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMemberReadOnly
from .models import Program, AgencyProgramConfig, Eligibility, Enrollment
from .serializers import (
    ProgramReader, ProgramWriter,
    AgencyProgramConfigReader, AgencyProgramConfigWriter,
    EligibilityReader, EligibilityWriter,
    EnrollmentReader, EnrollmentWriter,
)

# from .filters import AgencyFilter


class ProgramViewset(ModelViewSet):
    queryset = Program.objects.all()
    read_serializer_class = ProgramReader
    write_serializer_class = ProgramWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]

    def get_queryset(self):
        return Program.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AgencyProgramConfigViewset(ModelViewSet):
    queryset = AgencyProgramConfig.objects.all()
    read_serializer_class = AgencyProgramConfigReader
    write_serializer_class = AgencyProgramConfigWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]

    def get_queryset(self):
        return AgencyProgramConfig.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EligibilityViewset(ModelViewSet):
    queryset = Eligibility.objects.all()
    read_serializer_class = EligibilityReader
    write_serializer_class = EligibilityWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]

    def get_queryset(self):
        return Eligibility.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EnrollmentViewset(ModelViewSet):
    queryset = Enrollment.objects.all()
    read_serializer_class = EnrollmentReader
    write_serializer_class = EnrollmentWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]

    def get_queryset(self):
        return Enrollment.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)