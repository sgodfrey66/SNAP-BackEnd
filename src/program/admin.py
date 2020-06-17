from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Program, Enrollment, AgencyProgramConfig
# Register your models here.

admin.site.register(Program)
admin.site.register(AgencyProgramConfig)


@admin.register(Enrollment)
class EnrollmentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'status', 'client', 'program')

# @admin.register(Program)
# class ProgramAdmin(admin.ModelAdmin):
#     class AgenciesInline(admin.TabularInline):
#         model = Agency.programs.through

#     inlines = (AgenciesInline, )
