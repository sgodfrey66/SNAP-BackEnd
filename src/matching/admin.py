from django.contrib import admin
from .models import MatchingConfig, ClientMatching, ClientMatchingHistory, ClientMatchingNote


class ClientMatchingHistoryInline(admin.TabularInline):
    model = ClientMatchingHistory


class ClientMatchingNotesInline(admin.TabularInline):
    model = ClientMatchingNote


class ClientMatchingAdmin(admin.ModelAdmin):
    inlines = [ClientMatchingHistoryInline, ClientMatchingNotesInline]

    class Meta:
        model = ClientMatching


admin.site.register(ClientMatching, ClientMatchingAdmin)
admin.site.register(MatchingConfig)
