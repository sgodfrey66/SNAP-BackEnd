from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import ProgramEligibility, Enrollment, Program
# Register your models here.
admin.site.register(Program)


@admin.register(ProgramEligibility)
class ProgramEligibilityAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'status', 'client', 'program')


@admin.register(Enrollment)
class EnrollmentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'status', 'client', 'program')
