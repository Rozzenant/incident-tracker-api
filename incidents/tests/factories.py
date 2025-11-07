import factory
from incidents.models import Incident


class IncidentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Incident

    description = factory.Faker("sentence", nb_words=20)
    status = factory.Iterator(["open", "in_progress", "resolved"])
    source = factory.Iterator(["operator", "monitoring", "partner"])
