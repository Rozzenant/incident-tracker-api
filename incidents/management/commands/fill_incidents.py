from django.core.management.base import BaseCommand
from incidents.tests.factories import IncidentFactory
# from incidents.models import Incident

class Command(BaseCommand):
    help = "Создаёт 300 тестовых инцидентов в sqlite"

    def handle(self, *args, **kwargs):
        count = 300

        # Очистка
        # Incident.objects.all().delete()

        # Создание
        self.stdout.write(f"Создаём {count} инцидентов...")
        IncidentFactory.create_batch(count)

        self.stdout.write(self.style.SUCCESS(f"Создано {count} инцидентов"))
