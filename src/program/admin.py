from django.contrib import admin
from .models import Program
from agency.models import Agency
# Register your models here.


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    class AgenciesInline(admin.TabularInline):
        model = Agency.programs.through

    inlines = (AgenciesInline, )
