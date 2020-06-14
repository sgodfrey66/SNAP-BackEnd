import factory
from agency.factories import AgencyFactory
from .models import Program


class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Program

    name = factory.Sequence(lambda n: f'Program {n}')
    description = factory.LazyAttribute(lambda obj: f'Description for {obj.name}')


class AgencyWithPrograms(AgencyFactory):

    @factory.post_generation
    def num_programs(obj, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            assert isinstance(extracted, int)
            programs = ProgramFactory.create_batch(extracted)
            obj.programs.set(programs)
