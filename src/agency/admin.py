from django.contrib import admin
from agency.models import Agency, AgencyClient


class AgencyClientInline(admin.TabularInline):
    model = AgencyClient


admin.site.register(Agency)
