from django.contrib import admin
from survey.models import Survey, Question, Response, Answer


class AnswersInline(admin.TabularInline):
    model = Answer


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    inlines = (AnswersInline, )


admin.site.register(Survey)
admin.site.register(Question)
