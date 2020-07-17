from django.contrib import admin
from survey.models import Survey, Question, Response, Answer
from .forms import SurveyAdminForm


class AnswersInline(admin.TabularInline):
    model = Answer


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    inlines = (AnswersInline, )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'usage_count')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    form = SurveyAdminForm
