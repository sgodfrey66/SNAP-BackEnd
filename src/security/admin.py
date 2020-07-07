from django.contrib import admin
from agency.models import Agency
from .models import SecurityGroup, SecurityGroupAgencyConfig


admin.site.register(SecurityGroupAgencyConfig)


@admin.register(SecurityGroup)
class SecurityGroupAdmin(admin.ModelAdmin):
    class AgenciesInline(admin.TabularInline):
        model = Agency.security_groups.through
        exclude = ['created_by']

    inlines = (AgenciesInline, )
