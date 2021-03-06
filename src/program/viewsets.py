from core.viewsets import ModelViewSet
from core.permissions import IsAdmin, IsAgencyMember, IsAgencyMemberReadOnly
from core.validation import validate_fields_with_rules
from .filters import ProgramViewsetFilter, ProgramEligibilityViewsetFilter, EnrollmentViewsetFilter
from .models import Program, ProgramEligibility, Enrollment
from .serializers import (
    ProgramReader, ProgramWriter,
    ProgramEligibilityReader, ProgramEligibilityWriter,
    EnrollmentReader, EnrollmentWriter,
)


class ProgramViewset(ModelViewSet):
    queryset = Program.objects.all()
    read_serializer_class = ProgramReader
    write_serializer_class = ProgramWriter
    permission_classes = [IsAdmin | IsAgencyMemberReadOnly]
    filterset_class = ProgramViewsetFilter

    def get_queryset(self):
        return Program.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProgramEligibilityViewset(ModelViewSet):
    queryset = ProgramEligibility.objects.all()
    read_serializer_class = ProgramEligibilityReader
    write_serializer_class = ProgramEligibilityWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    filterset_class = ProgramEligibilityViewsetFilter

    def get_queryset(self):
        return ProgramEligibility.objects.for_user(self.request.user)

    def validate(self, request, data, action):
        validate_fields_with_rules(request.user, data, client='can_read_client', program='can_read_program')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EnrollmentViewset(ModelViewSet):
    queryset = Enrollment.objects.all()
    read_serializer_class = EnrollmentReader
    write_serializer_class = EnrollmentWriter
    permission_classes = [IsAdmin | IsAgencyMember]
    filterset_class = EnrollmentViewsetFilter

    def get_queryset(self):
        return Enrollment.objects.for_user(self.request.user)

    def validate(self, request, data, action):
        validate_fields_with_rules(request.user, data, client='can_read_client', program='can_read_program')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
