import factory

from bas import models
from bas.models import BusPark, Bus


class BusParkFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    description = factory.Faker('text')

    class Meta:
        model = BusPark


class BusFactory(factory.django.DjangoModelFactory):
    number = factory.Faker('number')
    type_of_bus = factory.Faker('type_of_bus')

    class Meta:
        model = Bus