from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from agency.models import Agency
from .models import Eligibility, AgencyEligibilityConfig, ClientEligibility

# Register your models here.
admin.site.register(AgencyEligibilityConfig)


@admin.register(ClientEligibility)
class ClientEligibilityAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'status', 'client')


@admin.register(Eligibility)
class ProgramAdmin(admin.ModelAdmin):
    class AgenciesInline(admin.TabularInline):
        model = Agency.eligibility.through
        exclude = ['created_by']

    inlines = (AgenciesInline, )
