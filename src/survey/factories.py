import factory
from .models import Survey


class SurveyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Survey

    name = factory.Sequence(lambda n: f'Survey {n}')
    definition = {
        'items': [],
    }
